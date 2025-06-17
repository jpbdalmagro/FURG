import graphics 
from time import sleep


def foi_no_botao(botao, onde_cliquei):
    bt_x = botao.getP1().getX()
    bt_y = botao.getP1().getY()
    bt2_x = botao.getP2().getX()
    bt2_y = botao.getP2().getY()
    print(f"({bt_x}, {bt_y}, {bt2_x}, {bt2_y})")
    if onde_cliquei.getX() > bt_x and onde_cliquei.getX() < bt2_x and onde_cliquei.getY() > bt_y and onde_cliquei.getY() < bt2_y:
        return True
    return False


def cria_botao(x1, y1, x2, y2, texto= 'Sair'):
    novo_botao = graphics.Rectangle(graphics.Point(x1,y1), graphics.Point(x2, y2))
    novo_botao.setFill('')
    centro = novo_botao.getCenter()
    text = graphics.Text(centro, texto)
    novo_botao.draw(win)
    text.draw(win)
    return novo_botao 


def aciona_botao(botao, onde_cliquei, password):
    if foi_no_botao(botao, onde_cliquei):
        botao.undraw()
        botao = cria_botao(179, 169, 221, 191)
        sleep(.1)
        botao.undraw()
        botao = cria_botao(180, 170, 220, 190)
        if password == 'Ânimo':
            win.close()


def coleta_senha(win):
    entrada = graphics.Entry(graphics.Point(200,150), 10)
    entrada.setFill('white')
    entrada.draw(win)
    senha = entrada.getText()
    return senha

win = graphics.GraphWin("Senha", 400, 300)
botao = cria_botao(180, 170, 220, 190)

while True:
    senha = coleta_senha(win)
    onde_cliquei = win.getMouse()
    aciona_botao(botao, onde_cliquei, senha)