from api.everything import *

# Routes used everywhere, like static and templates
import api.globalroutes

# Our getters
import api.dashboard
import api.contrib

# Our API
import api.API.bnumbers
import api.API.collaborators
import api.API.faculty
import api.API.makeExcel
import api.API.programs
import api.API.projects




# Form pages
import api.pages.create
import api.pages.people
import api.pages.collaborations
import api.pages.irbyn
import api.pages.upload
import api.pages.done
import api.pages.budget
import api.pages.download

#Committee pages
import api.committee.committee
import api.committee.allBudgets
import api.committee.allProjects
import api.committee.allFiles
import api.committee.allLabor

# import committee.vote
import api.committee.allVotes
import api.committee.castVote

#Chair pages
import api.chair.chair
import api.chair.awardLetters
import api.chair.setParameters
import api.chair.manageCommittee
import api.chair.email_accepted

import api.flaskLogin
