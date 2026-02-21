
import re
violations = {}	


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
				
#--- Sort violations ---				
sorted_violations =sorted(violations.items(),
							key = lambda x : x[1])


#--- Severity dashboard ---
critical = warning = minor = 0
print("\n==== Timing Dashboard ====")
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


#--- Summary ---
print("\n---- Summary ----")
print("Total violations:",len(violations))
print("Critical:",critical)
print("Warnings:",warning)
print("Minor:",minor)


#for path,slack in violations.items():
worst_path = min(violations)
print("Worst_path:",worst_path,"| Slack:",violations[worst_path])

         #OR
'''
if violations:
	worst_path= min(violations, key=violations.get)						#key=violations.get--->Extract values from dictionary(violations) and return the key
	print("Worst_path:",worst_path,"| Slack:",violations[worst_path])
'''
















