from util import utilStr
from stacktrace import error
from Type import determine

def on(rawList,i,varDict):
  returnString = ""
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
  while (k <= j):
    if not utilStr.equals_caseless(rawList[k],"plus"):
      checkType = determine.Type(rawList,k,varDict)
      if (checkType == "String"):
        returnString += utilStr.removeStartAndEnd(rawList[k])
      elif (checkType == "Integer"):
        returnString += rawList[k]
      elif (checkType == "Variable"):
        returnString += varDict[rawList[k]]
      else:
        error.unrecognizedVar()
    k += 1
      
  return [returnString,j]