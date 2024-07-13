import argparse
import turtle

def koch_curve(t, order, size, colors):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3, colors)
            t.left(angle)
            t.color(colors[(order - 1) % len(colors)])

def draw_koch_snowflake(order, size=300, background_color="black"):
    colors = ["cyan", "magenta", "yellow", "lime", "white"]
    window = turtle.Screen()
    window.bgcolor(background_color)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    t.color(colors[order % len(colors)])

    for _ in range(3):
        koch_curve(t, order, size, colors)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw a Koch snowflake with specified recursion level.")
    parser.add_argument("order", type=int, help="The recursion level of the Koch snowflake")
    parser.add_argument("--size", type=int, default=300, help="The size of the Koch snowflake")
    parser.add_argument("--background_color", type=str, default="black", help="Background color of the window")

    args = parser.parse_args()

    draw_koch_snowflake(args.order, args.size, args.background_color)
