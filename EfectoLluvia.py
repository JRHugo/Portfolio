import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(-20, 0)
        self.size = random.randint(2, 5)
        self.speed = random.randint(5, 10)

    def fall(self):
        self.y += self.speed
        if self.y > 400:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, 400)

raindrops = [Raindrop() for _ in range(100)]

running = True
while running:
    screen.fill((0, 0, 0))  # Fondo negro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for raindrop in raindrops:
        raindrop.fall()
        pygame.draw.circle(screen, (0, 0, 255), (raindrop.x, raindrop.y), raindrop.size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
