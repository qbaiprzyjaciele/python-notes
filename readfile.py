def load_file(name):
	f = open(name,'r+');
	line_ct = 0
	for line in f:
		print('line%s=%s' % (line_ct,line))
		line_ct += 1

load_file('testfile.txt')





	
