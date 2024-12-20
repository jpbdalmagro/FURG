import AED1.AULAS.aula1220.graphics as gf

def main():
    win = gf.GraphWin("My Window", 900, 600)
    c = gf.Circle(gf.Point(450, 300), 150)
    c.setFill("darkblue")
    c.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
