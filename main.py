from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("350x350")
win.title('Dicionário de Falsos Cognatos')
win.configure(bg='lightgray')

word_dict = {
    'A': [("Abrigo", "Casaco ou abrigo"),
          ("Aceite", "Óleo de cozinha."), ("Alejar", "Distanciar ou remover."),
          ("Apellido", "Sobrenome; nome da família."), ("Aderezo", "Molho ou tempero"),
          ("Acordarse", "Lembrar ou recordar")],

    'B': [("Balcón", "Sacada (de prédio)"), ("Billón", "Trilhão"),
          ("Borracha", "Bêbada"), ("Brinco", "Pulo"),
          ],

    'C': [("Camelo", "Engano"), ("Cena", "Jantar"),
          ("Chulo", "Bonito, Legal"), ("Crianza", "Criação")]
          }

current_list = []

current_definition = []


def show_definition(event):
    selected_word_index = list.curselection()
    if not selected_word_index:
        return

    word_index = selected_word_index[0]
    definition = current_definition[word_index]
    messagebox.showinfo(current_list[word_index], current_definition[word_index])


def update_listbox():
    list.delete(0, END) 
    for word in current_list:
        list.insert(END, word)

buttons_frame = Frame(background='pink')
buttons_frame.pack(side=TOP)

A_button = Button(buttons_frame, text="A")
A_button.pack(side=LEFT)

B_button = Button(buttons_frame, text="B")
B_button.pack(side=LEFT)

C_button = Button(buttons_frame, text="C")
C_button.pack(side=LEFT)

D_button = Button(buttons_frame, text="D")
D_button.pack(side=LEFT)

E_button = Button(buttons_frame, text="E")
E_button.pack(side=LEFT)

F_button = Button(buttons_frame, text="F")
F_button.pack(side=LEFT)

G_button = Button(buttons_frame, text="G")
G_button.pack(side=LEFT)

H_button = Button(buttons_frame, text="H")
H_button.pack(side=LEFT)

I_button = Button(buttons_frame, text="I")
I_button.pack(side=LEFT)

J_button = Button(buttons_frame, text="J")
J_button.pack(side=LEFT)

K_button = Button(buttons_frame, text="K")
K_button.pack(side=LEFT)

L_button = Button(buttons_frame, text="L")
L_button.pack(side=LEFT)

M_button = Button(buttons_frame, text="M")
M_button.pack(side=LEFT)

N_button = Button(buttons_frame, text="N")
N_button.pack(side=LEFT)

O_button = Button(buttons_frame, text="O")
O_button.pack(side=LEFT)

P_button = Button(buttons_frame, text="P")
P_button.pack(side=LEFT)

Q_button = Button(buttons_frame, text="Q")
Q_button.pack(side=LEFT)

R_button = Button(buttons_frame, text="R")
R_button.pack(side=LEFT)

S_button = Button(buttons_frame, text="S")
S_button.pack(side=LEFT)

T_button = Button(buttons_frame, text="T")
T_button.pack(side=LEFT)

U_button = Button(buttons_frame, text="U")
U_button.pack(side=LEFT)

V_button = Button(buttons_frame, text="V")
V_button.pack(side=LEFT)

W_button = Button(buttons_frame, text="W")
W_button.pack(side=LEFT)

X_button = Button(buttons_frame, text="X")
X_button.pack(side=LEFT)

Y_button = Button(buttons_frame, text="Y")
Y_button.pack(side=LEFT)

Z_button = Button(buttons_frame, text="Z")
Z_button.pack(side=LEFT)

list = Listbox(win, width=50, font=(9), bg="lightblue")
list.pack()

# Bind the show_definition function to the <ButtonRelease-1> event
list.bind("<ButtonRelease-1>", show_definition)

win.mainloop()
