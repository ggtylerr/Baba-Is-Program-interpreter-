from util import utilStr

def Type(rawList,i,varDict):
  returnType = "unknown"
  if (utilStr.enclosed(rawList[i],"\"")):
    returnType = "String"
  elif (utilStr.checkInt(rawList[i])):
    returnType = "Integer"
  elif (rawList[i] in varDict):
    returnType = "Variable"
  return returnType