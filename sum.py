digits = open("ints.txt").readlines()
d = {}
for x in range(len(digits)):
    d["int{0}".format(x)] = int(digits[x].strip())
D_keys = list(d.keys())
D_values = list(d.values())

result = str((D_values[0]-D_values[1]))
print("sum of "+ str(D_values[0]) +" and " + str(D_values[1]) +" is: " + result)

with open('sum.txt', 'a') as f:
    f.seek(0)
    f.truncate()
    f.write(result)
