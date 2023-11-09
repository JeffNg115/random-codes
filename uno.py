import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((200,200))

    IsRunning = True

    while IsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IsRunning = False
    
if __name__ == "__main__":
    main()