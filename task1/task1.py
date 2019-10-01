import sys, numpy


numfile = str(sys.argv[1])

list1 = []
with open(numfile) as f:
    for line in f:
        list1.append(int(line))
        


result = []
result.append(numpy.percentile(list1, 90))
result.append(numpy.median(list1))
result.append(numpy.max(list1))
result.append(numpy.min(list1))
result.append(numpy.mean(list1))

if result[2] > 32767 or result[3] < -32768:
    print('Must be [-32768, 32767)')

else:
    for elem in result:
        print('{:0.2f}\n'.format(elem))

    
