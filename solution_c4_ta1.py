import pygame,math

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
player_image = pygame.image.load("s4.png").convert_alpha()

player=pygame.Rect(200,200,30,30)

WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
xvel=2
yvel=3
angle=0
change=0

# Creating a variable 'distance' and assigning value '5' to it
distance=5
# Creating a variable 'forward' and assigning 'False' to it
forward=False

# Defining a function 'newxy()' to calculate new x,y coordinates
# New x,y coordinates are based on old x,y coordinates, angle, distance 
def newxy(oldx,oldy,distance,angle):
  angle=math.radians(angle+90)
  nx=oldx+(distance*math.cos(angle))
  return nx

while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          change = 6
       if event.key ==pygame.K_RIGHT:
        change = -6 
       # Checking if UP arrow key is pressed and make 'forward' to True
       if event.key == pygame.K_UP:
        forward = True
        
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
          change = 0
      # Checking if UP arrow key is released and make 'forward' to False
      if event.key == pygame.K_UP:
        forward = False 
      
  
  enemy.x=enemy.x + xvel
  enemy.y=enemy.y + yvel 
  
  if enemy.x < -250 or enemy.x > 650 :
    xvel = -1*xvel
  
  if enemy.y < -250 or enemy.y > 850:  
    yvel = -1*yvel
    
  # Checking if 'forward' is 'True' 
  if forward:
      # Finding new x-coordinate by calling the 'newxy()' function
      player.x=newxy(player.x, player.y, distance, angle)  
      
  angle = angle + change
  newimage=pygame.transform.rotate(player_image,angle) 
  screen.blit(newimage ,player)
  
  pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  clock.tick(30)
  
