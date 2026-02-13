# Assume die size = 1000 x 1000

die_width = 1000
die_height = 1000

macros_locations = {
		"CPU" : (100,300),
		"DSP" : (400,800),
		"MEM" : (1100,1400),
		"PLL" : (150,160)
}

for macro, (x,y) in macros_locations.items() :
	if x > die_width or y > die_height :
		print (macro,"macro is placed outside the die")
	else :
		print (macro,"placement ok")
