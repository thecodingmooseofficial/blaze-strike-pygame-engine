import pygame
pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 650

myScreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blaze Strike!')

# Set FrameRate
clock = pygame.time.Clock()
FPS = 80

# Player Action Variables
GoLeft = False
GoRight = False
GoUp = False
GoDown = False

background_image = pygame.image.load('Images/Warzone.jpeg')
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, playerspeed):
        pygame.sprite.Sprite.__init__(self)
        self.playerspeed = playerspeed
        self.direction = 1
        self.flip = False
        SoldierImage = pygame.image.load('Images/Soldier.png')
        self.SoldierImage = pygame.transform.scale(SoldierImage, (int(SoldierImage.get_width()*scale), int(SoldierImage.get_height()*scale)))
        self.rect = self.SoldierImage.get_rect()
        self.rect.center = (x, y)

    def MoveSoldier(self, GoLeft, GoRight):
        # Reset Movement Variables
        dx = 0
        dy = 0

        # Assign movement variables if moving left or right
        if GoLeft:
            dx = -self.playerspeed
            self.flip = True
            self.direction = -1
        if GoRight:
            dx = self.playerspeed
            self.flip = False
            self.direction = 1

        # Update Rectangle Position
        self.rect.x += dx
        self.rect.y += dy       
            
    def DisplaySoldier(self):
        myScreen.blit(pygame.transform.flip(self.SoldierImage, self.flip, False), self.rect)

player1 = Soldier(200, 525, 0.15, 5)           

RunWindow = True
while RunWindow:
    clock.tick(FPS)    
    myScreen.blit(background_image, (0, 0))
    player1.DisplaySoldier()
    player1.MoveSoldier(GoLeft, GoRight)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunWindow = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                GoLeft = True
            if event.key == pygame.K_RIGHT:
                GoRight = True
            if event.key == pygame.K_ESCAPE:
                RunWindow = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                GoLeft = False
            if event.key == pygame.K_RIGHT:
                GoRight = False

    pygame.display.update()

pygame.quit()
