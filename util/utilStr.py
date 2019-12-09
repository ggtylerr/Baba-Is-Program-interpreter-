'''
utilStr

Useful stuff regarding strings
'''

import unicodedata

def normalize_caseless(text):
  '''
  Normalizes and casefolds text using unicodedata.
  '''
  return unicodedata.normalize("NFKD", text.casefold())

def equals_caseless(left, right):
  '''
  Tests if two case-insensitive strings are equal.
  '''
  return normalize_caseless(left) == normalize_caseless(right)

def enclosed(string,char):
  '''
  Checks if string is enclosed with char.
  '''
  return string.startswith(char) and string.endswith(char)

def removeStart(string):
  '''
  Removes the starting character of a string.
  '''
  return string[1:]

def removeEnd(string):
  '''
  Removes the ending character of a string.
  '''
  return string[:-1]

def removeStartAndEnd(string):
  '''
  Removes the start and end characters of a string.
  '''
  return removeStart(removeEnd(string))

def checkInt(string):
  '''
  Checks if a string is an integer
  '''
  try:
    if string[0] in ('-', '+'):
      return string[1:].isdigit()
    return string.isdigit()
  except:
    if type(string) is int:
      return True
    else:
      return False