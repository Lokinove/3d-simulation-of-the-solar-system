from p5 import *

def setup():
	createCanvas(800, 800,WEBGL)
	global rotatey
	rotatey=90	
	loadImage('solar textures/2k_sun.jpg','Sun')
	loadImage('solar textures/2k_jupiter.jpg','jupiter')
	loadImage('solar textures/2k_earth_daymap.jpg','earth')
	loadImage('solar textures/2k_mars.jpg','mars')
	loadImage('solar textures/2k_mercury.jpg','mercury')
	loadImage('solar textures/2k_neptune.jpg','neptune')
	loadImage('solar textures/2k_stars.jpg','stars')
	loadImage('solar textures/2k_uranus.jpg','uranus')
	loadImage('solar textures/2k_moon.jpg','moon')
	loadImage('solar textures/2k_venus_surface.jpg','venus')
	loadImage('solar textures/2k_saturn.jpg','saturn')
	
def draw():
	global rotatey
	background('black')
	#drawTickAxes()
	orbitControl()
	# sphere(radius,detailX,detailY)
	scale(0.7)
	texture(assets['stars'])
	sphere(9999,50,50)

	texture(assets['Sun']),
	#text(sun)
	#fill('orange')
	rotatey+=2
	sphere(150,25,25)

	 #mercury
	push()
	texture(assets['mercury'])
	rotateY(rotatey)	
	translate(200,0,100)
	sphere(30,25,25)
	pop()

	# venus
	push()
	texture(assets['venus'])
	rotateY(rotatey/3)	
	translate(400,0,100)
	sphere(50,25,25)
	pop()

	# earth
	push()
	texture(assets['earth'])
	rotateY(rotatey/4)	
	translate(600,0,100)
	rotateY(rotatey)	
	sphere(55,25,25)
	
	#moon
	sphere(50,25,25)
	translate(100,0,100)
	texture(assets['moon'])
	sphere(30,25,25)
	pop()

	# mars
	push()
	texture(assets['mars'])
	rotateY(rotatey/8)	
	translate(800,0,100)
	sphere(35,25,25)
	pop()

	# jupiter
	push()
	texture(assets['jupiter'])
	rotateY(rotatey/12)	
	translate(1000,0,100)
	sphere(95,25,25)
	pop()
	
	# saturn
	push()
	texture(assets['saturn'])
	rotateY(rotatey/16)	
	translate(1200,0,100)
	sphere(65,25,25)
	pop()

	# uranus
	push()
	texture(assets['uranus'])
	rotateY(rotatey/5)	
	translate(1400,0,100)
	sphere(75,25,25)
	pop()

	# neptune
	push()
	texture(assets['neptune'])
	rotateY(rotatey*2/3)	
	translate(1800,0,100)
	sphere(85,25,25)
	pop()
