#Area based Check
macro_area = {
	"CPU" : 2.5,
	"DSP" :1.8,
	"MEM" :3.2,
	"PLL" :0.6
}

for macro,area in macro_area.items():
	if area >= 2.5 :
		print (macro,"is a large macro")
	else:
		print (macro,"is ok")


'''This logic is used to:
    Decide macro grouping
    Create placement constraints '''
