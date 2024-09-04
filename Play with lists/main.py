L = [4, 5, 1, 2, 9, 7, 10, 8]
print(f"Original List: {L}")
count = 0
for i in L:
  count += i
avg = count/len(L)
print(f"sum = {count}")
print(f"average = {avg}")
L.sort()
print(f"Smallest element is: {L[0]}")
print(f"Largest element is: {L[-1]}")