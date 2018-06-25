myfile = open('text_file.txt', 'a+')
numbers = [1, 2, 3]
for item in numbers:
	myfile.write(str(item) + '\n')
myfile.close()
