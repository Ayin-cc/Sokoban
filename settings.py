import configparser

config = configparser.ConfigParser()
config.read('config/config.cfg')

# Screen
CLOCK = config.getint('Screen', 'clock')