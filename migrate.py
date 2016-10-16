# import the migrator
from playhouse.migrate import *
# import model for database
from api.models import *

migrator = MySQLMigrator(dynamicDB)

# Create your field instances. For non-null fields you must specify a
# default value.
isChair     = BooleanField(default=False)
isCommitteeMember = BooleanField(default=False)

# Run the migration, specifying the database table, field name and field.
migrate(
    migrator.add_column('ldapfaculty', 'isChair', isChair),
    migrator.add_column('ldapfaculty', 'isCommitteeMember', isCommitteeMember),
)