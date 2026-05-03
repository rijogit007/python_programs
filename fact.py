

def fact(num):
    facorial=1
    for i in range(1,num+1):
        facorial*=i
        
    print(facorial)
    
num=int(input("enter the number"))

fact(num)
    
    