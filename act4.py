#Strong number
n = int(input("Enter any number: "))
add = 0 
temp = n 

while(temp > 0):
    fact = 1  
    i = 1
    rem = temp % 10
    while(i <= rem):
        fact = fact * i 
        i = i + 1

    add = add + fact
    temp = temp // 10

print("Addition of factorial is:", add)
    
if (add == n):
    print(" Strong Number")
else:
    print(" Not strong number")