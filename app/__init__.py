import pygame

# 初始化
pygame.init()
# 窗口大小
size = (1280, 720)
screen = pygame.display.set_mode(size)
# 窗口标题
pygame.display.set_caption("My Game")
# 60帧
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000