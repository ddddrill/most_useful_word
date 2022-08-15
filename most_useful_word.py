'''ПРОГРАММА ВЫЧИСЛЯЕТ НАИБОЛЕЕ ВСТРЕЧАЮЩЕСЯ СЛОВО В ТЕКСТЕ '''
file=open('C:\\Users\\Aleksandr\\Desktop\\python26\\dataset_3363_3.txt','r')
d={}
a=[]
for line in file:
    from typing import Counter
    u=line.lower().split()
    a+=u
    
    cort=Counter(a)
    num=[]
    for i in cort:
        num.append(cort[i])
    maximus=max(num)
    for i in cort:
        if cort[i]==maximus:
            #print (i,cort[i])
            M=i
            m=str(cort [i])
            current=M+' '+m 
print (current)            
stringg=''.join(current)
    
file.close()

ouf=open('C:\\Users\\Aleksandr\\Desktop\\python26\\dataset_3363_3.txt','w')
ouf.write(stringg)
ouf.close()


