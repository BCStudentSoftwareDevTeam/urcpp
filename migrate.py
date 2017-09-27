# import the migrator
from playhouse.migrate import *
# import model for database
from api.models import *


email_body = """The Undergraduate Research and Creative Projects Program (URCPP) Committee is pleased to approve your request for funding for your summer 2017 faculty-student research project. The URCPP will fund $@@Funding@@ on your project: @@ProjectTitle@@, contingent on IRB approval if your research involves human subjects. Your program will run from @@Start Date@@ - @@End Date@@.

Your stipend of $@@Stipend@@ will be disbursed in one payment in June. You will be notified by Jim Strand which account number to use to report expenses for your project. He also will provide instructions to follow for obtaining reimbursements. Be sure to stay within the approved budget amount mentioned above. If you receive additional funding for this project not already indicated in your proposal, please alert Sarah Broomfield, because that may affect your eligibility for this URCPP award.

Your project has been approved for working with @@Students@@ students -- yet to be determined. When you have selected your student researchers, send Sarah Broomfield their name(s) and B-numbers (send to broomfields@berea.edu) and she will create an electronic labor status form which will be copied to the student, to you as the supervisor, and to the Student Labor Office. The student information will also be shared with the Student Service Center to enroll them in UGR 010 which, upon satisfactory completion, will earn an ALE credit, but does not earn credit towards graduation. Please be aware that students cannot be enrolled in another summer course at the same time as they are enrolled in UGR 010 (including the first four-week or eight-week summer sessions, internships, independent studies, other non-credit courses, etc.) and participate in summer research funded by the URCPP.

There are some requirements you must fulfill as a faculty member receiving URCPP funding. Failure to complete the following requirements will affect future URCPP funding.

1.     You are required to submit an "S" or "U" grade to Associate Registrar Kathy Wallace for each student's participation in the research/creative project. Your grades must be submitted before Thanksgiving Break.
2.     You are required to administer a Pre-Research Survey and Post-Research Survey to each student working with your project. Details about the surveys will be forthcoming. You and your students must participate in the weekly summer discussions where student researchers will be asked to share the progress they are making on their research.
3.     You are required to electronically submit an abstract and a one-page summary of the project, which is due to the Academic Vice President's Office no later than August 21, 2017. The abstract will be shared with the Development office (for donors) and published in the annual Journal of Undergraduate Research Abstracts, compiled by Ron Rosen; thus, it can be discipline-specific. The report is shared with the Academic Vice President and Dean of the Faculty and should be geared toward a more general audience.
4.     You are also required to participate in the Berea Undergraduate Research Symposium (BURS) in early October 2017.
5.     If your research involves human subjects, your funding is subject to IRB approval and you must complete and submit an application to the IRB by March 13, 2017. Please see the following definition in the faculty manual to confirm whether you research does or does need IRB approval http://catalog.berea.edu/en/Current/Catalog/Selected-Institution-Wide-Policies/Research-Involving-Human-Subjects). No URCPP funds will be dispersed to any research involving human subjects who has not received IRB approval. Questions regarding IRB application can be directed to the IRB chair, Wendy Williams (williams@berea.edu).

If you have any questions, please feel free to contact any member of the URCPP Committee. Congratulations and best wishes on the project!

Sincerely,
Martin Veillett

URCPC Chair"""

email_subject = """Summer 2017 Undergraduate Research and Creative Projects Program Proposal"""

# Create EmailTemplates DB
class EmailTemplates(DynamicModel):
  eID                   = PrimaryKeyField()
  Body                  = TextField(null = True)
  Subject               = TextField(null = True)
dynamicDB.create_tables([EmailTemplates])

emails = EmailTemplates (
                    Body      = email_body,
                    Subject      = email_subject
                  )
emails.save(force_insert=True)

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

