macro_coordinates = {
		"CPU" : (200,300),
		"DSP" : (1200,400),
		"MEM" : (500,600)

}
for macro,(x,y) in macro_coordinates.items() :
	if x > 800 :
		print (macro,"is placed near the boundary")



path_slack = {
		"path1" : 1.2,
		"path2" : 2.5,
		"path3" : -0.9,
		"path4" : 3.1,
		"path5" : -2.1
}
for path ,slack in path_slack.items() :
	if slack < 0 :
		print (path,"is violated")
