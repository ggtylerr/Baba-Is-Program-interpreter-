import parser

data = ""

with open('code.baba','r') as file:
  data = file.read().replace('\n',' \\n ')

parser.parse(data)