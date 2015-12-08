from ldap3 import Server, Connection, ALL
from peewee import *
from api.everything import *

cfg = load_config('api/config.yaml')
# skt = load_config('api/secret_config.yaml')

theStaticDB = SqliteDatabase(cfg['databases']['static'])
theStaticDB.drop_table(LDAPFaculty)

server = Server ('berea.edu', port=389, use_ssl=False, get_info='ALL')
# conn   = Connection (server, user=skt['ldap']['user'], password=skt['ldap']['pass'])
conn   = Connection (server, user="BPLP", password="Ol1v4r!Tun4bp")
if not conn.bind():
    print('error in bind', conn.result)

# search_base and search_filter are the parameters
conn.search('dc=berea,dc=edu', 
  '(description=Faculty)', 
  attributes = ['samaccountname', 'givenname', 'sn', 'employeeid']
  )

print ("Found {0} faculty.".format(len(conn.entries))) 

# print (conn.entries[0])

def safe (d, k):
  result = ""
  try:
    if k in d:
      result = d[k]
  # If we can't find a key, skip it.
  except:
    pass
  
  return result
    
# Recreate the table.
theStaticDB.create_table(LDAPFaculty)

faculty = conn.entries
for fac in faculty:
  print ("Faculty: {0}".format(fac.samaccountname))
  o = LDAPFaculty (
    lastname  = safe (fac, 'sn'),
    firstname = safe (fac, 'givenname'),
    username  = fac.samaccountname,
    bnumber   = safe (fac, 'employeeid'),
    )
  o.save()