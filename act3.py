#Mid numbers Product- 12345= 3*4=12

n = int(input("Enter number : "))
t = n
len1 = 0

while t>0: 
  len1 = len1+1
  t = int(t/10)

if len1>=4: 
  len1 = int(len1/2)
  chk = 0
  while n>0:
    rem = n%10
    if chk==len1: 
      mid1 = rem
    elif chk==(len1-1): 
      mid2 = rem
    n= int(n/10)
    chk = chk+1
  product = mid1*mid2 

  print("Product of Mid digits :",product)

else:
  print("pls enter more than 4-digit number to check")