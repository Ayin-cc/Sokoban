import pygame
import os

from settings import DEFAULT_NUM
from utils import load_map

class MapSelection:
    def __init__(self, screen):
        self.screen = screen
        font_name = pygame.font.match_font('fangsong')
        self.column = 0
        self.map_selected = 0
        self.pack_selecting = True
        self.pack_selected = 0  # 0默认 1自定义 2返回
        self.font = pygame.font.Font(font_name, 24)  # 标题字体
        self.small_font = pygame.font.Font(font_name, 16)  # 选项字体
        # 地图列表
        self.map_num = 0
        self.default_maps = []
        self.default_maps_preview = []
        for i in range(1, DEFAULT_NUM + 1):
            filename = f"maps/level{i}.dat"
            if os.path.exists(filename):
                filename = os.path.basename(filename)
                map = load_map(filename)
                if map != None:
                    self.map_num += 1
                    self.default_maps.append(map)
                    filename = os.path.splitext(filename)[0]
                    try:
                        image = pygame.image.load(f"assets/image/{filename}.png")
                    except FileNotFoundError:
                        # 文件不存在
                        image = pygame.image.load(f"assets/image/none.png")
                    self.default_maps_preview.append(image)
                
        self.diy_nums = 0
        self.diy_maps = []
        self.diy_maps_preview = []
        for filename in os.listdir('maps/'):
            if filename.endswith(".dat") and filename not in [f'level{i}.dat' for i in range(1, 7)]:
                filename = os.path.basename(filename)
                map = load_map(filename)
                if map != None:
                    self.diy_nums += 1
                    self.diy_maps.append(map)
                    filename = os.path.splitext(filename)[0]
                    try:
                        image = pygame.image.load(f"assets/image/{filename}.png")
                    except FileNotFoundError:
                        # 文件不存在
                        image = pygame.image.load(f"assets/image/none.png")
                    self.diy_maps_preview.append(image)

    # 默认地图包
    def display_default_pack(self):
        for i in range(1, self.map_num + 1):
            if i == self.map_selected:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            # 地图图片
            name = self.small_font.render(f"第{i}关", True, color)
            x = 350 - (i % 2) * 150
            y = 155 + (i - 1) // 2 * 155
            self.screen.blit(self.default_maps_preview[i - 1], (164 + ((i - 1) % 2) * 150, 35 + (i - 1) // 2 * 155))
            self.screen.blit(name, (x, y))

    def display(self):
        # 清空屏幕
        self.screen.fill((0, 0, 0))  

        # 地图包
        if self.pack_selected == 0:
            if self.pack_selecting:
                color = (255, 255, 0)
            else:
                color = (0, 255, 255)
        else:
            color = (255, 255, 255)
        default_pack = self.font.render("默认", True, color)
        if self.pack_selected == 1:
            if self.pack_selecting:
                color = (255, 255, 0)
            else:
                color = (0, 255, 255)
        else:
            color = (255, 255, 255)
        back_opt = self.font.render("返回", True, color)
        self.screen.blit(default_pack, (30, 30))
        self.screen.blit(back_opt, (30, 110))

        # 地图列表
        self.display_default_pack()

        pygame.display.flip()
    

    # 处理事件
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:  # 上
                if self.column == 0:  # 切换地图包
                    self.pack_selected = (self.pack_selected + 1) % 2
                else:  # 切换地图
                    if self.map_selected - 2 > 0:
                        self.map_selected = self.map_selected - 2
            elif event.key == pygame.K_DOWN  or event.key == pygame.K_s:  # 下
                if self.column == 0:  # 切换地图包
                    self.pack_selected = (self.pack_selected + 1) % 2
                else:  # 切换地图
                    if self.map_selected + 2 <= self.map_num:
                        self.map_selected = self.map_selected + 2
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:  # 左
                if self.column == 1:
                    self.column = 0
                    self.map_selected = 0
                    self.pack_selecting = True
                elif self.column == 2:
                    self.column = 1
                    self.map_selected -= 1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # 右
                if self.column == 0:
                    self.column = 1
                    self.map_selected = 1
                    self.pack_selecting = False
                elif self.column == 1:
                    self.column = 2
                    if self.map_selected + 1 <= self.map_num:
                        self.map_selected += 1
                    
            elif event.key == pygame.K_RETURN:
                # 选择地图
                if self.map_selected > 0:
                    self.pack_selected = 0
                    return "开始游戏"
                # 返回
                if self.pack_selected == 1 and self.map_selected == 0:
                    return "主菜单"
        return None