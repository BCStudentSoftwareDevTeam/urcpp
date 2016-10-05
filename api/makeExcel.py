import xlsxwriter
from everything import *
from string import ascii_uppercase as AtoZ
from faculty import getFacultyWithProjects
from parameters import getParameters
from applicationCycle import getCurrentCycle


def getFilename(fileType):
  cycle = getCurrentCycle()
  fileName = cfg["downloads"]["downloadFileNameFormat"]
  fileType = cfg["downloads"]["downloadFileTypes"][fileType]
  fileName = fileName.replace("%%applicationCycle%%", str(cycle.year))
  fileName = fileName.replace("%%downloadFileType%%", fileType)
  return fileName

def getFilePath(fileType):
  '''
  This function returns the filepath with the filename and extension to be written into
  '''
  cycle = getCurrentCycle()
  writeFileName = getFilename(fileType)
  writeFileType = cfg["downloads"]["downloadFileTypes"][fileType]
  fileExtension = cfg["downloads"]["downloadFileExtension"]
  relPath = cfg["filepaths"]["projectFiles"] + str(cycle.year) + "/" + writeFileType + "/" + writeFileName + fileExtension
  here = os.path.dirname(__file__)
  return os.path.join(here, relPath)

def checkFilePath(fileType):
  '''
  This function checks if the filepath for the fileType exists, if not it creates the filepath.
  '''
  applicationCycle = getCurrentCycle()
  fileType = cfg["downloads"]["downloadFileTypes"][fileType]
  path = cfg["filepaths"]["projectFiles"] + str(applicationCycle.year)
  here = os.path.dirname(__file__)
  path = os.path.join(here, path)
  if os.path.isdir(path):
    pass
  else:
    os.mkdir(path)
  
  path = path + "/" + fileType
  if os.path.isdir(path):
    pass
  else:
    os.mkdir(path)

def makeBudgetExcel():
  applicationCycle = getCurrentCycle()
  faculty = getFacultyWithProjects()
  params = getParameters()
  
  checkFilePath("allBudgets")
  writeFilePath = getFilePath("allBudgets")

  workbook = xlsxwriter.Workbook(writeFilePath)
  workbook.set_properties({
  'title':    'Budget for {}'.format(applicationCycle.year),
  'author':   'URCPP System',
  'comments': 'Created with Python and XlsxWriter'})
  
  # create a worksheet
  worksheet = workbook.add_worksheet('All Budgets')
  worksheetRow = 1
  
  # add titles
  letterCount = 0
  worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow),'Faculty/Proj. Title')
  letterCount += 1
  worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow),'Project Status')
  letterCount += 1
  for title in cfg["budget"]:
    worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow), title['title'])
    letterCount += 1
  worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow),'Total')
  worksheetRow += 1
  lastColumnCount = letterCount # we need the lastColumn's letter later
  
  
  #loop though the budgets
  for person in faculty:
    letterCount = 0
    facProjStr = '{0} {1} ({2})\n{3}'.format(person.username.firstname, person.username.lastname, person.programID.name, person.pID.title)
    wordWrap = workbook.add_format()
    wordWrap.set_text_wrap()
    worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow), facProjStr, wordWrap)
    letterCount += 1
    worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow), person.pID.status)
    letterCount += 1

    budget = m2d(person.pID.budgetID)
    for field in cfg["budget"]:
      if field['amountFieldName'] == "miles":
        twoSF = workbook.add_format()
        twoSF.set_num_format('0.00')
        milesCost = budget[field['amountFieldName']] * params.mileageRate * 1.0
        worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow), milesCost, twoSF)
      else:
        worksheet.write('{0}{1}'.format(AtoZ[letterCount], worksheetRow), budget[field['amountFieldName']])
      letterCount += 1
    
    # write the total formula for each row
    worksheet.write_formula('{0}{1}'.format(AtoZ[letterCount], worksheetRow), '{{=SUM({0}{1}:{2}{1})}}'.format(AtoZ[2], worksheetRow, AtoZ[lastColumnCount-1]))
    worksheetRow += 1
  
  # write the grand total
  worksheet.write('{0}{1}'.format(AtoZ[0], worksheetRow), 'Grand Total')
  worksheet.write_formula('{0}{1}'.format(AtoZ[lastColumnCount], worksheetRow), '{{=SUM({0}{1}:{0}{2})}}'.format(AtoZ[lastColumnCount], 2, worksheetRow-1))
  
  workbook.close()

def makeLaborExcel():
  applicationCycle = getCurrentCycle()
  faculty = getFacultyWithProjects()
  params = getParameters()
  
  checkFilePath("allLabor")
  writeFilePath = getFilePath("allLabor")

  workbook = xlsxwriter.Workbook(writeFilePath)
  workbook.set_properties({
  'title':    'Labor for {}'.format(applicationCycle.year),
  'author':   'URCPP System',
  'comments': 'Created with Python and XlsxWriter'})
  
  # create a worksheet
  worksheet = workbook.add_worksheet('All Budgets')
  row = 0
  
  # add titles
  worksheet.write(row, 0, 'Faculty/Proj. Title')
  worksheet.write(row, 1, '# Students')
  worksheet.write(row, 2, 'Duration')
  worksheet.write(row, 3, 'Total')
  row += 1
  
  #loop though the budgets
  for person in faculty:
    facProjStr = '{0} {1} ({2})\n{3}'.format(person.username.firstname, person.username.lastname, person.programID.name, person.pID.title)
    wordWrap = workbook.add_format()
    wordWrap.set_text_wrap()
    worksheet.write(row, 0, facProjStr, wordWrap)
    worksheet.write(row, 1, person.pID.numberStudents)
    worksheet.write(row, 2, person.pID.duration)
    worksheet.write_formula(row, 3, '{{=B{0}*C{0}*{1}*40}}'.format(row+1, params.laborRate))
    row += 1
  
  # write the grand total
  worksheet.write(row, 0, 'Grand Total')
  worksheet.write_formula(row, 3, '{{=SUM({0}{1}:{0}{2})}}'.format(AtoZ[3], 2, row))
  
  workbook.close()
