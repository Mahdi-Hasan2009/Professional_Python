def OnSquareTime(n):
  iterations = 0
  for i in range(0,n):
    for j in range(0,n):
      print("ম", end=" ")
      iterations+=1
    print(f'When\'n\' is {n} Iterations = {iterations}')
    

OnSquareTime(4)
OnSquareTime(7)
OnSquareTime(5)
OnSquareTime(8)
OnSquareTime(9)

print("\n With every 'n' the taken time equals n^2")
print("O(n^2)")