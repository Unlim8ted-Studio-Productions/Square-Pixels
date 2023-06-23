import pygame as p, random as r
class TerrainGenerator:
    def __init__(self, w, h, x=0, y=0):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.t = []
        self.cx = 0
        self.cy = 0
    def g(self):
        self.t = [[0 for _ in range(self.w[1])] for _ in range(self.h)]
        gl = [self.h//2]*self.w[1]
        for x in range(self.w[0],self.w[1]):
            gl[x]=gl[x-1]+r.randint(-2,2)
            gl[x]=max(0,min(self.h-1,gl[x]))
        for x in range(self.w[0],self.w[1]):
            for y in range(gl[x],self.h):
                self.t[y][x]=r.choice([0,1])
        for x in range(self.w[0],self.w[1]):
            for y in range(gl[x]):
                self.t[y][x]=8
        tc=self.w[1]//10
        for _ in range(tc):
            tx=r.randint(0,self.w[1]-1)
            tpo=r.randint(5,10)
            ty=gl[tx]-tpo
            th=tpo
            for y in range(ty,ty+th):
                self.t[y][tx]=2
            lr=r.randint(2,4)
            for dx in range(-lr,lr+1):
                for dy in range(-lr,lr+1):
                    if 0<=tx+dx<self.w[1] and 0<=ty+dy<self.h:
                        if abs(dx)+abs(dy)<=lr:
                            self.t[ty+dy][tx+dx]=3
        oc=self.w[1]//100
        for _ in range(oc):
            ot=r.choice([4,5,6,7])
            ox=r.randint(0,self.w[1]-1)
            vn=False
            while not vn:
                try:
                    oy=r.randint(gl[ox]+1,self.h-1)
                except ValueError:
                    vn=False
                else:
                    vn=True
            orad=r.randint(1,4)
            for dx in range(-orad,orad+1):
                for dy in range(-orad,orad+1):
                    if 0<=ox+dx<self.w[1] and 0<=oy+dy<self.h:
                        if abs(dx)+abs(dy)<=orad:
                            self.t[oy+dy][ox+dx]=ot
    def run(self,s):
        c=p.time.Clock()
        self.g()
        vx=0
        vy=0
        s.fill((0,0,0))
        p.display.flip()
        c.tick(60)
def s():
    p.init()
    io=p.display.Info()
    s=p.display.set_mode((io.current_w,io.current_h))
    p.display.set_caption("terraria styledgame")
    p.mouse.set_cursor(p.SYSTEM_CURSOR_CROSSHAIR)
    tg=TerrainGenerator(800,io.current_h//10)
    tg.run(s)
