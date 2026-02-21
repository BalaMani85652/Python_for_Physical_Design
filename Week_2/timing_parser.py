import re
violations = {}
with open("timing.rpt.txt", "r") as f:
	for line in f:
		path_match= re.search(r"Path:\s(\S+)",line)
		slack_match= re.search(r"-?\d+\.\d+",line)
		if path_match:
			path = path_match.group(1)
			#print(path)
		if slack_match:
			slack = float(slack_match.group())
			#print(slack)
			if slack < 0:
				violations[path] = slack

#Printing Violations
print("\nViolations Found")
for p,s in violations.items():
	print(p,"---->",s)


#Sorting the violations based on slack
sorted_violations = sorted(violations.items(),
							key=lambda x:x[1]
						)
print("\nSorted Violations")
for p,s in sorted_violations:
	print(p,"--->",s)


#Top Violating paths
print("\nTop Violating paths")
for p,s in sorted_violations[:1]:
	print(p,"--->",s)

	
