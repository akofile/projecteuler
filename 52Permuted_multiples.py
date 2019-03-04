import time

def prov(str1,str2,boolean):

    for simvol in str2:

        if str1.find(simvol)>=0:
            boolean=True


        else:
            boolean=False
            break
    return boolean

str1=125873
check=False
while not check:
    str1+=1
    count =  0
    check=prov(str(str1),str(str1*2),check)
    if check: count+=1
    check=prov(str(str1),str(str1*3),check)
    if check: count+=1
    check=prov(str(str1),str(str1*4),check)
    if check: count+=1
    check=prov(str(str1),str(str1*5),check)
    if check: count+=1
    check=prov(str(str1),str(str1*6),check)
    if check: count+=1

    check=prov(str(str1*2),str(str1),check)
    if check: count+=1
    check=prov(str(str1*3),str(str1),check)
    if check: count+=1
    check=prov(str(str1*4),str(str1),check)
    if check: count+=1
    check=prov(str(str1*5),str(str1),check)
    if check: count+=1
    check=prov(str(str1*6),str(str1),check)
    if check: count+=1
    if count==10: check=True
    else:check=False



str1=int(str1)


print (str1,str1*2,str1*3,str1*4,str1*5,str1*6)
