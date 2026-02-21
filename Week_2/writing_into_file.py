#Writing timing summary into a file

violations = {}															#Intialising the empty dictionary

with open("timing.rpt.txt", "r") as f:
	for line in f:
		line =line.strip()												#Remove extra spaces and newline
		
		if line.startswith("Path:"):									#Detecting a line starts with "Path:"
			path =line.split(":")[1].strip()							
		
		elif line.startswith("Slack:"):									#Detecting a line starts with "Slack"
			slack =float(line.split(":")[1].strip())
			#print(slack)
			
			if slack < 0:
				violations[path] = slack
				#print(violations) ------> {'clk_reg3_to_reg4': -0.35, 'clk_mem_to_reg': -0.08}
				
total_violations = len(violations)										#2
#print(total_violations)

wns = min(violations.values())											#-0.35
#print(wns)

average_slack = sum(violations.values())/total_violations				#-0.215
#print(average_slack)

import datetime
with open("timing_summary.txt", "w")  as f:
	f.write("------ Timing Summary ------\n")
	f.write(f"Total Violations : {total_violations}\n")
	f.write(f"Worst Slack : {wns}\n")
	f.write(f"Average Slack : {average_slack}\n")
	f.write("-----------------------------\n")
	f.write(f"Gnerated on:{datetime.datetime.now()}")
print("Timing summary written to timing_summary.txt")
