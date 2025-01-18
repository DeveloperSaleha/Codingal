import pygame
import random
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision Game")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
player = Player()
enemies = pygame.sprite.Group()
for _ in range(7):
    enemy = Enemy()
    enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)
score = 0
font = pygame.font.Font(None, 36)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.update(keys)
    collided_enemies = pygame.sprite.spritecollide(player, enemies, True)
    if collided_enemies:
        score += 1
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
