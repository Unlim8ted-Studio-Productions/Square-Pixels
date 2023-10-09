import pygame as p, terraingen.terrain_gen as t, render.render as render, typing as tp, uimanagement.logo as l

if __name__ == "__main__":
    p.init()
    c = p.time.Clock()
    n = True
    v = r"terraria_styled_game\\Company Animated Logo.mov"
    i = p.display.Info()
    s = p.display.set_mode((i.current_w, i.current_h))
    p.display.set_caption("terraria styledgame")
    p.mouse.set_cursor(p.SYSTEM_CURSOR_CROSSHAIR)
    f = r"terraria_styled_game\\frames"
    l.play_intro_video(f, n, s)
    tt = t.TerrainGenerator((0, 800), i.current_h // 10)
    tt.run(s)
    x, y = 0, 0
    r = True
    while r:
        for e in p.event.get():
            if e.type == p.QUIT:
                r = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_UP or e.key == ord("w"):
                    y = -1
                elif e.key == p.K_DOWN or e.key == ord("s"):
                    y = 1
                elif e.key == p.K_LEFT or e.key == ord("a"):
                    x = -1
                elif e.key == p.K_RIGHT or e.key == ord("d"):
                    x = 1
        tt.cx += x
        tt.cy += y
        s.fill((0, 0, 0))
        render.d(s, tt.w, tt.h, tt.t, tt.x, tt.y, tt.cx, tt.cy)
        p.display.flip()
        c.tick(60)
