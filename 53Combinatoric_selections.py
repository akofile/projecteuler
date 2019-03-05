
def fac(x):
    return 1 if x==0 else x * fac(x-1)


count=0
for r in range(1,101):
    for n in range(r+1,101):
        print(r,n)
        if fac(n)/(fac(n-r)*fac(r))>=1000000:
            count+=1




print(count)
