from ldap3 import Server, Connection, ALL
from peewee import *
from os import path, remove
from api.models import *
import argparse

# Create database connection and model
database_path = "LDAP.db"
database = SqliteDatabase(database_path)

class Faculty(Model):
    fID               = PrimaryKeyField()
    username          = CharField(unique = True)
    bnumber           = TextField(null = True)
    lastname          = TextField(null = True)
    firstname         = TextField(null = True)

    class Meta:
        database = database

class Staff(Model):
    sID               = PrimaryKeyField()
    username          = CharField(unique = True)
    bnumber           = TextField(null = True)
    lastname          = TextField(null = True)
    firstname         = TextField(null = True)
    class Meta:
        database = database


def connect_to_server(user,password):
    server = Server ('berea.edu', port=389, use_ssl=False, get_info='ALL')
    # conn   = Connection (server, user=skt['ldap']['user'], password=skt['ldap']['pass'])
    conn   = Connection (server, user=user, password=password)
    if not conn.bind():
        print(conn.result)
        raise Exception("BindError")
    return conn

def grab_faculty(connection):
    return grab_data(connection, "Faculty")

def grab_staff(connection):
    return grab_data(connection,"Staff")

def grab_data(connection, description):
    # search_base and search_filter are the parameters
    connection.search('dc=berea,dc=edu',
      '(description=%s)' % (description),
      attributes = ['samaccountname', 'givenname', 'sn', 'employeeid']
      )

    return connection.entries

def grab_key(entry, key):
    if key in entry:
        return entry[key]
    else:
        return None


def dump_to_database(entries, Table):
    for entry in entries:
        row = Table(
            username          = grab_key(entry,'samaccountname'),
            bnumber           = grab_key(entry,'employeeid'),
            lastname          = grab_key(entry,'sn'),
            firstname         = grab_key(entry,'givenname')
        )
        row.save()


def main(user,password):
    pull_database(user, password)
    print("Adding new members")
    add_members()
    
def add_members():
    current_users = LDAPFaculty.select(LDAPFaculty.username)
    user_list = list()
    for user in current_users:
        user_list.append(user.username)
    new_users = Faculty.select().where( ~ (Faculty.username << user_list))
    print("Adding %s new members" %(str(len(new_users))))
    for user in new_users:
        if user.bnumber is None:
            print(user.username)
            continue
        
        new_user = LDAPFaculty.create(
                username = user.username,
                bnumber = user.bnumber,
                lastname = user.lastname,
                firstname = user.firstname
            )
        new_user.save()
        
def pull_database(user,password):
    print("Connecting to Database")
    database.connect()
    print("Dropping and creating tables")
    if path.isfile(database_path):
        try:
            database.drop_tables([Faculty, Staff])
        except Exception:
            pass
    database.create_tables([Faculty, Staff])
    print("Connecting to server")
    connection = connect_to_server(user,password)
    print("Grabbing data")
    faculty = grab_faculty(connection)
    # staff = grab_staff(connection)
    print("Dumping Data")
    dump_to_database(faculty, Faculty)
    # dump_to_database(Staff, Staff)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pull and Sync Faculty from LDAP')
    parser.add_argument('--user', help='Username for LDAP')
    parser.add_argument('--password', help="Password for LDAP")
    args = parser.parse_args()
    
    main(args.user, args.password)

