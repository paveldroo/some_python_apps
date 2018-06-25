def c_to_f(c):
    if c < -273.15:
        pass
    else:
        f = c*9/5+32
        with open('../celcium.txt', 'a+') as myfile:
            myfile.write('{}\n'.format(f))

temperatures = [10, -20, -289, 100]

for item in temperatures:
    c_to_f(item)
