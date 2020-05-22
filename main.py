from tkinter import Tk, Button, Label, StringVar, messagebox

play_game =True
turn = 1
p1 = 'X'
p2 = 'O'
moves = 0

def check_win():
    if b1.get() == b2.get() == b3.get():
        return b1.get()
    elif b4.get() == b5.get() == b6.get():
        return b4.get()
    elif b7.get() == b8.get() == b9.get():
        return b7.get()
    elif b1.get() == b4.get() == b7.get():
        return b4.get()
    elif b2.get() == b5.get() == b8.get():
        return b2.get()
    elif b3.get() == b6.get() == b9.get():
        return b3.get()
    elif b1.get() == b5.get() == b9.get():
        return b1.get()
    elif b3.get() == b5.get() == b7.get():
        return b3.get()
    else:
        return None

    
def button_click(b_id):
    global turn, moves
    if turn == 1:
        if b_id == 1:
            b1.set(p1)
        elif b_id == 2:
            b2.set(p1)
        elif b_id == 3:
            b3.set(p1)
        elif b_id == 4:
            b4.set(p1)
        elif b_id == 5:
            b5.set(p1)
        elif b_id == 6:
            b6.set(p1)
        elif b_id == 7:
            b7.set(p1)
        elif b_id == 8:
            b8.set(p1)
        elif b_id == 9:
            b9.set(p1)

        c = check_win()
        if c is not None and c != '':
            messagebox.showinfo("Game Over", f"Player {turn} won the game")
            root.destroy()

        c = None
        turn = 2
        moves += 1
        player_turn.set('Player {} turn'.format(turn))
        insert_var.set(f'Insert "{p2}"')
        
    elif turn == 2:
        if b_id == 1:
            b1.set(p2)
        elif b_id == 2:
            b2.set(p2)
        elif b_id == 3:
            b3.set(p2)
        elif b_id == 4:
            b4.set(p2)
        elif b_id == 5:
            b5.set(p2)
        elif b_id == 6:
            b6.set(p2)
        elif b_id == 7:
            b7.set(p2)
        elif b_id == 8:
            b8.set(p2)
        elif b_id == 9:
            b9.set(p2)

        c = check_win()
        if c is not None and c != '':
            messagebox.showinfo("Game Over", f"Player {turn} won the game")
            root.destroy()
            
        c = None
        turn = 1
        moves += 1
        player_turn.set('Player {} turn'.format(turn))
        insert_var.set(f'Insert "{p1}"')

    elif moves == 9 and c is None:
        messagebox.showinfo("Game Over", "DRAW !!!")
        root.destroy()


root = Tk()
root.title('Tic Tac Toe')
root.maxsize(230,200)
root.minsize(230,200)

b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()
player_turn = StringVar()
player_turn.set(f'Player {turn} turn')
insert_var = StringVar()
insert_var.set(f'Insert "{p1}"')

label_msg = Label(root, text='Click on a button to start', font='arial 15')
label_msg.grid(row=1, column=1, columnspan=3)

button1 = Button(root, textvariable=b1, command=lambda: button_click(1))
button1.grid(row=2,column=1, ipadx=15)

button2 = Button(root, textvariable=b2, command=lambda: button_click(2))
button2.grid(row=2,column=2, ipadx=15)

button3 = Button(root, textvariable=b3, command=lambda: button_click(3))
button3.grid(row=2,column=3, ipadx=15)

button4 = Button(root, textvariable=b4, command=lambda: button_click(4))
button4.grid(row=3,column=1, ipadx=15)

button5 = Button(root, textvariable=b5, command=lambda: button_click(5))
button5.grid(row=3,column=2, ipadx=15)

button6 = Button(root, textvariable=b6, command=lambda: button_click(6))
button6.grid(row=3,column=3, ipadx=15)

button7 = Button(root, textvariable=b7, command=lambda: button_click(7))
button7.grid(row=4,column=1, ipadx=15)

button8 = Button(root, textvariable=b8, command=lambda: button_click(8))
button8.grid(row=4,column=2, ipadx=15)

button9 = Button(root, textvariable=b9, command=lambda: button_click(9))
button9.grid(row=4,column=3, ipadx=15)

player_turn_label = Label(root, textvariable=player_turn, pady=5)
player_turn_label.grid(row=5, column=2)

insert_label = Label(root, textvariable=insert_var, pady=5)
insert_label.grid(row=6, column=2)

root.mainloop()
