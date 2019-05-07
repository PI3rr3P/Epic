from mapEditor import *

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    lab = Labyrinth()
    lab.import_labyrinth()
    lab.build_labyrinth()
    lab.draw()
    # afficher
    pygame.display.flip()
    pygame.key.set_repeat(400, 30)

    done = False
    win = False
    while not done:
        clock.tick(30) # 10 times per sec
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == KEYDOWN:
                win = lab.move(event.key)
        
            lab.draw()
            pygame.display.flip()

            if win:
                lab.screen.fill((255,255,255))
                font = pygame.font.SysFont('Comic Sans MS', 30)
                txt = font.render("You WIN", False, (0,0,0))
                lab.screen.blit(txt, (375, 375))
                pygame.display.flip()

    pygame.quit()