import pygame
from  settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化pygame,设置和屏幕对象
    
    pygame.init() #初始化背景设置
    ai_settings =Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    

    #设置背景色
    bg_color =(230,230,230)


    #创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    
    #创建外星人群
    #alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环
    while True:


        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        #每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        
        



        


run_game()
