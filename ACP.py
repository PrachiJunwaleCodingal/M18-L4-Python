#ACP-Binary Conversion(Decimal to binary)

decimal=float(input("enter number:"))

def fun1(n):
  if n > 1:
    fun1(n//2)
  print(int(n%2) , end=" " )


fun1(decimal)
print()
