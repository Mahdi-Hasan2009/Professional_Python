# Programm to move n disk to tower  of Hanoi

def TowerOfHanoi(n, a, b, c):
  if n == 1:
    print(f"\U0001F449 \033[1mMove disk 1 from rod {a} to rod {b}\033[0m")
    return
  # MOve n-1 disk from a to b
  TowerOfHanoi(n-1, a, c, b)
  print(f"\U0001F449 \033[1mMove disk {n} from rod {a} to rod {b}\033[0m")
  TowerOfHanoi(n-1, c, b, a)
  
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')