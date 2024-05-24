import pygame
import sys

from settings import CLOCK
from app.menu import Menu
from app.map_selection import MapSelection
from app.game_core import GameCore
from app.about import About

def main():
    # 初始化
    pygame.init()
    # 窗口大小
    screen = pygame.display.set_mode((800, 600))
    # 窗口标题
    pygame.display.set_caption("推箱子")
    # 帧数
    clock = pygame.time.Clock()
    clock.tick(CLOCK)

    menu = Menu(screen)
    map_selection = MapSelection(screen)
    game_core = GameCore(screen)
    about = About(screen)

    current_state = "menu"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if current_state == "menu":
                # 处理主菜单模块的事件
                selection = menu.handle_events(event)
                if selection == "开始新游戏":
                    current_state = "game"
                elif selection == "选择地图":
                    current_state = "map_selection"
                elif selection == "游戏介绍":
                    current_state = "about"
                elif selection == "退出游戏":
                    pygame.quit()
                    sys.exit()
            elif current_state == "map_selection":
                # 处理地图选择模块的事件
                map_selection.handle_events(event)
            elif current_state == "game":
                # 处理游戏核心模块的事件
                game_core.handle_events(event)
            elif current_state == "about":
                # 处理游戏介绍模块的事件
                current_state = about.handle_events(event)

        # 渲染帧画面
        if current_state == "menu":
            menu.display()
        elif current_state == "map_selection":
            map_selection.display()
        elif current_state == "game":
            game_core.run()
        elif current_state == "about":
            about.display()
            


if __name__ == "__main__":
    main()