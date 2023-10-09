import pygame as a
import typing as b
import player.player as c


def d(
    e: a.Surface,
    f: b.Union[float, int],
    g: b.Union[float, int],
    h: list,
    i: b.Union[float, int],
    j: b.Union[float, int],
    k: b.Union[float, int],
    l: b.Union[float, int],
):
    m = 10
    n = [
        (100, 100, 100),
        (139, 69, 19),
        (139, 115, 85),
        (34, 139, 34),
        (0, 128, 0),
        (211, 211, 211),
        (255, 223, 0),
        (128, 128, 128),
        (135, 206, 235),
    ]
    for o in range(f[0], f[1]):
        for p in range(g):
            q = h[p][o]
            r = n[q]
            a.draw.rect(
                e,
                r,
                (
                    (o + i - k) * m,
                    (p + j - l) * m,
                    m,
                    m,
                ),
            )


def s(e: a.Surface, o: float | int, p: float | int, q: int, r: tuple):
    a.draw.circle(e, r, (o, p), q, q)


def t(e: a.Surface, u: list):
    for v in u:
        a.draw.circle(e, v.color, (v.x, v.y), v.size, v.size)


def y(ab: b.Dict[str, int]) -> b.List[b.Tuple[str, int]]:
    ac = sorted(ab.items(), key=lambda x: x[1], reverse=True)
    return ac


def z(ae: b.List[str], af: int, ag: a.Surface) -> None:
    font = a.font.Font(None, 20)
    for i, ah in enumerate(ae):
        ai = font.render(ah, True, (255, 255, 255))
        if 10 + i * 20 >= af - 30:
            aj = ae[i]
            i = 0
            ae.clear()
            ae.append(aj)
            ak = ai.get_rect(left=10, top=10 + i * 20)
            ag.blit(ai, ak)
        else:
            ak = ai.get_rect(left=10, top=10 + i * 20)
            ag.blit(ai, ak)


def al(ai: b.Dict[str, int], ag: a.Surface) -> None:
    am = y(ai)
    font = a.font.Font(None, 20)
    for i, an in enumerate(am):
        ao, ap = an
        ai = font.render(f"{ao}: {ap}", True, (255, 255, 255))
        ar = ai.get_rect(left=700, top=10 + i * 20)
        ag.blit(ai, ar)


def as_hitboxes(ai: b.Dict[str, int]) -> dict:
    am = y(ai)
    aq = {}
    for i, an in enumerate(am):
        ao, ap = an
        aq[ao] = a.Rect((700, 10 + i * 20, 30, 10))
    return aq


def au(hitboxes: dict, u: list, ag, ab: dict, ax: list) -> tuple:
    for hitbox in hitboxes:
        if hitboxes[hitbox].collidepoint(a.mouse.get_pos()):
            a.draw.rect(ag, (255, 0, 0), rect=hitboxes[hitbox])
            if a.mouse.get_pressed()[0]:
                ay = hitbox
                print(u)
                if ay is not None:
                    for az in u:
                        if az.name == ay:
                            u.remove(az)
                            break
                    for az in ab:
                        if az == ay:
                            ab.pop(az)
                            ax.append(az)
                            break

    return u, ab, ax


class aq:
    def __init__(self, az: c.Player):
        self.player = az

    def draw(self, ag: a.Surface) -> None:
        font = a.font.Font(None, 20)
        ai = font.render(self.player.name, True, (255, 255, 255))
        ak = ai.get_rect(center=(self.player.x, self.player.y - 15))
        ag.blit(ai, ak)
