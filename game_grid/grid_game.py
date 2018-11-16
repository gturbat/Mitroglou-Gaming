from tkinter import *

def place_image(lien_image, coordonnees, canvas):
    photo=PhotoImage(file=lien_image)
    canvas.create_image(coordonnees[1], coordonnees[2], image=photo)

def create_fenetre_jeu():
    fenetre=Tk()
    fenetre.title('Game Interface')
    return fenetre


def canva_creation(game_grid, size, dic_grid,fenetre):
    n=len(game_grid)
    w= size[0] * n # width of the windows
    h= size[1] * n # height of the windows
    new_grid=Canvas(fenetre,width=w,height=h)
    for i in range(0,n):
        for j in range(0,n):
            lien_image=dic_grid[game_grid[i, j]] # get the file of the image
            coordone=[j * size[0] / 2, i * size[0] / 2] # coordones of the image
            place_image(lien_image,coordone,new_grid) # placement of the image
    new_grid.pack()



