path = None
slack = None
timing_violations = 0
TNS = 0																	#TNS = Sum of all negative slack
WNS = 0																	#WNS = Most negative slack
with open("timing.rpt.txt", "r") as f:
	for line in f:
		line =line.strip()												#Remove extra spaces and newline
		
		if line.startswith("Path:"):									#Detecting a line starts with "Path:"
			path =line.split(":")[1].strip()							
		
		elif line.startswith("Slack:"):									#Detecting a line starts with "Slack"
			slack =float(line.split(":")[1].strip())
			#print(slack)
			
			if slack < 0:
				timing_violations += 1
				TNS = TNS + slack
				
				print("VIOLATION",path,"slack=",slack)
				if slack < WNS :
					WNS = slack
	
	
print("\nTotal timing violations=",timing_violations)	
print("Total negative slack=",TNS)
print("Worst negative slack",WNS)

	
'''line.split(":")[1].strip()
   line.split(":") ----> ["Path:", " clk_reg1_to_reg2"]
   [1] ----> " clk_reg1_to_reg2"
   .strip() ----> "clk_reg1_to_reg2"
   
'''
