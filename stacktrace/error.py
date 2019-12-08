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