from tkinter import *
from game_interface.grid_game import canva_creation

def creation_fenetre_comand(): # creation of the command windows
    fenetre=Tk()
    fenetre.title('command interface')
    return fenetre

def button_action(order, canvas, fenetre, game_grid_init, size, dic_grid): # action of bouton
    canvas.destroy() # clear the windows
    game_grid=order(game_grid_init) # new grid given by the game in relation to the order
    canva_creation(game_grid, size, dic_grid,fenetre) # creation of a new graphic grid
    fenetre.mainloop()


def button_creation_for_an_order(fc,order,canvas,fenetre,game_grid_init,size,dic_grid): # implementation of a button
    Boutton=Button(fc, text=order[0],
                   command=lambda order=order[1],canvas=canvas,fenetre=fenetre,game_grid_init=game_grid_init,size=size,dic_grid=dic_grid:
                   button_action(order, canvas, fenetre, game_grid_init, size, dic_grid))
    Boutton.pack()



def creation_interface_comand(d,fenetre,fc,canvas,game_grid_init,size,dic_grid,order):
    L=d.values
    for i in L:
        button_creation_for_an_order(fc,order,canvas,fenetre,game_grid_init,size,dic_grid)
    fc.mainloop()








