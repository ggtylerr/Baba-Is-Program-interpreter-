import sys

def unrecognizedVar():
  print("ERROR: Unrecognized Variable!")
  sys.exit(-1)

def missingIs():
  print("ERROR: Missing \"is\" statement!")
  sys.exit(-1)

def doesntEnd():
  print("ERROR: Block doesn't end!")
  sys.exit(-1)

def invalidSyntax():
  print("ERROR: Invalid Syntax!")
  sys.exit(-1)

# Intrepreter only errors
def tooManyArgs():
  print("ERROR: Too many arguments!")
  sys.exit(-1)

def unknownFile():
  print("ERROR: Unknown file/path!")
  sys.exit(-1)