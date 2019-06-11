from everything import *

# Routes used everywhere, like static and templates
import api.globalroutes

# Our getters
import api.dashboard
import api.contrib

# Our API
import API.bnumbers
import API.collaborators
import API.faculty
import API.makeExcel
import API.programs
import API.projects




# Form pages
import pages.create
import pages.people
import pages.history
import pages.irbyn
import pages.upload
import pages.done
import pages.budget
import pages.download

#Committee pages
import committee.committee
import committee.allBudgets
import committee.allProjects
import committee.allFiles
import committee.allLabor

# import committee.vote
import committee.allVotes
import committee.castVote

#Chair pages
import chair.chair
import chair.awardLetters
import chair.setParameters
import chair.manageCommittee
import chair.email_accepted

import flaskLogin
