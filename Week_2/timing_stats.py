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
				
if violations:
	slacks = list(violations.values())
	average_slack = sum(slacks)/len(slacks)
	worst_slack = min(slacks)
	best_slack = max(slacks)
	print("----Timing Statistics----")
	print("Average slack:",average_slack)
	print("Worst slack:",worst_slack)
	print("Best slack:",best_slack)


if average_slack < -0.2:
	print("Timing status: CRITICAL")
else:
	print("Timing status: WARNING")
