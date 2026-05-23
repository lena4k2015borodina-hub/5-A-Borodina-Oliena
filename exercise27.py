import turtle

t = turtle.Turtle()

n = int(input("Введіть 3, 4 або 5: "))

if n == 3:
    t.forward(100)
    t.right(120)

    t.forward(100)
    t.right(120)

    t.forward(100)

else:
    if n == 4:
        t.forward(100)
        t.right(90)

        t.forward(100)
        t.right(90)

        t.forward(100)
        t.right(90)

        t.forward(100)

    else:
        if n == 5:
            t.forward(100)
            t.right(72)

            t.forward(100)
            t.right(72)

            t.forward(100)
            t.right(72)

            t.forward(100)
            t.right(72)

            t.forward(100)

        else:
            print("Такої фігури не передбачено")

turtle.done()