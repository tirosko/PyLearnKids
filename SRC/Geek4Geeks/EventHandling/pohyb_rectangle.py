import pygame
pygame.init()
w, h = 600, 200  # size
s = pygame.display.set_mode((w, h))
c_white, c_blue = (255, 255, 255), (0, 0, 255)  # colors
x, y, rw, rh, spd = 0, 50, 60, 40, 5  # rect params
clk = pygame.time.Clock()  # clock

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    s.fill(c_white)
    pygame.draw.rect(s, c_blue, (x, y, rw, rh))
    x = (x + spd) % (w + rw) - rw
    pygame.display.flip()
    clk.tick(30)

pygame.quit()
