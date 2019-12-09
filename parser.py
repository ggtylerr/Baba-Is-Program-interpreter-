from util import utilStr
from stacktrace import error
from String import concatenation
from Type import determine
from Integer import maths
import shlex

def parse(raw):
  rawList = shlex.split(raw, posix=False)
  varDict = {}
  i = 0
  while (i < len(rawList)):
    curr = rawList[i]
    if (utilStr.equals_caseless(curr,"say")):
      temp = concatenation.on(rawList,(i + 1),varDict)
      print(temp[0])
      i = temp[1]
    elif (utilStr.equals_caseless(curr,"comment")):
      try:
        i = rawList.index("\\n",i) - 1
      except:
        i = len(rawList)
    elif (utilStr.equals_caseless(curr,"block-comment")):
      j = i + 1
      if (not utilStr.equals_caseless(rawList[j],"is")):
        error.missingIs();
      while (j < len(rawList)):
        if (utilStr.equals_caseless(rawList[j],"and")):
          if (utilStr.equals_caseless(rawList[j+1],"end")):
            if (utilStr.equals_caseless(rawList[j+2],"block-comment")):
              j += 2
              break
            else:
              j += 2
          else:
            j += 1
        j += 1
      if (j < len(rawList)):
        i = j
      else:
        error.missingIs()
    elif (utilStr.equals_caseless(rawList[i + 1],"is")):
      testBool = False
      try:
        testBool = rawList[i + 2] == "\\n" or utilStr.equals_caseless(rawList[i + 2],"and")
      except:
        testBool = False
      if not testBool:
        i += 2
        checkType = determine.Type(rawList,i,varDict)
        definition = ""
        if (checkType == "String"):
          definition = concatenation.on(rawList,i,varDict)[0]
        elif (checkType == "Integer"):
          definition = maths.calc(rawList,i,varDict)
        elif (checkType == "Variable"):
          if (not utilStr.checkInt(varDict[rawList[i]])):
            definition = concatenation.on(rawList,i,varDict)[0]
          else:
            definition = maths.calc(rawList,i,varDict)
        elif (checkType == "Input"):
          rawList[i] = "\"" + input() + "\""
          definition = concatenation.on(rawList,i,varDict)[0]
        else:
          error.unrecognizedVar()
        varDict[rawList[i-2]] = definition
      else:
        error.invalidSyntax()
    i = determineNextIndex(rawList,i)

def determineNextIndex(rawList,i):
  testBool = False
  try:
    testBool = rawList[i + 1] == "\\n" or utilStr.equals_caseless(rawList[i + 1],"and")
  except:
    testBool = False
  if testBool:
    i += 2
  else:
    i += 1
  return i