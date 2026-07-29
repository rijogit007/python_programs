number=int(input("enter the number u wanna check prime or not:\n"))


if number==1:
    
    print("it is not a prime number")
    
if number>1:
 
    
 for i in range(2,number):  #23458
        
        if number%i==0:
            print(i,"not a prime")
            # break
        else:
            
            print(i,"its a prime")    
            
    
        