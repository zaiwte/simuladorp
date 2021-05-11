import pygame as pg
import sys
from pygame.locals import *

class Linea:
	def __init__(self,superficie,mouseg=None):
		self.superficie=superficie
		self.punto_iX=0
		self.punto_iY=0
		self.punto_fX=0
		self.punto_fY=0
		self.variable1=0
		self.dicc_lineas={}
		self.lista_lineas=[]
		self.nlineas=0
		self.__mover=False
		self.dicc_dops={}

	def inicio_linea(self):
		self.variable1=True
		x,y=pg.mouse.get_pos()
		self.punto_iX,self.punto_iY=x,y

	def final_linea(self):
		self.variable1=False
		self.nlineas += 1
		x,y=pg.mouse.get_pos()
		self.punto_fX,self.punto_fY=x,y
		pi=(self.punto_iX, self.punto_iY)
		pf=(self.punto_fX, self.punto_fY)
		self.lista_lineas.append(self.nlineas)
		self.dicc_lineas[self.nlineas]={"pi":pi,"pf":pf}

	def dibujar_linea(self):
	
		if self.variable1==True:
			x,y=pg.mouse.get_pos()
			pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(x,y),1)

		if self.variable1==False:
			pg.draw.line(self.superficie,(15,15,15),(self.punto_iX,self.punto_iY),(self.punto_fX,self.punto_fY),1)		

	def memoria_lineas(self):
		for i in self.lista_lineas:
			pi = self.dicc_lineas[i]["pi"]
			pf = self.dicc_lineas[i]["pf"]
			linea=pg.draw.line(self.superficie,(15,15,155),pi,pf,1)

	def actualizar_lineas(self,origen):
		if self.__mover:
			ox,oy = origen
			for i in self.lista_lineas:
				pix, piy = self.dicc_lineas[i]["pi"]
				pfx, pfy = self.dicc_lineas[i]["pf"]
				dopix, dopiy = self.dicc_dops[i]["dopi"]
				dopfx, dopfy = self.dicc_dops[i]["dopf"]
				pix,piy = (ox - dopix,oy - dopiy)
				pfx,pfy = (ox - dopfx,oy - dopfy)
				pi = (pix,piy)
				pf = (pfx,pfy)
				self.dicc_lineas[i] = {"pi": pi, "pf": pf}
				linea = pg.draw.line(self.superficie, (15, 15, 155), pi, pf, 1)

	def mover_lineas(self,origen):
		self.__mover=True
		ox,oy = origen
		for i in self.lista_lineas:
			pix, piy = self.dicc_lineas[i]["pi"]
			pfx, pfy = self.dicc_lineas[i]["pf"]

			dopix,dopiy = ox - pix,oy - piy  # distancia entre el origen y el punto inicial en x , y
			dopfx,dopfy = ox - pfx,oy - pfy  # distancia entre el origen y el punto final en x
			dopi = (dopix,dopiy)
			dopf = (dopfx,dopfy)
			self.dicc_dops[i] = {"dopi":dopi,"dopf":dopf}
			self.punto_iX = 0
			self.punto_iY = 0
			self.punto_fX = 0
			self.punto_fY = 0
			#falta guardar las distandias en una lista

	def parar(self):
		self.__mover = False

	def borrar_linea(self):
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
		pass	