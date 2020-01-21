import pygame

# Initialize game engine
pygame.init

# Create pygame screen
screen = pygame.display.set_mode((1600, 900))
icon = pygame.image.load('images/Splendor.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Splendor")

background_image = pygame.image.load('images/Tabletop.jpg')
screen.blit(background_image, [0, 0])

# playerImg = pygame.image.load('player.png')
# playerX = 370
# playerY = 480


# def player():
#     screen.blit(playerImg, (playerX, playerY))


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]:
    # if keys[pygame.K_RIGHT]:
    # if keys[pygame.K_UP]:
    # if keys[pygame.K_DOWN]:

    pygame.display.update()

pygame.quit()
