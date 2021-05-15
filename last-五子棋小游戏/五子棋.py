# -*- coding=utf-8 -*-
import pygame

pygame.init()

space = 60 # 四周留下的边距
cell_size = 40 # 每个格子大小
cell_num = 15
grid_size = cell_size * (cell_num - 1) + space * 2 # 棋盘的大小
screencaption = pygame.display.set_caption('FIR')
screen = pygame.display.set_mode((grid_size + 200,grid_size)) #设置窗口长宽(680)

chess_arr = [] #棋子数组，存放棋子位置
flag = 1 # 1黑 2白
game_state = 1 # 游戏状态1.表示正常进行 2.表示黑胜 3.表示白胜



myfont = pygame.font.SysFont('SimHei', 40)

DarkKhaki = 189,183,107
yellow = 255,255,0
Pink = 255,192,203

# 自定义按钮
class Button():
    # msg为要在按钮中显示的文本
    def __init__(self,screen,centerxy,width, height,button_color,text_color, msg,size):
        """初始化按钮的属性"""
        self.screen = screen
        # 按钮宽高
        self.width, self.height = width, height
        # 设置按钮的rect对象颜色为深蓝
        self.button_color = button_color
        # 设置文本的颜色为白色
        self.text_color = text_color
        # 设置文本为默认字体，字号为20
        self.font = pygame.font.SysFont('SimHei', size)
        # 设置按钮大小
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 创建按钮的rect对象，并设置按钮中心位置
        self.rect.centerx = centerxy[0]-self.width/2+2
        self.rect.centery= centerxy[1]-self.height/2+2
        # 渲染图像
        self.deal_msg(msg)

    def deal_msg(self, msg):
        """将msg渲染为图像，并将其在按钮上居中"""
        # render将存储在msg的文本转换为图像
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # 根据文本图像创建一个rect
        self.msg_img_rect = self.msg_img.get_rect()
        # 将该rect的center属性设置为按钮的center属性
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # 填充颜色
        self.screen.fill(self.button_color, self.rect)
        # 将该图像绘制到屏幕
        self.screen.blit(self.msg_img, self.msg_img_rect)

def get_one_dire_num(lx, ly, dx, dy, m): 
    tx = lx
    ty = ly
    s = 0
    #没越界且有子加一个棋子
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[ty][tx] == 0: return s
        s+=1

#检查是否获胜
def check_win(chess_arr, flag):
    m = [[0]*cell_num for i in range(cell_num)] # 先定义一个15*15的全0的数组,不能用[[0]*cell_num]*cell_num的方式去定义因为一位数组会被重复引用
    # m = [[0]*cell_num]*cell_num这是浅拷贝，一个赋值全都赋值
    for x, y, c in chess_arr:
        if c == flag:
            m[y][x] = 1 # 上面有棋则标1
    lx = chess_arr[-1][0] # 最后一个子的x
    ly = chess_arr[-1][1] # 最后一个子的y
    # 4个方向数组,往左＋往右、往上＋往下、往左上＋往右下、往左下＋往右上，4组判断方向
    dire_arr = [[(-1,0) , (1,0)],
                [(0,-1) , (0,1)],
                [(-1,-1), (1,1)],
                [(-1,1) , (1,-1)]]
    
    for dire1,dire2 in dire_arr: #判断四个方向
        dx, dy = dire1
        num1 = get_one_dire_num(lx, ly, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(lx, ly, dx, dy, m)
        if num1 + num2 + 1 >= 5: return True

    return False

while True:
    screen.fill((34,139,34)) # 将界面设置为蓝色
    for x in range(0,cell_size*cell_num,cell_size): #共执行15次，0-14
        pygame.draw.line(screen,(DarkKhaki),(x+space,0+space),(x+space,cell_size*(cell_num-1)+space),2) #画列
    for y in range(0,cell_size*cell_num,cell_size):
        pygame.draw.line(screen,(DarkKhaki),(0+space,y+space),(cell_size*(cell_num-1)+space,y+space),2) 
    
    #绘制重新开始按钮
    button_reset = Button(screen, (850, 150), 150, 60, yellow, DarkKhaki, "重新开始", 25)
    button_reset.draw_button()
    #绘制退出按钮
    button_quit = Button(screen,(850,250),150,60,yellow, DarkKhaki, "退出游戏", 25)
    button_quit.draw_button()
    #绘制悔棋按钮
    button_back = Button(screen,(850,350),150,60,yellow, DarkKhaki, "悔棋", 25)
    button_back.draw_button()
    #判断游戏状态
    for event in pygame.event.get():
         # print(event)
         if event.type == pygame.QUIT:
             pygame.quit()
             # exit()
    
         if game_state == 1 and event.type == pygame.MOUSEBUTTONUP: # 鼠标弹起
             x, y = pygame.mouse.get_pos() # 获取鼠标位置
             # print(x,y)
             xi = round((x - space)/cell_size) # 获取到x方向上取四舍五入的位置
             yi = round((y - space)/cell_size) # 获取到y方向上取四舍五入的位置
             #判断位置是否在期盼区域内并且是否已经有棋子
             if xi>=0 and xi<cell_num and yi>=0 and yi<cell_num and (xi,yi,1) not in chess_arr and (xi,yi,2) not in chess_arr:
                 chess_arr.append((xi,yi,flag))
                 # print(chess_arr)
                 if check_win(chess_arr, flag):#最后一颗棋子落下的时候判断
                     game_state = 2 if flag == 1 else 3 #判断谁赢
                 else:
                     flag = 2 if flag == 1 else 1 #更换棋手
            #判断是否重新开始
             if x <= 850 and x >= 700 and y <= 150 and y >= 90 :
                 chess_arr = []
            #退出按钮
             if x <= 850 and x >= 700 and y <= 250 and y >= 190 :
                pygame.quit()
             #悔棋按钮
             if x <= 850 and x >= 700 and y <= 350 and y >= 290 :
                chess_arr.pop()
                flag = 2 if flag == 1 else 1 #更换棋手
         #游戏结束时
         if (game_state == 2 or game_state == 3)  and event.type == pygame.MOUSEBUTTONUP: # 鼠标弹起
             x, y = pygame.mouse.get_pos() # 获取鼠标位置
             print(x,y)
             #判断是否重新开始
             if x <= 850 and x >= 700 and y <= 150 and y >= 90 :
                 chess_arr = []
                 game_state = 1
             #退出按钮
             if x <= 850 and x >= 700 and y <= 250 and y >= 190 :
                pygame.quit()
            
    #绘制棋子\游戏状态
    for x, y, c in chess_arr:
        chess_color = (0,0,0) if c == 1 else (225,225,225)
        
        pygame.draw.circle(screen, chess_color, [x*cell_size+space, y*cell_size+space], 16,16)
        
        player_text = "%s time" % ('Black' if flag == 1 else 'White')
        textImage = myfont.render(player_text, True, Pink)
        screen.blit(textImage, (650,10))
        print(chess_arr)
    #绘制游戏结束状态
    if game_state != 1:
        win_text = "%s win"%('black' if game_state == 2 else 'white')
        textImage = myfont.render(win_text, True, yellow)
        screen.blit(textImage, (260,320))
    #更新界面
    pygame.display.update() # 必须调用update才能看到绘图显示