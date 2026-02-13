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

#Sorting the violations
sorted_violations = sorted(
						violations.items(),						    
						key=lambda x: x[1] 								#Expected output : [('clk_mem_to_reg', -0.35), ('clk_reg3_to_reg4', -0.08)]
						)


print("\nWorst timing paths:")

for path,slack in sorted_violations:
	print(path, ":",slack)

#Worst path
worst_path = sorted_violations[0]
print("\nWorst path:",worst_path)


'''sorted(violations.items(),key=lambda x: x[1] 
	violations.items() "Covert dictionary into list of pairs"------->[
																		("clk_reg3_to_reg4", -0.35),
																		("clk_mem_to_reg4", -0.08)
	"Python needs to know what to sort by"																]
    key=lambda x:x[1] 
    Here x =("clk_reg3_to_reg4", -0.35)
    So
    x[0] → path
    x[1] → slack


'''
