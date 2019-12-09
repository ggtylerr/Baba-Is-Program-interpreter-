from util import utilStr
from stacktrace import error
from Type import determine

def calc(rawList,i,varDict):
  returnInt = 0
  testBool = False
  k = i
  j = 0
  while (i < len(rawList)):
    try:
      testBool = utilStr.equals_caseless(rawList[i + 1],"\\n") or utilStr.equals_caseless(rawList[i + 1],"and")
    except:
      error.invalidSyntax()
    if testBool:
      j = i
      break
    else:
      i += 1
  prevCalc = ""
  firstTime = True
  while (k <= j):
    if utilStr.equals_caseless(rawList[k],"plus"):
      prevCalc = "+"
    elif utilStr.equals_caseless(rawList[k],"minus"):
      prevCalc = "-"
    elif not prevCalc == "" or firstTime:
      checkType = determine.Type(rawList,k,varDict)
      currInt = 0
      if (checkType == "Integer"):
        currInt = int(rawList[k])
      elif (checkType == "Variable"):
        currInt = varDict[rawList[k]]
      if prevCalc == "+" or firstTime:
        returnInt += currInt
      else:
        returnInt -= currInt
      firstTime = False
      prevCalc = ""
    else:
      error.invalidSyntax()
    k += 1
  return returnInt