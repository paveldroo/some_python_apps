myfile = open('fruits.txt')
fruits = myfile.read()
fruits = fruits.splitlines()
for items in fruits:
	print(len(items))
