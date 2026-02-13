#Function to check timing
def check_slack (path,slack) :
	if slack < 0  :
		print ("TIMING VIOLATION:",path,"slack=",slack)
	else :
		print (path,"meets timing")
		


#Timing dictionary
timing_slack = {
		"clk_reg1_to_reg2" : 0.15,
		"clk_reg3_to_reg4" :-0.32,
		"clk_mem_to_reg"   :-0.08,
		"clk_reg_to_out"   :0.05
}

#Loop and call function
for path,slack in timing_slack.items() :
	check_slack (path,slack)
