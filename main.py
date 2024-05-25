import pygame
import sys

from settings import CLOCK, CURRENT_MAP
from utils import load_map
from app.menu import Menu
from app.map_selection import MapSelection
from app.game_core import GameCore
from app.about import About

def main():
    # 初始化
    pygame.init()
    # 窗口大小
    screen = pygame.display.set_mode((500, 520))
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
    init_map = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if current_state == "menu":
                # 处理主菜单模块的事件
                selection = menu.handle_events(event)
                if selection == "开始游戏":
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
                selection = map_selection.handle_events(event)
                if selection == "开始游戏":
                    current_state = "game"
                elif selection == "主菜单":
                    current_state = "menu"
            elif current_state == "game":
                # 处理游戏核心模块的事件
                selection = game_core.handle_events(event)
                if selection == "主菜单":
                    init_map = False
                    current_state = "menu"
                elif selection == "选择地图":
                    init_map = False
                    current_state = "map_selection"
            elif current_state == "about":
                # 处理游戏介绍模块的事件
                selection = about.handle_events(event)
                if selection == "主菜单":
                    current_state = "menu"

            # 渲染帧画面
            if current_state == "menu":
                menu.display()
            elif current_state == "map_selection":
                map_selection.display()
            elif current_state == "game":
                if not init_map:
                    game_core.target_positions.clear()
                    if map_selection.map_selected == 0:
                        game_core.setMap(load_map(CURRENT_MAP))
                        map_selection.column = 1
                        map_selection.pack_selecting = False
                        map_selection.pack_selected = 0
                        map_selection.map_selected = 1
                    else:
                        if map_selection.pack_selected == 0:
                            game_core.setMap(map_selection.default_maps[map_selection.map_selected - 1])
                        else:
                            game_core.setMap(map_selection.diy_maps[map_selection.map_selected - 2])
                    init_map = True
                game_core.display()
            elif current_state == "about":
                about.display()
            


if __name__ == "__main__":
    main()