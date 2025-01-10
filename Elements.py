import pygame
pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")
background_color = (255, 255, 255)
rectangle_color = (0, 0, 255) 
rectangle_size = (200, 100) 
rectangle_position = (
    (window_size[0] - rectangle_size[0]) // 2, 
    (window_size[1] - rectangle_size[1]) // 2,  
)
font = pygame.font.Font(None, 36) 
text = font.render("Hello!", True, (0, 0, 0)) 
text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 + 70))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    pygame.draw.rect(screen, rectangle_color, (*rectangle_position, *rectangle_size))
    screen.blit(text, text_rect)
    pygame.display.flip()
pygame.quit()
