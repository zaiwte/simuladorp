import pygame as pg
import sys,random,time
import os
from pygame.locals import *
import PySimpleGUI as sg
import linea
import punto
import vector
import plano


class Subc:
    def __init__(self,val=None):

        self.func=val

    def get(self):
        return self.func

    def set(self,val):
        self.func=val

def main():
    buttons_name=['mouse','linea', 'punto', 'vector', 'circulo','arco']

    button_act="ninguno"


    layout=[[sg.Button('mouse'),sg.Button('linea'),sg.Button('punto'),sg.Button('vector'),sg.Button('circulo'),sg.Button('arco')],
            [sg.Graph((1100,500),(0,0),(200,200),background_color="black",key='-GRAPH-')]
            ]

    window=sg.Window('simulador',layout,finalize=True)


    graph = window['-GRAPH-']
    embed = graph.TKCanvas
    os.environ['SDL_WINDOWID']=str(embed.winfo_id())

    pg.init()
    #pg.display.init()
    screen=pg.display.set_mode((1100,500))
    screen.fill((255,255,255))
    pg.display.update()

    plano_XY=plano.Plano(screen,1100,500)
    linea1=linea.Linea(screen)
    punto1=punto.Punto(screen)
    vector1=vector.Vector(screen)


    while True:

        event,value=window.read(timeout=10)

        if event==sg.WIN_CLOSED:
            break

        """if button_act==(event,True):
            window[event].update(button_color=sg.theme_button_color())
            button_act='mouse'"""

        if event in buttons_name:
            for k in buttons_name:
                window[k].update(button_color=sg.theme_button_color())
            window[event].update(button_color=('white','red'))
            button_act=event


        #print(event)

        for evento in pg.event.get():
            if evento.type == QUIT:
                pass

            elif evento.type==MOUSEBUTTONDOWN:
                if evento.button==1:

                    if button_act=='linea':
                        linea1.inicio_linea()

                    elif button_act=='punto':
                        punto1.crear_punto()

                    elif button_act=='vector':
                        vector1.inicio_vector()

                    elif button_act=='mouse':
                        plano_XY.mover()

                        """print(plano_XY.mover(x,y))"""

            elif evento.type==MOUSEBUTTONUP:
                if evento.button==1:

                    if button_act=='linea':
                        linea1.final_linea()

                    elif button_act=='vector':
                        vector1.final_vector()

                    elif button_act=='mouse':
                        plano_XY.parar()

        screen.fill((225,255,255))
        #plano_XY.ver_ejes_XY()

        #pg.draw.circle(screen,(0,0,0),plano_XY.origen,10)

        if button_act=='linea':
            linea1.dibujar_linea()

        elif button_act=='punto':
            punto1.dibujar_punto()

        elif button_act=='vector':
            vector1.dibujar_Vector()

        elif button_act=='mouse':
            plano_XY.actualizar()


        """miFuente=pg.font.Font(None,25)
        origen=miFuente.render(str(plano_XY.origen),0,(5,5,5))
        screen.blit(origen,(0,0))"""

        plano_XY.puntero()

        linea1.memoria_linea()
        punto1.memoria_puntos()

        pg.display.update()




    pg.quit()
    window.close()

main()


