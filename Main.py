class Postac(Sprite):
	def __init__(self):
		self.image=17
		self.color=Color(255,192,203)
		self.position.x=-50
		self.position.y=-45
	def update(self):
		global sila
		global grunt1
		global pozycja
		global x2
		global y2
		if self.position.y>-49.5:
			self.position.y-=3
		self.angle=0
		if game.key('left'):
			self.position.x-=1
			self.angle=2
			sila =(pozycja - self.angle)-10
		if game.key('right') and self.position.x<-25:
			self.position.x+=1
			self.angle=-2
			sila =(pozycja - self.angle)+10
		if game.key('up') and grunt1 ==1:
			self.position.y+=20
			grunt1 = 0
		y2 = self.position.y
		x2 = self.position.x
class Siatka(Sprite):
	def __init__(self):
		self.image=63
		self.size=3
		self.position.x=0
		self.position.y=a
		self.color=Color(255,255,255)
	def update(self):
		global atak
		global sila
		global pozycja
		sila =(pozycja - self.angle)+10
		if self.collide(pilka):
			atak = 1
class Ziemia(Sprite):
	def __init__(self):
		self.image=63
		self.size=3
		self.position.x=b
		self.position.y=a
		self.color=Color(153,51,0)
	def update(self):
		global grunt1
		global atak
		global punktyenemy
		if (self.collide(postac)):
			grunt1 = 1
		if (self.collide(pilka)):
				punktyenemy+=1
				pilka.position = Vector(-45,-20)
class Ziemia2(Sprite):
	def __init__(self):
		self.image=63
		self.size=3
		self.position.x=b
		self.position.y=a
		self.color=Color(153,51,0)
	def update(self):
		global grunt2
		global atak
		global punktypostac
		if (self.collide(postac)):
			grunt2 = 1
		if (self.collide(pilka)):
				punktypostac+=1
				pilka.position = Vector(-45,-20)
class Pilka(Sprite):
	def __init__(self):
		self.image=51
		self.size=15
		self.position.x=-30
		self.position.y=-20
		self.color=Color(255,255,204)
	def update(self):
		global dotyk
		global sila
		global pozycja
		global x2
		global y2
		global atak
		global odbiciapostac
		global odbiciaenemy
		global punktyenemy
		global punktypostac
		if dotyk ==1:
			if self.position.y>-68:
				self.position.y-=2
		
		if atak==1:
			if self.position.x<=0:
				if(self.position.y>-45):
					self.position.x-=15
					atak=0
				else:
					self.position.x-=8
					atak=0	
			else:
				if(self.position.y>-45):
					self.position.x+=15
					atak=0
				else:
					self.position.x+=8
					atak=0	
		if self.collide(postac[0]):
			odbiciaenemy = 0
			odbiciapostac += 1
			dotyk = 1
			if odbiciapostac==3:
				punktyenemy+=1
				self.position = Vector(-45,-20)
			self.angle=sila
			if(self.position.y>-25):
				self.position.y+=45
				if((x2-self.position.x)<-10):
					for i in range(4):
						self.position.x-=25
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x+=25
			elif(self.position.y>-45):
				self.position.y+=30
				if((x2-self.position.x)<-10):
					for i in range(4):
						self.position.x-=15
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x+=15
			else:
				self.position.y+=5
				if((x2-self.position.x)<-10):
					for i in range(4):
						self.position.x-=1
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x+=1
		pozycja	= self.angle
		if self.collide(postac[1]):
			odbiciapostac = 0
			odbiciaenemy += 1
			if odbiciaenemy==3:
				punktypostac+=1
				self.position = Vector(45,-20)
			dotyk = 1
			self.angle=sila
			if(self.position.y>-25):
				self.position.y+=45
				if((x2-self.position.x)<0):
					for i in range(4):
						self.position.x+=25
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x-=25
			elif(self.position.y>-45):
				self.position.y+=30
				if((x2-self.position.x)<0):
					for i in range(4):
						self.position.x+=15
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x-=15
			else:
				self.position.y+=5
				if((x2-self.position.x)<0):
					for i in range(4):
						self.position.x+=1
				elif((x2-self.position.x)>0):
					for i in range(4):
						self.position.x-=1
		pozycja	= self.angle
class Enemy(Sprite):
	def __init__(self):
		self.image=17
		self.color=Color(51,255,153)
		self.position.x=50
		self.position.y=-45
	def update(self):
		global sila
		global grunt2
		global pozycja
		global x2
		global y2
		if self.position.y>-49.5:
			self.position.y-=3
		self.angle=0
		if game.key('a')and self.position.x>23:
			self.position.x-=2
			self.angle=1
			sila =(pozycja - self.angle)-10
		if game.key('d'):
			self.position.x+=2
			self.angle=-1
			sila =(pozycja - self.angle)+10
		if game.key('w') and grunt2 ==1:
			self.position.y+=20
			grunt2 = 0
		y2 = (self.position.y)*-1
		x2 = (self.position.x)+-1
class licznik1(Sprite):
	def __init__(self):
		self.image=94
		self.size=12
		self.color=Color(255,0,51)
		self.position.x=-70
		self.position.y=80
	def update(self):
		global punktypostac
		if punktypostac==1:
			self.image=95
		if punktypostac==2:
			self.image=96
		if punktypostac==3:
			self.image=97
		if punktypostac==4:
			self.image=98
		if punktypostac==5:
			self.image=99
		if punktypostac==6:
			self.image=100
		if punktypostac==7:
			self.image=101
		if punktypostac==8:
			self.image=102
		if punktypostac==9:
			self.image=103
		if punktypostac==10:
			message.show("Player 1 WINS")
			game.stop()
class licznik2(Sprite):
	def __init__(self):
		self.image=94
		self.size=12
		self.color=Color(255,0,51)
		self.position.x=70
		self.position.y=80
	def update(self):
		global punktyenemy
		if punktyenemy==1:
			self.image=95
		if punktyenemy==2:
			self.image=96
		if punktyenemy==3:
			self.image=97
		if punktyenemy==4:
			self.image=98
		if punktyenemy==5:
			self.image=99
		if punktyenemy==6:
			self.image=100
		if punktyenemy==7:
			self.image=101
		if punktyenemy==8:
			self.image=102
		if punktyenemy==9:
			self.image=103
		if punktyenemy==10:
			message.show("Player 2 WINS")
			game.stop()

				
global a
global b
global grunt1
global grunt2
global dotyk
global pozycja
global y2
global x2
global atak
global odbiciapostac
global odbiciaenemy
global punktyenemy
global punktypostac
faul = message.show('Siatkowka: gra dla dwoch osob: Aby wygrac trzeba zdobyc 10 punktow, za kazdym razem kiedy obijesz 3 razy pilke lub pilka spadnie na twoja polowe tracisz punkt. Powodzenia.' '\n''Player1:' '\n''strzalka w gore: skok''\n''strzalka w prawo: ruch w prawo ''\n''strzalka w lewo: ruch w lewo''\n''Player2:''\n' 'w: skok''\n''d: ruch w prawo ''\n''a: ruch w lewo')
odbiciaenemy = 0
odbiciapostac = 0
punktypostac = 0
punktyenemy = 0
atak=0
pozycja = 0
a = 0
b = 0
siatka = []
ziemia = []
postac = []
grunt1 = 1
grunt2 = 1
dotyk = 0
sila = 0
game.add(licznik1())
game.add(licznik2())
game.background=Color(0,0,0)
for i in range(19):
	siatka.append(Siatka())
	game.add(Siatka())
	a=a-4
b = -100
for i in range(26):
	ziemia.append(Ziemia())
	game.add(Ziemia())
	b=b+4
for i in range(25):
	ziemia.append(Ziemia2())
	game.add(Ziemia2())
	b=b+4
postac.append(Postac())
postac.append(Enemy())
game.add(postac[0])
game.add(postac[1])
pilka = Pilka()
game.add(pilka)
game.start()
