from util import utilStr
from stacktrace import error

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
      if (utilStr.enclosed(rawList[k],"\"")):
        returnString += utilStr.removeStartAndEnd(rawList[k])
      else:
        error.unrecognizedVar()
    k += 1
      
  return [returnString,j]