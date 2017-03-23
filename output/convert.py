data = open('firstlog.txt').read()
out = open('output.txt','wb')
for d in data:
	# print ord(d)
	out.write(str(ord(d))+" ")