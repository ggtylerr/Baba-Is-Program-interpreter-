import parser
import sys
from stacktrace import error

path = 'code.baba'
if (len(sys.argv) == 2):
  path = sys.argv[1]
elif (len(sys.argv) > 2):
  error.tooManyArgs()

data = ""
try:
  with open(path,'r') as file:
    data = file.read().replace('\n',' \\n ')
except:
  error.unknownFile()

parser.parse(data)