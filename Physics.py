import pygame as pg
import math
import numpy as np

pg.init()
screen = pg.display.set_mode((640, 480),pg.RESIZABLE)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 30)
FONT2 = pg.font.Font(None,17)
a=''
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        a=''
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    a = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
        return a
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

                


def main():
    def get_matrix(angle) :
        return np.matrix( ((math.cos(angle),-math.sin(angle)), (math.sin(angle), math.cos(angle))) )
    quit = False
    while not quit: 
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        klin = False
        isBreak = False
        ballistic = False
        clicked = False
        GRAY = (125, 125, 125)
        LIGHT_BLUE = (91,201,232)
        GREEN = (57, 137, 89)
        DARK_GREEN = (0,73,7)
        YELLOW = (225, 225, 0)
        PINK = (230, 50, 230)
        pushed = False
        clock = pg.time.Clock()
        while not clicked:
            height = screen.get_height()
            width = screen.get_width()
            button2 = pg.Rect(width/2-112,height/2-25,225,50)
            button3 = pg.Rect(width/2-112,height/2+30,225,50)
            # button2 = pg.Rect(width/2,height/2,125,50)
            # width = screen.get_width()
            # height = screen.get_height()
            screen.fill(LIGHT_BLUE)
            pg.draw.rect(screen, [255, 255, 255], button2)  # draw button
            new1 = FONT.render('Задачи на баллистику', True,BLACK)
            screen.blit(new1,(width/2-112,height/2-25))
            pg.draw.rect(screen, [255, 255, 255], button3)  # draw button
            new2 = FONT.render('Задачи с клином', True,BLACK)
            screen.blit(new2,(width/2-112,height/2+30))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                    if button3.collidepoint(mouse_pos):
                        klin = True
                        clicked = True
                    if button2.collidepoint(mouse_pos):
                        # prints current location of mouse
                        ballistic = True
                        clicked = True
                        print('button was pressed at {0}'.format(mouse_pos))
            pg.display.flip()
            clock.tick(10)  
        input_box1 = InputBox(5, 20, 35, 22)
        input_box2 = InputBox(5, 80, 35, 22)
        input_box3 = InputBox(5, 140, 35, 22)
        input_box4 = InputBox(5, 200, 35, 22)
        input_boxes = [input_box1, input_box2,input_box3,input_box4]
        done = False
        size = 10
        button = pg.Rect(100, 100, 100, 50)  # creates a rect object
        
        start = False
        
        info=[0,0,0,0]
        if ballistic:
            while not done:
                width = screen.get_width()
                height = screen.get_height()        
                pushed = False
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        done = True
                        quit = True
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos  # gets mouse position

                    # checks if mouse position is over the button

                        if button1.collidepoint(mouse_pos):
                            # prints current location of mouse
                            print('button was pressed at {0}'.format(mouse_pos))
                            start =True
                        if button4.collidepoint(mouse_pos):
                            # prints current location of mouse
                            print('button was pressed at {0}'.format(mouse_pos))
                            isBreak = True
                            
                        
                    for i in range(4):
                        a=input_boxes[i].handle_event(event)
                        if a!='':
                            info[i]=int(a)
                for box in input_boxes:
                    box.update()

                screen.fill(LIGHT_BLUE)
                # print(info)
                for box in input_boxes:
                    box.draw(screen)
                text1 = FONT.render('Координата по оси ОХ', True,BLACK)
                screen.blit(text1, (5, 2))
                
                ox = FONT.render(str(info[0]),True,BLACK)
                screen.blit(ox,(210,23))

                text2 = FONT.render('Координата по оси ОY', True,BLACK)
                screen.blit(text2, (5, 62))

                oy = FONT.render(str(info[1]),True,BLACK)
                screen.blit(oy,(210,83))

                text1 = FONT.render('Угол с горизонтальной осью', True,BLACK)
                screen.blit(text1, (5, 122))

                angle = FONT.render(str(info[2]),True,BLACK)
                screen.blit(angle,(210,143))

                text1 = FONT.render('Начальная скорость', True,BLACK)
                screen.blit(text1, (5, 182))
                
                speed = FONT.render(str(info[3]),True,BLACK)
                screen.blit(speed,(210,203))


                       
                if isBreak:
                    break
                pg.draw.rect(screen, GREEN, (0, height/2, width, height))
                pg.draw.line(screen, DARK_GREEN, [0, height/2], [width, height/2], 10)
                pg.draw.line(screen,BLACK,[300,10],[300,height/2-10])
                for i in range((height//2-10)//size+1):
                    text = FONT2.render(str((height//2-10)//size-i-1),True,GRAY)
                    if (height//2-10)//size-i-1!=-1 and ((height//2-10)//size-i-1)%5==0:
                        screen.blit(text,(300+3,i*size+5))
                    if i!=(height//2-10)//size:
                        pg.draw.line(screen,BLACK,[300-2.5,i*size+10],[300+2.5,i*size+10])
                for i in range(1,width-300//size):
                    if i % 5 == 0:    
                        text = FONT2.render(str(i),True,GRAY)
                        screen.blit(text,(296+i*size,height/2-5))
                    pg.draw.line(screen,BLACK,[300+i*size,height/2-7.5],[300+i*size,height/2-12.5])
                pg.draw.line(screen,BLACK,[300,height/2-10],[width,height/2-10])
                pg.draw.circle(screen,YELLOW,(info[0]*size+300,height/2-(info[1]*size)-10),10)
                height = screen.get_height()
                width = screen.get_width()
                button4 = pg.Rect(width/2,height/2+150,150,50)  
                pg.draw.rect(screen, [255, 255, 255], button4)  # draw button
                new2 = FONT.render('Назад', True,BLACK)
                screen.blit(new2,(width/2,height/2+150))

                pg.draw.line(screen,BLACK,[info[0]*size+300,height/2-(info[1]*size)-10],[info[0]*size+300+math.cos(-info[2]*math.pi/180)*25,height/2-(info[1]*size)-10+math.sin(-info[2]*math.pi/180)*25])
                x = info[0]*size+300
                y = height/2-(info[1]*size)-15
                j=False
                speedX = info[3]*math.cos(-info[2]*math.pi/180)
                speedY = info[3]*math.sin(-info[2]*math.pi/180)
                # speedY=-speedY 
                # print(speedY)
                time=0
                button1 = pg.Rect(width/2,height/2+90, 100, 50) 
                pg.draw.rect(screen, [255, 255, 255], button1)  # draw button
                new = FONT.render('Запустить', True,BLACK)
                screen.blit(new,(width/2,height/2+90))
                frame = 0.0005

                if  start:    
                    start = False    
                    while (y<height/2-15)or(not j):
                        
                        x += frame*speedX*size
                        y += frame*speedY*size
                        speedY += size*frame*10
                        time+=frame*size
                        # time =math.floor(time)
                        # time = round(time,2)
                        # print((2*info[3]*math.sin(math.radians(info[2])))/10)
                        # print(time)
                        if (y<height/2-15):
                            time+=frame*size
                            # time =math.floor(time)
                            # time =round(time,2)
                            x += frame*speedX*size
                            y += frame*speedY*size
                            speedY += size*frame*10
                            screen.fill(LIGHT_BLUE)
                            pg.draw.rect(screen, GREEN, (0, height/2, width, height))
                            pg.draw.line(screen, DARK_GREEN, [0, height/2], [width, height/2], 10)
                            # pg.draw.line(screen,BLACK,[300,10],[300,height/2-10])
                            for i in range((height//2-10)//size+1):
                                text = FONT2.render(str(((height//2-10)//size-i-1)),True,GRAY)
                                if (height//2-10)//size-i-1!=-1 and ((height//2-10)//size-i-1)%5==0:
                                    screen.blit(text,(300+3,i*size+5))
                                if i!=(height//2-10)//size:
                                    pg.draw.line(screen,BLACK,[300-2.5,i*size+10],[300+2.5,i*size+10])
                            for i in range(1,width-300//size):
                                if i % 5 ==0:
                                    text = FONT2.render(str(i),True,GRAY)
                                    screen.blit(text,(296+i*size,height/2-5))
                                pg.draw.line(screen,BLACK,[300+i*size,height/2-7.5],[300+i*size,height/2-12.5])
                            # pg.draw.line(screen,BLACK,[10,height/2-10],[width,height/2-10])
                            
                            pg.draw.line(screen,BLACK,[300,height/2-10],[width,height/2-10])
                            if speedX==0:
                                pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/0.0000000001))*25,y+math.sin(math.atan(speedY/0.0000000001))*25])
                            else:
                                pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/speedX))*25,y+math.sin(math.atan(speedY/speedX))*25])

                            speed = FONT.render(str(round(math.hypot(speedX,speedY))),True,BLACK)
                            if speedX==0:
                                screen.blit(speed, (x+math.cos(math.atan(speedY/0.0000000001))*size,y+math.sin(math.atan(speedY/0.0000000001))*size-3))
                            else:
                                screen.blit(speed, (x+math.cos(math.atan(speedY/speedX))*size,y+math.sin(math.atan(speedY/speedX))*size-3))
                            if info[2]<=0:   
                                a = 2*info[3]*math.sin(math.radians(info[2]))/10
                                a-= 0.06
                            # print(type(a),' ',a)
                            # print(type((-info[3]*math.sin(math.radians(info[2]))+speedY)/10),' ',(-info[3]*math.sin(math.radians(info[2]))+speedY)/10)
                            # print(round(a+((-info[3]*math.sin(math.radians(info[2]))+speedY)/10),2))
                            timeText = FONT.render(str(round(time,2)),True,BLACK)
                            if info[2]>0:   
                                a = 2*info[3]*math.sin(math.radians(info[2]))/10
                                a-= 0.06
                            screen.blit(timeText,(40,height/2+50))
                            pg.draw.circle(screen,YELLOW,(x,y),10)

                        screen.fill(LIGHT_BLUE)
                        j=True
                        
                        pg.draw.rect(screen, GREEN, (0, height/2, width, height))
                        pg.draw.line(screen, DARK_GREEN, [0, height/2], [width, height/2], 10)
                        pg.draw.line(screen,BLACK,[300,10],[300,height/2-10])
                        for i in range((height//2-10)//size+1):
                            text = FONT2.render(str(((height//2-10)//size-i-1)),True,GRAY)
                            if (height//2-10)//size-i-1!=-1 and ((height//2-10)//size-i-1)%5==0:
                                screen.blit(text,(300+3,i*size+5))
                            if i!=(height//2-10)//size:
                                pg.draw.line(screen,BLACK,[300-2.5,i*size+10],[300+2.5,i*size+10])
                        for i in range(1,width-300//size):
                            if i % 5 ==0:
                                text = FONT2.render(str(i),True,GRAY)
                                screen.blit(text,(296+i*size,height/2-5))
                            pg.draw.line(screen,BLACK,[300+i*size,height/2-7.5],[300+i*size,height/2-12.5])
                        pg.draw.line(screen,BLACK,[300,height/2-10],[width,height/2-10])
                        
                        # pg.draw.line(screen,BLACK,[10,height/2-10],[width,height/2-10])
                        if speedX==0:
                            pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/0.0000000001))*25,y+math.sin(math.atan(speedY/0.0000000001))*25])
                        else:
                            pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/speedX))*25,y+math.sin(math.atan(speedY/speedX))*25])

                        speed = FONT.render(str(round(math.hypot(speedX,speedY),2)),True,BLACK)
                        if info[2]>0:   
                            a = 2*info[3]*math.sin(math.radians(info[2]))/10
                            a-= 0.06
                        if speedX==0:
                            screen.blit(speed, (x+math.cos(math.atan(speedY/0.0000000001))*size,y+math.sin(math.atan(speedY/0.0000000001))*size-3))
                        else:
                            screen.blit(speed, (x+math.cos(math.atan(speedY/speedX))*size,y+math.sin(math.atan(speedY/speedX))*size-3))
                        # if info[2] == 90:
                        #     timeText = FONT.render(str(round(a+0.01+((-info[3]*math.sin(math.radians(info[2]))+speedY)/10),2)),True,BLACK)
                        # else:
                        timeText = FONT.render(str(round(time,2)),True,BLACK)
                        screen.blit(timeText,(40,height/2+50))
                        

                        pg.draw.circle(screen,YELLOW,(x,y),10)

                        pg.display.update()
                        clock.tick(200)
                    
                        


                    screen.fill(LIGHT_BLUE)
                    pg.draw.rect(screen, GREEN, (0, height/2, width, height))
                    pg.draw.line(screen, DARK_GREEN, [0, height/2], [width, height/2], 10)
                    pg.draw.line(screen,BLACK,[300,10],[300,height/2-10])
                    for i in range((height//2-10)//size+1):
                        text = FONT2.render(str(((height//2-10)//size-i-1)),True,GRAY)
                        if (height//2-10)//size-i-1!=-1 and ((height//2-10)//size-i-1)%5==0:
                            screen.blit(text,(300+3,i*size+5))
                        if i!=(height//2-10)//size:
                            pg.draw.line(screen,BLACK,[300-2.5,i*size+10],[300+2.5,i*size+10])
                    for i in range(1,width-300//size):
                        if i % 5 ==0:
                            text = FONT2.render(str(i),True,GRAY)
                            screen.blit(text,(296+i*size,height/2-5))
                        pg.draw.line(screen,BLACK,[300+i*size,height/2-7.5],[300+i*size,height/2-12.5])
                    pg.draw.line(screen,BLACK,[300,height/2-10],[width,height/2-10])
                    
                    # pg.draw.line(screen,BLACK,[10,height/2-10],[width,height/2-10])
                    # pg.draw.circle(screen,YELLOW,(info[0]*size+300,height/2-(info[1]*size)-14),10)
                    if speedX==0:
                        pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/0.0000000001))*25,y+math.sin(math.atan(speedY/0.0000000001))*25])
                    else:
                        pg.draw.line(screen,BLACK,[x,y],[x+math.cos(math.atan(speedY/speedX))*25,y+math.sin(math.atan(speedY/speedX))*25])

                    # speed = FONT.render(str(round(math.hypot(speedX,speedY),2)),True,BLACK)
                    
                    # screen.blit(speed, (x+math.cos(math.atan(speedY/speedX))*size,y+math.sin(math.atan(speedY/speedX))*size-3))
                    
                        # speed = FONT.render(str(info[3]),True,BLACK)
                        # screen.blit(speed, (x+math.cos(math.atan(speedY/speedX))*size,y+math.sin(math.atan(speedY/speedX))*size-3))
                    # timeText = FONT.render(str(round(a+((-info[3]*math.sin(math.radians(info[2]))+speedY)/10),2)),True,BLACK)
                    screen.blit(timeText,(40,height/2+50))

                    pg.draw.circle(screen,YELLOW,(x,y),10)

                    
                    speed = FONT.render(str(round(math.hypot(speedX,speedY))),True,BLACK)
                    
                    
                    
                    if speedX==0:
                        screen.blit(speed, (x+math.cos(math.atan(speedY/0.0000000001))*size,y+math.sin(math.atan(speedY/0.0000000001))*size-3))
                    else:
                        screen.blit(speed, (x+math.cos(math.atan(speedY/speedX))*size,y+math.sin(math.atan(speedY/speedX))*size-3))


                    while not pushed:
                        pg.draw.rect(screen, [255, 255, 255], button)  # draw button
                        new = FONT.render('Заново', True,BLACK)
                        screen.blit(new,(100,100))
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                quit = True
                                return False
                            if event.type == pg.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos  # gets mouse position

                            # checks if mouse position is over the button

                                if button.collidepoint(mouse_pos):
                                    # prints current location of mouse
                                    pushed = True
                                    info=[0,0,0,0]
                                    print('button was pressed at {0}'.format(mouse_pos))
                        pg.display.flip()
                        clock.tick(10)                    
                pg.display.flip()
                clock.tick(50)
            if isBreak:
                continue
        elif klin:
            info.append(0)
            input_boxes.append(InputBox(5, 260, 35, 22))   
            while not done:

                button4 = pg.Rect(width/2,height/2+150,150,50)  
                
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        quit = True
                        done = True
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos 

                        if button4.collidepoint(mouse_pos):
                            # prints current location of mouse
                            # print('button was pressed at {0}'.format(mouse_pos))
                            done = True
                    for i in range(5):
                            a=input_boxes[i].handle_event(event)
                            if a!='':
                                info[i]=int(a)
                for box in input_boxes:
                    box.update()
                screen.fill(LIGHT_BLUE)
                pg.draw.rect(screen, GREEN, (0, height/2, width, height))
                pg.draw.line(screen, DARK_GREEN, [0, height/2], [width, height/2], 10)
                for i in range((height//2-10)//size+1):
                    text = FONT2.render(str(((height//2-10)//size-i-1)),True,GRAY)
                    if (height//2-10)//size-i-1!=-1 and ((height//2-10)//size-i-1)%5==0:
                        screen.blit(text,(300+3,i*size+5))
                    if i!=(height//2-10)//size:
                        pg.draw.line(screen,BLACK,[300-2.5,i*size+10],[300+2.5,i*size+10])
                for i in range(1,width-300//size):
                    if i % 5 ==0:
                        text = FONT2.render(str(i),True,GRAY)
                        screen.blit(text,(296+i*size,height/2-5))
                    pg.draw.line(screen,BLACK,[300+i*size,height/2-7.5],[300+i*size,height/2-12.5])
                pg.draw.line(screen,BLACK,[300,height/2-10],[width,height/2-10])
                pg.draw.line(screen,BLACK,[300,10],[300,height/2-10])
                for box in input_boxes:
                    box.draw(screen)

                height = screen.get_height()
                width = screen.get_width()


                
                button1 = pg.Rect(width/2,height/2+90, 100, 50) 
                pg.draw.rect(screen, [255, 255, 255], button1)  # draw button
                new = FONT.render('Запустить', True,BLACK)
                screen.blit(new,(width/2,height/2+90))
                pg.draw.rect(screen, [255, 255, 255], button4)
                new2 = FONT.render('Назад', True,BLACK)
                screen.blit(new2,(width/2,height/2+150))

                text1 = FONT.render('Длина клина', True,BLACK)
                screen.blit(text1, (5, 2))
                
                ox = FONT.render(str(info[0]),True,BLACK)
                screen.blit(ox,(210,23))

                text2 = FONT.render('Высота клина', True,BLACK)
                screen.blit(text2, (5, 62))

                oy = FONT.render(str(info[1]),True,BLACK)
                screen.blit(oy,(210,83))

                text1 = FONT.render('Высота тела на клине', True,BLACK)
                screen.blit(text1, (5, 122))

                angle = FONT.render(str(info[2]),True,BLACK)
                screen.blit(angle,(210,143))

                text1 = FONT.render('Коэффициент трения', True,BLACK)
                screen.blit(text1, (5, 182))
                
                speed = FONT.render(str(info[3]),True,BLACK)
                screen.blit(speed,(210,203))

                text1 = FONT.render('Масса тела', True,BLACK)
                screen.blit(text1, (5, 242))
                
                speed = FONT.render(str(info[4]),True,BLACK)
                screen.blit(speed,(210,263))

                if info[0]>0 and info[1]>0:
                    pg.draw.polygon(screen, WHITE,
                  [[300, height//2-10-info[1]*size], [300, height//2-10],
                   [300+info[0]*size,height//2-10]])  
                if info[2]>0:
                    height = screen.get_height()
                    width = screen.get_width()
                    angle = math.atan(info[1]/info[0])
                    heightTr = info[2]
                    lengthTr = heightTr/math.tan(info[1]/info[0])
                    point1 = (300+info[0],height//2-30)
                    point2 = (300+info[0],height//2-10)
                    point4 = (330+info[0],height//2-10)
                    point3 = (330+info[0],height//2-30)
                    points = np.array((point1,point2,point3,point4))
                    # print(get_matrix(angle))
                    # print(points)
                    # print(get_matrix(angle)*points)
                    x = np.array( points )
                    y = get_matrix(-angle)
                    # np.matrix(get_matrix(angle))
                    x1 = np.array([[-15,-10],[-15,10],[15,10],[15,-10]])
                    for i in range(4):
                        x1[i][1]+=height//2-10
                        x1[i][0]+=300    
                    print('xfffffааааfffff  ffffFFFFFFfffААААААА',(x1*y).tolist())
                    result = (x1*y).tolist()
                    pg.draw.polygon(screen,YELLOW,result)
                
                pg.display.flip()
                clock.tick(10)
                

if __name__ == '__main__':
    main()
    pg.quit()