theBoard = {'7': ' ', '8': ' ', '9': ' ',
  '4': ' ', '5': ' ', '6': ' ',
  '1': ' ', '2': ' ', '3': ''
}

board_key = []

for key in theBoard:
  board_key.append(key)
  
def printBoard(board):
  print(board['7' + '|' + '8' + '|' + '9' + '|'])
  print('-+-+-')
  print(board['4' + '|' + '5' + '|' + '6' + '|'])
  print('-+-+-')
  print(board['1' + '|' + '2' + '|' + '3' + '|'])
  
def game():
  turn = 'X'
  count = 0
  for i in range(10):
    printBoard(theBoard)
    print(f"It's your turn, {turn}. Move to which place?")
    move = input()
    if theBoard[move] == ' ':
      theBoard[move] = turn
      count += 1
    else:
      print("The place is already filled.\n Move to which place?")
      continue
    if count >= 5:
      if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
        printBoard(theBoard)
        print("\nGame Over\n")
        print("**** "+turn+ " won.****")
        break
      elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
    if count == 9:
      print("\nGame Over\n")
      print("It's a Tie!!")