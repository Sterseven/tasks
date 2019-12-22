import sys

filee = sys.argv[1]

list1 = []

with open(filee) as f:
    for line in f:
        list1.append(line)

clist = []

for elem in list1:
    clist.append(elem[:-1])

rep = []

for elem in clist:
    rep.append(elem.replace(":", "."))
    
intone = []
intsec = []

for elem in rep:
    intone.append(float(elem.split(' ')[0]))
    intsec.append(float(elem.split(' ')[1]))

inter = set()
t = []
for x in range(len(intone)):
    r = []
    inter.add(intone[x])
    inter.add(intsec[x])
    r.append(intone[x])
    r.append(intsec[x])
    t.append(r)

inter = list(inter)
inter.sort()


vis = []

d = {}

    

for elem in range(len(inter) - 1):
    vis.append(0)
    for x in range(len(t)):
        if t[x][0] <= inter[elem] < inter[elem + 1] <= t[x][1]:
            vis[elem] += 1
bol = max(vis)


for x in range(len(inter) - 1):
    if bol == vis[x] and (x == 0 or bol != vis[x - 1]):
        show = '{:.2f}'.format(inter[x]).replace('.', ':')
        print(show, end=' ')
        
    if bol != vis[x] and bol == vis[x - 1]:
        show = '{:.2f}'.format(inter[x]).replace('.', ':')
        print(show)
