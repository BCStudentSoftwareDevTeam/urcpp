# URCPP
URCPP stands for Undergraduate Research and Creative Projects Proposal. It is the system that faculty use to propose funded research project for the summer. This particular system has been used for two years.

# Getting Started
These Instruction will get you a copy of the project up and running on a local machine.

## Prerequisites

These are the things you will need to have installed before setting up for development 

* Python Version 2.7
* VirtualEnv
* MySQL

## Set Up the Environment
1. Make sure that database server is started `mysqld start`
2. run `source setup.py`
3. run flask `python api.py`

## file system map

├── API
│   ├── __init__.py
│   ├── bnumbers.py
│   ├── budget.py
│   ├── collaborators.py
│   ├── committee.py
│   ├── faculty.py
│   ├── files.py
│   ├── get.py
│   ├── makeExcel.py
│   ├── parameters.py
│   ├── programs.py
│   ├── projects.py
│   └── voting.py
├── README.md
├── __init__.py
├── chair
│   ├── __init__.py
│   ├── chair.py
│   ├── email_accepted.py
│   ├── forms.py
│   ├── manageCommittee.py
│   └── setParameters.py
├── committee
│   ├── __init__.py
│   ├── allBudgets.py
│   ├── allFiles.py
│   ├── allLabor.py
│   ├── allProjects.py
│   ├── allVotes.py
│   ├── castVote.py
│   ├── committee.py
│   └── vote.py
├── config.py
├── config.yaml
├── dashboard.py
├── everything.py
├── flaskLogin.py
├── globalroutes.py
├── models.py
├── pages
│   ├── __init__.py
│   ├── budget.py
│   ├── create.py
│   ├── done.py
│   ├── download.py
│   ├── history.py
│   ├── irbyn.py
│   ├── people.py
│   └── upload.py
├── redirectback.py
├── secret_key
├── set.py
├── static
│   ├── css
│   └── js
│       └── pages
│           └── upload
└── templates
    ├── chair
    ├── committee
    ├── pages
    └── snips

## Adding Models

1. Add models to models.py
2. Add Models to Config

# Built With

* Flask
* MySQL
* others

# Authors
Austin Farmer - Original System
Cody Myers
Guillermo Ramos Macias
Dr. Matt Jadud
Dr. Scott Heggen


# Next Steps
These are what I personally envision for this system

Testing - All systems should be tested thoroughly this one is no different.
Better Versioning - DevOps on this system should be better

