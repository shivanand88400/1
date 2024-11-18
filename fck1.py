import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shiv@anand12345',
    database='gamedb'
)





#fck2
import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def on_click(row, col):
    global game_over  # Declare game_over as global
    global current_player  # Declare current_player as global
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_win(board, current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
#fck complete





def start_game(username):
    print("Starting Tic-Tac-Toe...")


    #fuck
    root = tk.Tk()
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i, j=j: on_click(i, j))
            buttons[i][j].grid(row=i, column=j)

        root.mainloop()


    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i, j=j: on_click(i, j))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

    # Simplified game result input for demo
    result = input("Did you win? (yes/no): ").strip().lower()
    result = 'win' if result == 'yes' else 'loss'

    cursor.execute("INSERT INTO game_results (username, result) VALUES (%s, %s)", (username, result))
    conn.commit()
    print(f"Game result recorded: {result}")



            
cursor = conn.cursor()
def register_user():
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    try:
        cursor.execute("INSERT INTO users (name, username, phone, password) VALUES (%s, %s, %s, %s)",
                       (name, username, phone, password))
        conn.commit()
        print("Registration successful!")
        player1=input('1.register another player\n2.play game\n3.exit\nChoose the above options..').strip().lower()
        if player1=='1':
            register_user()
        elif player1=='2':
            #abhi kuc krenge iska
            start_game()
            pass
        elif player1=='3':
            exit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
def login_user():
    username = input("Enter First player's username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        start_game(username)
    else:
        print("Invalid username or password.")
        x=input('1.login again\n2.register a player\n3.exit(2)')
        if x=='1':
            login_user()
        elif x=='2':
            register_user()
        else:
            exit()

def main():
    print("Welcome to the Game!")
    choice = input("1. Register\n2. Play Game\nChoose an option: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    else:
        print("Invalid choice Choose again!")
        main()

if __name__ == "__main__":
    main()
import tkinter as tk
from PIL import Image, ImageTk

'''def open_game():
    # Function to handle opening the game
    print("Game started")
    main()  # Call main to handle registration/login flow'''


root = tk.Tk()
root.title("Tic_Tac_Toe...")

# Load the icon
icon_path = "icon.png"
icon = Image.open(icon_path)
icon = ImageTk.PhotoImage(icon)

# Create a button with the icon
button = tk.Button(root, image=icon, command=start_game)
button.pack()

root.mainloop()


#fck
'''board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
'''


