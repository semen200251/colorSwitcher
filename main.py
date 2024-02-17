from colors_cityscapes import COLORS_TO_SWITCH_cityscapes
from ColorSwitcher import ColorSwitcher

cityscapes = ColorSwitcher("D:\\datasetPreparation", "D:\\datasetPreparation\\prep", "color.png", COLORS_TO_SWITCH_cityscapes)
cityscapes.switch_color()


'''
Итоговые классы:        1) Пустота (0, 0, 0)
                        2) Растительность (0, 102, 0)
                        3) Песок (255, 229, 204)
                        4) Деревья/кусты (255, 153, 204)
                        5) Транспорт (255, 255, 0)
                        6) Асфальт (64, 64, 64)
                        7) Гравий (255, 128, 0)
                        8) Здание (255, 0, 0)
                        9) Каменная воперхность (102, 102, 0)
                        10) Препятствие (102, 0, 0)
                        11) Человек (204, 153, 255)
                        12) Знак (0, 102, 102)
                        13) Парковка (250, 170, 160)
                        14) ЖД пути (230, 150, 140)
                        15) Светофор (250, 170, 30)
'''