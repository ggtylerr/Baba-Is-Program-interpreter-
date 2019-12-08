from util import utilStr
from stacktrace import error
import shlex

def parse(raw):
  rawList = shlex.split(raw, posix=False)
  vars = []
  i = 0
  while (i < len(rawList)):
    curr = rawList[i]
    if (utilStr.equals_caseless(curr,"say")):
      printString = rawList[i + 1]
      if (utilStr.enclosed(printString,"\"")):
        print(utilStr.removeStartAndEnd(printString))
      else:
        error.unrecognizedVar()
      i = i + 1
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
      
    i = determineNextIndex(rawList,i)

def determineNextIndex(rawList,i):
  testBool = False
  try:
    testBool = utilStr.equals_caseless(rawList[i + 1] == "\\n") or utilStr.equals_caseless(rawList[i + 1] == "and")
  except:
    testBool = False
  if testBool:
    i += 2
  else:
    i += 1
  return i