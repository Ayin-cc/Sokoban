import pygame

class About:
    def __init__(self, screen):
        self.screen = screen
        font_name = pygame.font.match_font('fangsong')
        self.font = pygame.font.Font(font_name, 42)  # 标题字体
        self.small_font = pygame.font.Font(font_name, 30)  # 选项字体

    def display(self):
        # 清空屏幕
        self.screen.fill((0, 0, 0))

        # 文本内容
        color = (255, 255, 255)
        h1 = self.font.render("操作说明:", True, color)
        h2 = self.font.render("其他", True, color)
        descriptions = [
            "向上移动: W 或 ↑",
            "向左移动: A 或 ←",
            "向右移动: D 或 →",
            "向下移动: S 或 ↓",
            "撤销操作: Z",
            "重新开始: P",
            "返回菜单: M"
        ]
        self.screen.blit(h1, (60, 60))
        for index, it in enumerate(descriptions):
            text = self.small_font.render(it, True, color)
            self.screen.blit(text, (60, 120 + index * 40))
        details = [
            "游戏版本: v1.0",
            "作者: Ayin"
        ]
        self.screen.blit(h2, (400, 60))
        for index, it in enumerate(details):
            text = self.small_font.render(it, True, color)
            self.screen.blit(text, (400, 120 + index * 40))

        # 返回主菜单
        color = (255, 255, 0)
        back = self.font.render("返回主菜单", True, color)
        self.screen.blit(back, (300, 500))

        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "menu"
        return "about"