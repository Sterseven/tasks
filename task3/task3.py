import sys


path = sys.argv[1]


path_file = []

for x in range(5):
    ipath = path + "Cash" + str(x+1) + '.txt'
    path_file.append(ipath)

print(path_file)

list1 = []
for elem in path_file:
    with open(elem) as f:
            for line in f:
                list1.append(float(line))
print(list1)    

    
n = 0
ff = []
    
while n != 16:
    test = []
    for x in range(n, len(list1), 16):
        test.append(list1[x])
    ff.append(sum(test))
    n += 1


print(ff.index(max(ff)) + 1)
                 

     


