import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
space = False
color = (0,0,0)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pygame.display.flip()
        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
        if space: color = (255, 255, 255)
        else: color = (0, 0, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space = not space;
