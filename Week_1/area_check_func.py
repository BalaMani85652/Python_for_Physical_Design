def check_macro_area (macro,area) :							#DEFINITION
	if area > 3.0 :
		print (macro,"is a LARGE macro")
	else :
		print (macro,"is ok")			
		
							
check_macro_area("CPU",2.5)									#CALLING THE FUNCTION
check_macro_area("MEM",3.1)									#CALLING THE FUNCTION
