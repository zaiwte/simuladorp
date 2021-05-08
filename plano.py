import pygame as pg
import sys
from pygame.locals import *

class Plano:
      def __init__(self,superficie,ancho,alto):
          self._superficie=superficie

          self._ancho=ancho
          self._alto=alto
          self._negro=(90,90,90)
          self._gris=(190,190,190)

          self.ox=int(self._ancho/2)
          self.oy=int(self._alto/2)

          self.domx=0
          self.domy=0

          self.origen=(self.ox,self.oy)

          self._mover=False

          self.lPuntos_x=[]

          self.dicc={}

          self.vax=0
          self.vay=0

          self.centro=((self.ox+self.vax),(self.oy+self.vay))


      def _rejilla(self,color,distancia,origen,dimen):
          num=0
          G=1
          x=origen[0]
          y=origen[1]

          ancho=dimen[0]
          alto=dimen[1]

          self.dicc={"y":[  (x,  y-alto),  (x,  y+alto)  ],
                     "x":[  (x-ancho, y), (x+ancho, y)   ] }

          for i in self.dicc:

                if i in ["x"]:

                    while True:

                          if (self.dicc[i][0][1]+(num*distancia))>(y+alto):

                              break
                          if num==0:
                              pass
                          else:
                              G=1
                          #lineas que se colocan hacia abajo>               x inicial                    y inicial
                          pg.draw.line(self._superficie,color,(self.dicc[i][0][0] , self.dicc[i][0][1]+(num*distancia)),
                          #                                                                                                             x final                      y final
                                                                      (self.dicc[i][1][0] , self.dicc[i][1][1]+(num*distancia)),G)

                          #lineas que se colocan hacia arriba<              x inicial                                                    y inicial
                          pg.draw.line(self._superficie,color,(self.dicc[i][0][0] , self.dicc[i][0][1]-(num*distancia)),
                          #                                                                                                             x final                      y final
                                                                      (self.dicc[i][1][0] , self.dicc[i][1][1]-(num*distancia)),G)
                          num+=1
                    num=0

                elif i in ["y"]:

                    while True:

                          if (self.dicc[i][0][0]+(num*distancia))>(x+ancho):

                              break
                          if num==0:
                              pass
                          else:
                              G=1


                          #lineas 1 que se colocan hacia la derecha
                          pg.draw.line(self._superficie,color,(self.dicc[i][0][0]+(num*distancia),self.dicc[i][0][1]),
                                                                      (self.dicc[i][1][0]+(num*distancia),self.dicc[i][1][1]),G)

                          #lineas 2 que se colocan hacia la izquierda
                          pg.draw.line(self._superficie,color,(self.dicc[i][0][0]-(num*distancia),self.dicc[i][0][1]),
                                                                      (self.dicc[i][1][0]-(num*distancia),self.dicc[i][1][1]),G)
                          num+=1
                    num=0


      def _rejillas_C(self,origen,dimen):
          x=origen[0]
          y=origen[1]
          ancho=dimen[0]
          alto=dimen[1]

          self._rejilla(self._gris, 10, (x,y), (ancho,alto) )

          self._rejilla(self._negro, 50, (x,y), (ancho,alto) )
          #cada regilla debe tener centro con coordenada para fijar posicion de ellos en la pantalla
          return (x,y)

      def ver_ejes_XY(self):

        miFuente=pg.font.Font(None,23)

        coord={"1":(1,-1),"2":(0,-1),"3":(-1,-1),
               "4":(1,0),"M":(0,0),"6":(-1,0),
               "7":(1,1),"8":(0,1),"9":(-1,1)}

        R=self._rejillas_C( (self.centro[0], self.centro[1]), (self._ancho, self._alto)  )
        o=miFuente.render(str(R),0,(5,100,5))
        self._superficie.blit(o,R)
        """for i in coord:

            R=self._rejillas_C( (self.centro[0]+(coord[i][0]*(self._ancho)), self.centro[1]+(coord[i][1]*(self._alto))), (self._ancho/2, self._alto/2)  )
            #pg.draw.circle(self._superficie,(100,0,0),self.origen,10)


            if i=="M":
                o=miFuente.render(str(R),0,(5,100,5))
                self._superficie.blit(o,R)"""

          #cada regilla debe tener centro con coordenada para fijar posicion de ellos en la pantalla

      def mover(self):

          self._mover=True
          mx,my=pg.mouse.get_pos()
          self.domx=mx-self.ox
          self.domy=my-self.oy

      def parar(self):
          self._mover=False

          #return {"ejeX":[self._pos_Inicial_ejeX,self._pos_Final_ejeX],"ejeY":[self._pos_Inicial_ejeY,self._pos_Final_ejeY]}
      def actualizar(self):
          if self._mover:

                miFuente=pg.font.Font(None,25)
                mx,my=pg.mouse.get_pos()
                self.ox=mx-self.domx
                self.oy=my-self.domy
                self.origen=(self.ox,self.oy)
                self.centro=((self.ox+self.vax), (self.oy+self.vay))


                if (self.centro[0]>(self._ancho)):
                    o2=miFuente.render(str("derecha"),0,(5,100,5))
                    self._superficie.blit(o2,(0,0))
                    self.vax=self.vax-self._ancho
                    pg.draw.circle(self._superficie,(0,150,0),self.centro,15)

                elif (self.centro[0]<0):
                    o2=miFuente.render(str("izquierda"),0,(5,100,5))
                    self._superficie.blit(o2,(0,0))
                    self.vax=self.vax+self._ancho
                    pg.draw.circle(self._superficie,(0,0,150),self.centro,15)

                elif (self.centro[1]>(self._alto)):
                    o2=miFuente.render(str("abajo"),0,(5,100,5))
                    self._superficie.blit(o2,(0,0))
                    self.vay=self.vay-self._alto

                elif (self.centro[1]<0):
                    o2=miFuente.render(str("arriba"),0,(5,100,5))
                    self._superficie.blit(o2,(0,0))
                    self.vay=self.vay+self._alto
                else:
                    pass


                o2=miFuente.render(str(self.origen),0,(5,100,5))
                self._superficie.blit(o2,(0,0))


      def puntero(self):
          mx,my=pg.mouse.get_pos()

          mx=mx-self.ox
          my=self.oy-my

          miFuente=pg.font.Font(None,25)
          #o=miFuente.render(str((self.ox,self.oy)),0,(5,5,5))
          #mxy=miFuente.render(str((mx,my)),0,(5,5,5))

          #self._superficie.blit(o,(0,0))
          #self._superficie.blit(mxy,(150,0))


