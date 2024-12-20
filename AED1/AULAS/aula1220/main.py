import graphics as gf
import random

random.seed()


def foi_no_botao(botao, onde_cliquei):
    bt_x = botao.getP1().getX()
    bt_y = botao.getP1().getY()
    bt2_x = botao.getP2().getX()
    bt2_y = botao.getP2().getY()
    print(f"({bt_x}, {bt_y}, {bt2_x}, {bt2_y})")
    if onde_cliquei.getX() > bt_x and onde_cliquei.getX() < bt2_x and onde_cliquei.getY() > bt_y and onde_cliquei.getY() < bt2_y:
        return True
    return False


def cria_botao(x1, y1, x2, y2):
    novo_botao = gf.Rectangle(gf.Point(x1,y1), gf.Point(x2, y2))
    novo_botao.setFill('black')
    novo_botao.draw(win)
    return novo_botao 


def aciona_botao(onde_cliquei):
    if foi_no_botao(botao, onde_cliquei):
        botao.setFill('green')
    else:
        botao.setFill('black')


win = gf.GraphWin("Janela", 1200, 900)
botao = cria_botao(300, 500, 600, 700)

while True:
    onde_cliquei = win.getMouse()
    aciona_botao(onde_cliquei)
