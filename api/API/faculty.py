from ..everything import *
import json
import projects

def getLDAPFaculty (username):
  """ gets the LDAPFaculty by username
      
      Args:
        username (str): the username that your are looking format
      
      Returns:
        LDAPFaculty Object, None: the LDAPfaculty object if it finds it otherwise None
  
  """
  ldapQ = (LDAPFaculty.select()
    .where (LDAPFaculty.username == username)
    )
  
  if ldapQ.exists():
    return ldapQ.get()
  else:
    return None
  
  
def get_faculty_by_bnumbers(*bnumbers):
  """ gets the faculty from bnumbers 
      
      Args:
        *bnumbers (*): the bnumber of the faculty that we are trying to get
      Returns:
        Peewee Object: the select query of the faculty
  """
  return LDAPFaculty.select().where(LDAPFaculty.bnumber << bnumbers)
        
      
def getFaculty (username):
  """ gets the URCPPfaculty by username
      
      Args:
        username (str): the username that is being looked for
        
      Returns:
        URCPPfaculty Object, None: The URCPPFaculty object or None
  """
  facQ = (URCPPFaculty.select()
    .where (URCPPFaculty.username == username)
    )

  if facQ.exists():
    return facQ.get()
  else:
    return None
    
def getFacultyByYear (username, year):
  """ gets the faculty with project for a given years
  
      Args:
        username (str): the username that is being looked for
        year (int): the year that this faculty would belong to
        
      Returns:
      URCPPFaculty Object: the faculty in that year
      
  """
  facQ = (URCPPFaculty.select().join(Projects)
    .where (URCPPFaculty.username == username)
    .where (Projects.year == year)
    )

  if facQ.exists():
    return facQ.get()
  else:
    return None


def getFacultyWithProjects (year):
  """ gets faculty with project for a given year 
  
      Args:
        year (int): the year that the faculty should have a project
        
      Returns:
      URCPPFaculty Select Query: The faculty that have a prject in that year
  """
  facQ = (URCPPFaculty.select().join(Projects).where(Projects.year == year))

  if facQ.exists():
    return facQ.execute()
  else:
    return None


def getFacultyWithPendingProjects ():
  """ gets the faculty that have started but not submitted a project
  
      Returns:
        URCPPFaculty Select Query: the faculty with pending Projects
        
  """
  facQ = (URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["Pending"])
                        .where(Projects.pID == URCPPFaculty.pID)
                        )

  if facQ.exists():
    return facQ.execute()
  else:
    return None
    
def getFacultyForProject (pid):
  """ gets the faculty that belong to a project
  
      Args:
      pid (int): the project id
      
      Returns:
        URCPPFaculty Object: the faculty that owns the project
        
  """
  facQ =  ( URCPPFaculty.select()
                        .where(URCPPFaculty.pID == pid)
          )
  if facQ.exists():
    return facQ.get()
  else:
    return None

def getFacultyWithAcceptedProjects(year=None):
  """ gets the faculty that have projects that have been accepted
  
      Returns:
        URCPPFaculty Select Query: the faculty with accepted Projects
        
  """
  
  
  facQ = ( URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["Accept"])
          )
  if year is not None:
    facQ = facQ.where(Projects.year == year).execute()
  if facQ:
    return facQ
  else:
    return None

def getFacultyWithRejectedProjects():
  """ gets the faculty that have projects that have been rejected
  
      Returns:
        URCPPFaculty Select Query: the faculty with rejected projects
  """
  facQ = ( URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["Reject"])
          )
          
  if facQ.exists():
    return facQ.execute()
  else:
    return None
    
@app.route("/urcpp/v1/faculty/get/<username>", methods = ["POST"])
def faculty_get (username):
  """ gets the LDAPFaculty by username
      
      Args:
        username (str): the username that your are looking format
      
      Returns:
        JSON: Dictionary of the faculty or noResults
  
  """
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  fac = getFaculty(username)  
  ldap = getLDAPFaculty(username)
  
  if fac and ldap:
    response = {  "response" : "OK" }
    response["faculty"] = m2d(fac)
    response["details"] = m2d(ldap)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No faculty found for username {0}.".format(username)
                 }
    return jsonify(response)  

