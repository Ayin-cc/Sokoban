import configparser
import pickle
import os

def set_cfg(section, key, value):
    config = configparser.ConfigParser()
    config.write('config/config.cfg')
    config.set(section, key, value)

def save_map(map_data, filename):
    with open(filename, 'w') as file:
        pickle.dump(map_data, file)

def load_map(filename):
    filename = os.path.join("maps", filename)
    if not validate_map_file(filename):
        return None
    with open(filename, 'r') as file:
        lines = file.readlines()
    # 将每一行拆分为字符列表，存储在二维列表中
    map = [list(line.strip()) for line in lines]
    return map
    

    
# 验证地图是否规范
def validate_map_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if len(lines) != 15:
        return False

    num_3 = 0
    num_4 = 0
    num_5 = 0

    for line in lines:
        if len(line.strip()) != 15:
            return False
        for char in line.strip():
            if char not in ['1', '2', '3', '4', '5', '6']:
                return False
            if char == '3':
                num_3 += 1
            elif char == '4':
                num_4 += 1
            elif char == '5':
                num_5 += 1

    print(f"3: {num_3}")
    print(f"4: {num_4}")
    print(f"5: {num_5}")
    if num_3 != num_4 or num_5 != 1:
        return False

    return True