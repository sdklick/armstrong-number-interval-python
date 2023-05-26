

# armstrong number interval

lownum = int(input("please input lower number : "))
highnum = int(input("please enter high num : "))

for x in range(lownum, highnum+1):
    valadd = 0
    if (x==0 or x==1 or x>9):
     for y in str(x): 
        valmul = 1
        for z in range(len(str(x))):
            valmul *= int(y)
        valadd += valmul
     if valadd==x:
        print(x)

