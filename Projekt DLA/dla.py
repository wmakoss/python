import pygame
from random import randint
import png

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
POINTSIZE = 3
DISPLAY_WIDTH = 1
DISPLAY_HEIGHT = 1

AMOUNT = 4000
SHOW = True
PNGFILENAME = "dla.png"

display = None
walkerslist = list()

class Walker():
    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y
    
    def random_move(self):
        rand = randint(0, 3)
        while True:
            if rand == 0:
                if self.y > 0:
                    self.y -= 1
                    break
            elif rand == 1:
                if self.x < DISPLAY_WIDTH-1:
                    self.x += 1
                    break
            elif rand == 2:
                if self.y < DISPLAY_HEIGHT-1:
                    self.y += 1
                    break
            elif rand == 3:
                if self.x > 0:
                    self.x -= 1
                    break

            rand = randint(0, 3)
            
    def check_neighbors(self):
        for i in range(max(self.x-1,0),min(self.x+1,DISPLAY_WIDTH-1)+1):
            for j in range(max(self.y-1,0),min(self.y+1,DISPLAY_HEIGHT-1)+1):
                if display.get(i, j) == (255, 0, 0):
                    return True
        return False

class Display:
    def create(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.pixel_array = pygame.PixelArray(self.window)

    def set(self, x, y, r, g, b):
        if x>0 and y>0 and x<DISPLAY_WIDTH and y<=DISPLAY_HEIGHT:
            for i in range(POINTSIZE*x, POINTSIZE*x + POINTSIZE):
                for j in range(POINTSIZE*y, POINTSIZE*y + POINTSIZE):
                    self.pixel_array[i, j] = (((r*256)+g)*256)+b
            # pygame.display.flip()

    def get(self, x, y):

        if x<0 or y<0 or x>=DISPLAY_WIDTH or y>=DISPLAY_HEIGHT:
            return (0,0,0)

        color = self.pixel_array[POINTSIZE*x, POINTSIZE*y]
        b = int(color % 256)
        color /= 256
        g = int(color % 256)
        color /= 256
        r = int(color)

        return (r, g, b)
    
    def close(self):
        self.pixel_array.close()
        pygame.quit()
        # exit()


def main_loop():
    global SHOW
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SHOW:
                    SHOW = False
                else:
                    SHOW = True

        for walker in walkerslist:
            display.set(walker.x, walker.y, 0, 0, 0) # hide green point
            walker.random_move()
            if walker.check_neighbors():
                display.set(walker.x, walker.y, 255, 0, 0)
                walkerslist.remove(walker)
                print(str(AMOUNT - len(walkerslist)) + " / " + str(AMOUNT))
                if len(walkerslist) == 0:
                    run = False
            else:
                if SHOW:
                    display.set(walker.x, walker.y, 0, 255, 0) # display green point
        
        pygame.display.flip()

def save_to_png():
    img = []
    for y in range(WINDOW_HEIGHT):
        row = ()
        for x in range(WINDOW_WIDTH):
            row = row + display.get(x//POINTSIZE,y//POINTSIZE)
        img.append(row)
    with open(str(PNGFILENAME), 'wb') as f:
        w = png.Writer(WINDOW_WIDTH, WINDOW_HEIGHT, greyscale=False)
        w.write(f, img)

if __name__ == "__main__":
    value = input(f"WINDOW WIDTH ({WINDOW_WIDTH}) : ")
    if value.isnumeric():
        WINDOW_WIDTH = int(value)

    value = input(f"WINDOW HEIGHT ({WINDOW_HEIGHT}) : ")
    if value.isnumeric():
        WINDOW_HEIGHT = int(value)

    value = input(f"POINT SIZE ({POINTSIZE}) : ")
    if value.isnumeric():
        POINTSIZE = int(value)

    DISPLAY_WIDTH = WINDOW_WIDTH // POINTSIZE
    DISPLAY_HEIGHT = WINDOW_HEIGHT // POINTSIZE

    value = input(f"AMOUNT ({AMOUNT}) : ")
    if value.isnumeric():
        AMOUNT = int(value)

    print("WINDOW WIDTH :" + str(WINDOW_WIDTH))
    print("WINDOW HEIGHT :" + str(WINDOW_HEIGHT))
    print("POINT SIZE :" + str(POINTSIZE))
    print("DISPLAY WIDTH :" + str(DISPLAY_WIDTH))
    print("DISPLAY HEIGHT :" + str(DISPLAY_HEIGHT))
    print("AMOUNT :" + str(AMOUNT))

    display = Display()

    display.create()

    for i in range(AMOUNT):
        randx = randint(0, DISPLAY_WIDTH-1)
        randy = randint(0, DISPLAY_HEIGHT-1)
        walkerslist.append(Walker(randx, randy))
        display.set(randx, randy, 0, 255, 0) # display green point

    # random start
    # randx = randint(0, DISPLAY_WIDTH-1)
    # randy = randint(0, DISPLAY_HEIGHT-1)

    randx = DISPLAY_WIDTH // 2
    randy = DISPLAY_HEIGHT // 2

    display.set(randx, randy, 255, 0, 0)

    main_loop()

    save_to_png()

    display.close()
