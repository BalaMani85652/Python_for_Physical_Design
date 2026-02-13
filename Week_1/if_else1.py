
macros = ["CPU", "DSP", "MEM", "PLL"]
for macro in macros:
	if macro == "PLL" :
		print (macro,"need isolation")
	else:
		print (macro,"normal placement")
