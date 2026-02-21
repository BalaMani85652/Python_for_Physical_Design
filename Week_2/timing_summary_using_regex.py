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

#Sorting the violations based on slack
sorted_violations = sorted(violations.items(),
							key=lambda x:x[1]
						)
						
total_paths = len(violations)
if violations:
	worst_slack = min(violations.values())
	best_slack = max(violations.values())
else:
	worst_slack = 0
	best_slack = 0
print("------Timing Summary-----")
print("Total violations:",total_paths)
print("Worst slack",worst_slack)
print("Best slack",best_slack)


#Print Top N violations
print("\n------Top Violations-----")
N = 2
for path,slack in sorted_violations[:N]:
	print(path,"--->",slack)
	
	
	
#Writing into a file
with open("violations.csv","w") as out:
	out.write("------Timing Summary-----")
	out.write(f"\nTotal violations:{total_paths}")
	out.write(f"\nWorst slack:{worst_slack}")
	out.write(f"\nBest slack:{best_slack}")
	for path,slack in sorted_violations:
		out.write(f"\n{path},{slack}")
print("\nCSV file created: violations.csv")
		

