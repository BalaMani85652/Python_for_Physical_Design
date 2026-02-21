#Regex = percision parsing
#Regex = pattern matching tool


import re
line = "Path clg_reg1_to_reg2 Slack = -0.35ns"


#Extracting slack from the line
slack_match = re.search(r"-?\d+\.\d+",line)
if slack_match:
	slack = float(slack_match.group())										#Returns the matched text
	print("Slack:",slack)


#Extracting path fro the line
path_match = re.search(r"Path\s+(\S+)",line)
if path_match:
	path = path_match.group(0)
	print("Path:",path)
	
	
	
#match = re.search(r"-?\d+\.\d+",line)
#   -?      → optional negative sign
#	\d+     → digits
#	\.      → decimal point
#	\d+     → digits 

