import turtle
t = turtle.Turtle()
t.shape("turtle")

x_list = [ ]
y_list = [ ]

x1 = int(input("x1 : "))
x_list.append(x1)
y1 = int(input("y1 : "))
y_list.append(y1)

x2 = int(input("x2 : "))
x_list.append(x2)
y2 = int(input("y2 : "))
y_list.append(y2)

x3 = int(input("x3 : "))
x_list.append(x3)
y3 = int(input("y3 : "))
y_list.append(y3)

t.goto(x_list[0], y_list[0])
t.goto(x_list[1], y_list[1])
t.goto(x_list[2], y_list[2])