import pygame

'''
    游戏开始菜单
    0. 开始新游戏
    1. 选择地图
    2. 设置
    3. 关于
    4. 退出
'''
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.menu_options = ["开始新游戏", "选择地图", "选项", "游戏介绍", "退出游戏"]
        self.selected_option = 0
        font_name = pygame.font.match_font('fangsong')
        self.font = pygame.font.Font(font_name, 74)
        self.small_font = pygame.font.Font(font_name, 50)
        self.title_text = self.font.render("推箱子", True, (255, 255, 255))

    # 显示
    def display_menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, (800 // 2 - self.title_text.get_width()//2, 100))
        # 加载菜单图标
        menu_images = []
        for i in range(5):
            image = pygame.image.load(f"assets/image/menu{i}.png")
            menu_images.append(image)

        # 渲染菜单
        for index, option in enumerate(self.menu_options):
            if index == self.selected_option:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            option_text = self.small_font.render(option, True, color)
            self.screen.blit(menu_images[index], (600 // 2 - 40, 260 + index * 60))
            self.screen.blit(option_text, (600 // 2, 250 + index * 60))

        pygame.display.flip()

    # 处理事件
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.selected_option = (self.selected_option - 1) % len(self.menu_options)
            elif event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                self.selected_option = (self.selected_option + 1) % len(self.menu_options)
            elif event.key == pygame.K_RETURN:
                return self.menu_options[self.selected_option]
        return None