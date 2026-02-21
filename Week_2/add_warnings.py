
import re
violations = {}	
critical = 0
warning = 0
minor =0

# --- Parse timing report ---
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
				
				
sorted_violations =sorted(violations.items(),
							key = lambda x : x[1])
print("\n====Sverity Classification====")
for path,slack in sorted_violations:
	if slack < -0.3:
		severity = "CRITICAL"
		critical += 1
	elif slack < -0.1:
		severity = "WARNING"
		warning += 1
	else:
		severity = "MINOR"
		minor += 1
	print(path,"->",slack,"|",severity)
print("\n==== Dashboard Summary ====")
print("Critical violations:",critical)
print("Warning:",warning)
print("Minor violations:",minor)
