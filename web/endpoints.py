from everything import *

#################################################################
@app.route("/{0}/_/getcorresponding/<username>".format(cfg['tag']))
def _getcorresponding (username):
  fac = getcorresponding (username)
  if fac:  
    json = jsonify(m2d(fac))
    return json
  else:
    return jsonify({})
    
def getcorresponding (username):
  app.logger.info("endpoint: getcorresponding for {0}".format(username))
  facQ = (Faculty.select()
    .join(FacultyProjects, on = (FacultyProjects.fid == Faculty.fid))
    .join(Projects, on = (FacultyProjects.pid == Projects.pid))
    .where(Faculty.username == username)
    .where(FacultyProjects.corresponding == True)
    )

  if facQ.exists():
    fac = facQ.get()
    app.logger.info("Fetched Corresponding Faculty: {0}".format(fac))
    return fac
  else:
    app.logger.info("Corresponding faculty {0} not found.".format(username))
    return None
    
#################################################################
@app.route("/{0}/_/getproject/<username>".format(cfg['tag']))
def _getproject (username):
  proj = getproject (username)
  if proj:
    json = jsonify(m2d(proj))
    return json
  else:
    return jsonify({})
    
def getproject (username):
  app.logger.info("endpoint: getproject")
  # Run the query. There MUST be only one project for
  # which they are corresponding.
  theFaculty = getcorresponding(username)
  if theFaculty:
    projectQ = (Projects.select()
      .join (FacultyProjects, on = (FacultyProjects.pid == Projects.pid))
      .where (theFaculty.fid == FacultyProjects.fid)
      .where (FacultyProjects.corresponding  == True)
      )

    if projectQ.exists():
      return projectQ.get()
  else:
    return None
    
#################################################################
@app.route("/{0}/_/bybnumber/<bnumber>".format(cfg['tag']))
def _bybnumber (bnumber):
  ldapQ = (LDAPFaculty.select()
    .where (LDAPFaculty.bnumber == bnumber)
  )
  
  fac = None
  if ldapQ.exists():
    fac = ldapQ.get()
  
  if fac:  
    json = jsonify(m2d(fac))
    return json
  else:
    return jsonify({})
  
  
#################################################################
@app.route("/{0}/_/getprojectfaculty/<username>".format(cfg['tag']))
def _getprojectfaculty (username):
  collabs = getprojectfaculty (username)
  res = {}
  for fac in collabs:
    res[fac.fid] = m2d(fac)
  return jsonify(res)

def getprojectfaculty (username):
  # We have the username of the corresponding faculty member.
  # We want all the other faculty on this project.
  corrFacQ = (Faculty.select()
    .where(Faculty.username == username)
  )
  corrFac = corrFacQ.get()
  
  # Now, we have the corresponding faculty member. From here, we want
  # to get their project.
  fpQ = (FacultyProjects.select()
    .where (FacultyProjects.fid == corrFac.fid)
    .where (FacultyProjects.corresponding == True)
  )
  fp = fpQ.get()
  
  # Now, we know the project id for their project. From here, we
  # can look for all the entries that match that pid.
  # But, don't include the original faculty member.
  fpQ = (FacultyProjects.select()
    .where (FacultyProjects.pid == fp.pid)
    .where (FacultyProjects.fid != corrFac.fid)
  )
  fps = fpQ.select()
  
  # Now, we have a list of faculty project entries.
  collabs = []
  for fp in fps:
    facsQ = (Faculty.select()
      .where (Faculty.fid == fp.fid)
      )
    if facsQ.exists():
      collabs.append(facsQ.get())
  
  # This should be the list of faculty we want.
  return collabs
