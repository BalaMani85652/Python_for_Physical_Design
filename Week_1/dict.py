'''Dictionaries store relationships:
   Macro ----> Area
   Macro ----> Location
   Macro ---->Fanout
 '''

#Intialising Dictionary
macro_area = {
	"CPU" : 2.5,
	"DSP" :1.8,
	"MEM" :3.2,
	"PLL" :0.6
}

#Acessing
print("CPU Area:",macro_area["CPU"])


#Loop through dictionaries
for macro, area in macro_area.items():
	print(macro,"Area:",area)
