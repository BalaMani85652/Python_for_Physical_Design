macros = ["CPU", "DSP", "MEM", "PLL"]
macros_locations = {
		"CPU" : (10,30),
		"DSP" : (40,80),
		"MEM" : (100,140),
		"PLL" : (150,160)
}
for m in macros :
	print (m,"is located",macros_locations[m])


#Calculating total macro area

total_area = 0
macro_area = {
	"CPU" : 2.5,
	"DSP" :1.8,
	"MEM" :3.2,
	"PLL" :0.6
}
for area in macro_area.values():
	total_area = total_area + area
	
print ("Total macro area:",total_area)
