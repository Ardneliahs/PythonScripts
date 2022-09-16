import re

my_string = re.compile(r'.{6}\|[a-zA-Z0-9]{4}\|[0-9]{4}')

with open("sample.txt") as logfile:
  loglines = logfile.readlines()
  for lines in loglines:
    my_output = re.search(my_string,lines)
    if type(my_output) != "None":
      print(lines[0:20] + my_output.group())
