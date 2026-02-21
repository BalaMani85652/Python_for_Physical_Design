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

print("------ Timing Summary ------")
print("Total Violations :",len(violations))
print("Worst slack:",min(violations.values()))
print("Average slack:",sum(violations.values())/len(violations))
print("----------------------------")

