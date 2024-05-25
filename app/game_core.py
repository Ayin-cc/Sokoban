import pygame
import time
import copy

from settings import CLOCK

class GameCore:
    def __init__(self, screen):
        self.screen = screen
        self.game_images = []
        self.player = (0, 0)
        self.obt_des = False
        self.box_obt_des = []
        self.dx = 0
        self.dy = 0
        self.origin_map = [[]]
        self.map = [[]]
        self.target_positions = []
        font_name = pygame.font.match_font('fangsong')
        self.font = pygame.font.Font(font_name, 64) 
        self.small_font = pygame.font.Font(font_name, 42)
        for i in range(1, 7):
            image = pygame.image.load(f"assets/image/{i}.png")
            self.game_images.append(image)

    def setMap(self, map):
        self.origin_map = copy.deepcopy(map)
        self.map = copy.deepcopy(self.origin_map)
        # 将二维列表中所有目标点的位置保存到集合中
        for y in range(15):
            for x in range(15):
                if map[y][x] == '4':
                    self.target_positions.append((x, y))

    def display(self):
        # 清空屏幕
        self.screen.fill((0, 0, 0))

        for i in range(0, 15):
            for j in range(0, 15):
                ele = (int) (self.map[i][j])
                if ele == 5:
                    self.player = (j, i)
                x = 10 + 32 * j
                y = 10 + 32 * i
                self.screen.blit(self.game_images[ele - 1], (x, y))

        pygame.display.flip()

    def isWin(self):
        if len(self.target_positions) == len(self.box_obt_des) and set(self.target_positions) == set(self.box_obt_des):
            shade = pygame.Surface((515, 545))
            shade.fill((0, 0, 0))
            shade.set_alpha(214)
            self.screen.blit(shade, (0, 0))
            con = self.font.render("你赢了!", True, (255, 255, 255))
            text = self.small_font.render("按任意键继续...", True, (255, 255, 255))
            self.screen.blit(con, (250 - con.get_width() // 2, 200 - con.get_height() // 2))
            self.screen.blit(text, (250 - text.get_width() // 2, 270))
            pygame.display.flip()
            while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        self.map = copy.deepcopy(self.origin_map)
                        self.obt_des = False
                        self.box_obt_des.clear()  
                        return "选择地图"
        return None

    # 角色移动
    def move(self):
        x = self.player[0] + self.dx
        y = self.player[1] + self.dy
        if x > 0 and x < 15 and y > 0 and y < 15:  # 可以移动
            if self.map[y][x] == '6' or self.map[y][x] == '4':  # 空白砖块或目标点
                for i in range(1, 32):  # 逐帧渲染移动
                    tx = 10 + 32 * (x - self.dx) + i * self.dx
                    ty = 10 + 32 * (y - self.dy) + i * self.dy
                    if self.obt_des:
                            self.screen.blit(self.game_images[3], (10 + 32 * (x - self.dx), 10 + 32 * (y - self.dy)))
                    else:
                        self.screen.blit(self.game_images[5], (10 + 32 * (x - self.dx), 10 + 32 * (y - self.dy)))
                    self.screen.blit(self.game_images[4], (tx, ty))
                    time.sleep(0.5 / CLOCK)
                    pygame.display.flip()
                # 更新map
                if self.obt_des:
                    self.map[y - self.dy][x - self.dx] = '4'
                    self.obt_des = False
                else:  # 原来的位置变为空白砖块
                    self.map[y - self.dy][x - self.dx] = '6'
                # 是否又重新占据了目标点
                if self.origin_map[y][x] == '4':
                    self.obt_des = True
                self.map[y][x] = '5'
                        
            elif self.map[y][x] == '3':  # 箱子
                # 判断箱子是否可移动
                if (y - 1 <= 0 and y + 1 >= 15) or not (self.map[y + self.dy][x + self.dx] == '4' or self.map[y + self.dy][x + self.dx] == '6'):
                    return None
                for i in range(1, 32):  # 逐帧渲染移动
                    tx = 10 + 32 * (x - self.dx) + i * self.dx
                    ty = 10 + 32 * (y - self.dy) + i * self.dy
                    if self.obt_des:
                            self.screen.blit(self.game_images[3], (10 + 32 * (x - self.dx), 10 + 32 * (y - self.dy)))
                    else:
                        self.screen.blit(self.game_images[5], (10 + 32 * (x - self.dx), 10 + 32 * (y - self.dy)))
                    self.screen.blit(self.game_images[4], (tx, ty))
                    self.screen.blit(self.game_images[2], (tx + 32 * self.dx, ty + 32 * self.dy))
                    time.sleep(0.5 / CLOCK)
                    pygame.display.flip()
                # 更新map
                if self.obt_des:
                    self.map[y - self.dy][x - self.dx] = '4'
                    self.obt_des = False
                else:  # 原来的位置变为空白砖块
                    self.map[y - self.dy][x - self.dx] = '6'
                # 是否又重新占据了目标点
                if (x, y) in self.box_obt_des:
                    self.obt_des = True
                    self.box_obt_des.remove((x, y))
                if self.origin_map[y + 1 * self.dy][x + 1 * self.dx] == '4':
                    self.box_obt_des.append((x + 1 * self.dx, y + 1 * self.dy))
                self.map[y][x] = '5'
                self.map[y + 1 * self.dy][x + 1 * self.dx] = '3'
        # 判断是否结束
        return self.isWin()
        

    # 游戏逻辑
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:  # 上
                self.dx = 0
                self.dy = -1
                return self.move()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # 下
                self.dx = 0
                self.dy = 1
                return self.move()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # 左
                self.dx = -1
                self.dy = 0
                return self.move()       
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # 右
                self.dx = 1
                self.dy = 0
                return self.move()
            if event.key == pygame.K_p:  # 重新开始
                self.map = copy.deepcopy(self.origin_map)
                self.obt_des = False
                self.box_obt_des.clear()  
                return None
            if event.key == pygame.K_m:  # 返回菜单
                self.map = copy.deepcopy(self.origin_map)
                self.obt_des = False
                self.box_obt_des.clear()  
                return "主菜单"
        return None