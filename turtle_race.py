import turtle
import random 
import time

WEIDTH,HEIGHT =500,500
COLORS = ['red','green','blue','black','purple','pink','brown','cyan','orange','yellow']

screen = turtle.Screen()
screen.setup(WEIDTH,HEIGHT)
screen.title('my turtol racing')




def get_number_of_racing_turtol():
    racers = 0 
    while True:
        racers = turtle.textinput("racer input",'enter number of racers (2 - 10)')
        if racers.isdigit():
            racers = int(racers)
        else:
            turtle.color("red")
            turtle.write("Please Eneter Valid Input in Numeric.....",align="center", font=('Arial', 20, 'normal'),move=True)
            
            time.sleep(2)
            turtle.clearscreen()
            continue
            
        if 2 <= racers <= 10:
            return racers
        else:
            turtle.color("red")
            turtle.write("Please Enter number in range 2 to 10 ",align="center", font=('Arial', 20, 'normal'),move=True)
            time.sleep(3)
            turtle.clearscreen()
            

def race(colors):
    turtles = create_turtols(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,25)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT//2 -20:
                return colors[turtles.index(racer)]




def create_turtols(colors):
    turtles = []
    spacing = WEIDTH // (len(colors) + 1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        # seting at starting position
        racer.setpos(-WEIDTH //2 + (i +1) * spacing , -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)

    return turtles



def show_winner(winer):
    turtle.clearscreen()
    turtle.color(winer)
    turtle.write(f"the winner is turtol color {winer}",align="center", font=('Arial', 25, 'normal'),move=True)


def turtol_screen():
    screen = turtle.Screen()
    screen.setup(WEIDTH,HEIGHT)
    screen.title('my turtle racing')


def main():
    racers = get_number_of_racing_turtol()
    turtol_screen()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    show_winner(winner)
    time.sleep(5)
    turtle.bye()


main()
