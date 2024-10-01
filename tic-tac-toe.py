def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
  board = []
  inside_board = []
  str = ' '
  for i in range(n):
    inside_board.append(str)
  for g in range (n):
    board.append(inside_board[0:])
  return board

#done
def get_location(n, game_board):
    row = input(f'Please enter a row index between 0 and {n - 1}: ')
    column = input(f'Please enter a column index between 0 and {n - 1}: ')
    while True:
      if row.isdigit() == False or column.isdigit == False:
        print(f"({row}, {column}) is not a legal input!")
        row = input(f'Please enter a row index between 0 and {n - 1}: ')
        column = input(f'Please enter a column index between 0 and {n - 1}: ')
        continue
      if row.isdigit() == True and column.isdigit() == False:
        print(f"({row}, {column}) is not a legal input!")
        row = input(f'Please enter a row index between 0 and {n - 1}: ')
        column = input(f'Please enter a column index between 0 and {n - 1}: ')
        continue
      else:
        x = int(row)
        y = int(column)
        if int(row) >= n or int(column) >= n: 
          print(f"({row}, {column}) is not a legal space!")
          row = input(f'Please enter a row index between 0 and {n - 1}: ')
          column = input(f'Please enter a column index between 0 and {n - 1}: ')
          continue
        if game_board[x][y] != ' ' :
          print(f'({row}, {column}) is not an available space!')
          row = input(f'Please enter a row index between 0 and {n - 1}: ')
          column = input(f'Please enter a column index between 0 and {n - 1}: ')
          continue
        if game_board[x][y] == ' ' :
          return x,y
# works

def row_win(n, game_board, player):
  for row in game_board:
    win = 0
    for cell in row:
      if cell == player:
        win+= 1
        if win == n:
          return True
      else:
        win = 0
  if win == n:
    return True
  else:
    return False
  

def col_win(n, game_board, player):
  win = 0
  count = 0
  while count < n:
    for spaces in game_board:
      if spaces[count] == player:
        win+= 1
    if win != n:
      win = 0
      count +=1
      continue
    if win == n:
      return True
  if win != n:
    return False
 
  #works

def diag_win(n, game_board, player):
  win = 0
  count = 0
  for spaces in game_board:
    if count == n:
      break
    if spaces[count] == player:
      win+=1
      count+=1
    else:
      count+=1
  if win == n:
    return True
  else:
    return False
  
def anti_diag_win(n, game_board, player):
    for i in range(n):
      if game_board[i][n-1-i] != player:
        return False
      else:
        continue
    return True
        
def has_won(n, game_board, player):
  if row_win(n, game_board, player) == True or col_win(n, game_board, player) == True or diag_win(n, game_board, player) == True or anti_diag_win(n, game_board, player) ==True:
    return True
  else:
    return False

# done
'''
print(col_win(4,       [['O', 'O', 'O', ' '],
                        ['O', 'O', 'X', 'O'],
                        ['O', 'X', 'O', 'O'],
                        ['X', 'O', 'O', 'O']],
                        'O'))
'''

def play_game(n):
  empty = make_empty_board(n)
  print(f'*** Welcome to {n} by {n} Tic-Tac-Toe ***')
  print_board(n, empty)
  print()
  while True:
    tie = 0
    for rows in empty:
      if ' ' not in rows:
        continue
      else:
        tie+=1
    if has_won(n, empty, 'X') == False and has_won(n, empty, 'O') == False and tie == 0:
      print()
      print('Tie!')
      break
    print("* X's turn *")
    x,y = get_location(n, empty)
    empty[x][y] = 'X'
    print_board(n, empty)
    if has_won(n, empty, 'X') == True:
      print()
      print('X wins!')
      break
    tie = 0
    for rows in empty:
      if ' ' not in rows:
        continue
      else:
        tie+=1
    if has_won(n, empty, 'X') == False and has_won(n, empty, 'O') == False and tie == 0:
      print()
      print('Tie!')
      break
    print()
    print(f"* O's turn *")
    a, b = x,y = get_location(n, empty)
    empty[a][b] = 'O'
    print_board(n, empty)
    if has_won(n, empty, 'O') == True:
      print()
      print('O wins!')
      break
    tie = 0
    for rows in empty:
      if ' ' not in rows:
        continue
      else:
        tie+=1
    if has_won(n, empty, 'X') == False and has_won(n, empty, 'O') == False and tie == 0:
      print()
      print('Tie!')
      break
  #loop

play_game(4)
