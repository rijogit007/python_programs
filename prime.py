number=int(input("enter the number u wanna check prime or not:\n"))


if number==1:
    
    print("it is not a prime number")
    
if number>1:
 
    
 for i in range(2,number):
        
        if number%i==0:
            print("not a prime")
            break
        else:
            
            print("its a prime")    
            
    
        