import pygame as pg
import sys
from pygame.locals import *

class Vector:
	def __init__(self,superficie):
		self.superficie=superficie

		self.punto_iX=""
		self.punto_iY=""
		self.punto_fX=""
		self.punto_fY=""
		
		self.variable1=""
		self.memoria_puntoI=[]
		self.memoria_puntoF=[]

	def inicio_vector(self):
		self.variable1=True
		x,y=pg.mouse.get_pos()
		self.punto_iX,self.punto_iY=x,y

	def final_vector(self):
		self.variable1=False
		x,y=pg.mouse.get_pos()
		self.punto_fX,self.punto_fY=x,y

		var1=(self.punto_iX,self.punto_iY)
		var2=(self.punto_fX,self.punto_fY)

		self.memoria_puntoI.append(var1)
		self.memoria_puntoF.append(var2)

	def dibujar_Vector(self):
	
		if self.variable1==True:
			x,y=pg.mouse.get_pos()

			ala_i=pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(x-10,y+10),1)
			ala_d=pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(x+10,y+10),1)
			pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(x,y),1)

		if self.variable1==False:
			ala_i=pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(self.punto_fX-10,self.punto_fY+10),1)
			ala_d=pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(self.punto_fX+10,self.punto_fY+10),1)
			pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(self.punto_fX,self.punto_fY),1)

	
	def memoria_vector(self):
		n=0
		for i in self.memoria_puntoI:
			pos1=self.memoria_puntoI[n]
			pos2=self.memoria_puntoF[n]
			linea=pg.draw.line(self.superficie,(15,15,15),pos1,pos2,1)
			n=n+1
	"""def borrar_linea(self):
		pass

	def lista_lineas(self):
		pass

	def coordenadas_iniciales(self):
		pass

	def coordenadas_finales(self):
		pass

	def crear_superficie(self):
		pass

	def configurar_coordenadas(self):
		pass"""