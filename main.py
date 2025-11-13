import pygame
from environment import Environment
from robot import Robot
from package import Package
from gui import GUI

def main():
    env = Environment(width=7, height=7)
    robots = [Robot("robot1", position=(0, 0))]
    packages = [
        Package("pkg1", (2, 2), (5, 5)),
        Package("pkg2", (1, 3), (6, 1)),
        Package("pkg3", (3, 5), (0, 6)),
        Package("pkg4", (5, 2), (2, 1)),
    ]

    gui = GUI(env, robots, packages)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                r = robots[0]
                if event.key == pygame.K_UP:
                    r.move("up")
                elif event.key == pygame.K_DOWN:
                    r.move("down")
                elif event.key == pygame.K_LEFT:
                    r.move("left")
                elif event.key == pygame.K_RIGHT:
                    r.move("right")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gui.handle_click(event.pos)


        gui.draw()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()
