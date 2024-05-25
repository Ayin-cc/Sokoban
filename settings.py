import configparser

config = configparser.ConfigParser()
config.read('config/config.cfg')

# Screen
CLOCK = config.getint('Screen', 'clock')

# Map
DEFAULT_NUM = config.getint("Map", "default_num")
CURRENT_MAP = config.get('Map', "current_map")