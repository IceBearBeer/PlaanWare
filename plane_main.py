import pygame
from plane_sprites import *
# 常量命名方式 所有字母都是大写_大写


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化.")
        # 1. 创建游戏的窗口
        # 第一参数是屏幕的宽度,第二个是屏幕的高度
        # 最好不要写死固定数值
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法,精灵和精灵组的创建
        self.__creat_sprites()

        # 4. 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)

    def __creat_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌人的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵族
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 1. 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                # print("敌人出场.")
                # 创建敌人精灵
                enemy = Enemy()
                # 将敌人精灵添加到精灵族
                self.enemy_group.add(enemy)
            # 事件监听每按下一次,只会响应一次
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("向右移动")
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应按键的索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束了!")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()