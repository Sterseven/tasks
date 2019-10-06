import sys, time


numfile = str(sys.argv[1])


list1 = []
with open(numfile) as f:
    for line in f:
        list1.append(line[:-1])


if len(list1) > 0:
    clear= []        
    for elem in list1:
        clear.append(elem.replace(":", ""))

    num = []
    for elem in clear:    
        num.append(elem.split(' '))
    
    last = []
    for elem in num:
        tmin = []
        for e in elem:
            if len(e) == 3:
                tmin.append(int(e[0])*60 + int(e[1])*10 + int(e[2]))
            if len(e) == 4:
                tmin.append(int(e[0:2])*60 + int(e[2])*10 + int(e[3]))
        last.append(tmin)        

    n = 480
    pmin = []

    while n != 1200:
        tf = []
    
        for elem in last:
            if n >= elem[0] and n < elem[1]:
                tf.append("true")
            else:
                tf.append("false")
            
        pmin.append(tf.count("true"))
        n += 1
                        
    inmaxtf = [i for i, j in enumerate(pmin) if j == max(pmin)] #индексы наибольшего числа посетителей в банке

    spi = []
    dt1 = 480 + inmaxtf[0]
    dt2 = dt1//60
    
    if dt1 - dt2 > 0:
        spi.append((str(dt2) + ':' + str(inmaxtf[0])))
    else:
        spi.append((str(dt2) + ':' + "00"))

    one = 1
    nnn = 0
    tfn = []
    while one != len(inmaxtf):
        if inmaxtf[one] - inmaxtf[nnn] == 1:
            None
        else:
            tfn.append(nnn)
        one +=1
        nnn += 1
    
           
    if len(tfn) == 0 and max(pmin) == 0:
        print ("No visitors")


    if len(tfn) == 0:
        print(list1[0] + "\n")
       
       
    raz = []
           
    for x in range(len(inmaxtf)):
        if x in tfn:
            
            raz.append(inmaxtf[0:x + 1])

    raz.append(inmaxtf)

    
    raz2 = []

    raz2.append(inmaxtf)

    for elem in tfn:
        raz2.append(inmaxtf[elem + 1:])


    inte = []
    for x in range(len(raz)):
        
        interv = []        
        interv.append(time.strftime('%H:%M:%S', time.gmtime((raz2[x][0] + 480)*60)))
        interv.append(time.strftime('%H:%M:%S', time.gmtime((raz[x][-1] + 480 + 1)*60)))
        inte.append(interv)
        

    nar = []
    
    for x in range(len(inte)):
        na = []
        na.append(inte[x][0][:-3])
        na.append(inte[x][1][:-3])
        nar.append(na)

    ex = []

    for x in range(len(nar)):
        sf = []
        for elem in nar[x]:
            
            if elem[0] == '0':
                sf.append(elem[1:])
                

            else:
                sf.append(elem)

            
        ex.append(sf)
        
    for x in range(len(ex)):
        print(ex[x][0] + ' ' + ex[x][1] + '\n')
         
    
else:
    print ("No visitors")
