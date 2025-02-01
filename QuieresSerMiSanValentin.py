import turtle
import random

# Config pantalla
screen = turtle.Screen()
screen.setup(width=350, height=600)  #MEDIDAS DE MOVIL
screen.bgcolor("black")
screen.title("San Valentín 💖")
screen.tracer(0)

# Mensaje principal
name = "Nombre"  # Nombre a salir en pantalla
msg = turtle.Turtle()
msg.color("white")
msg.hideturtle()
msg.penup()
msg.goto(0, 220)
msg.write(f"¿Quieres ser mi San Valentín, {name}? ", align="center", font=("Arial", 12, "bold"))

# Corazones flotando
hearts = []
for _ in range(500):
    heart = turtle.Turtle()
    heart.shape("circle")
    heart.color(random.choice(["red", "pink"]))
    heart.penup()
    heart.goto(random.randint(-540, 540), random.randint(-1600, -300))
    heart.dy = random.uniform(0.5, 1.5)
    hearts.append(heart)

# Animación de corazones subiendo
def animate_hearts():
    for heart in hearts:
        y = heart.ycor() + heart.dy
        if y > 300:
            y = random.randint(-300, -100)
            heart.goto(random.randint(-140, 140), y)
        else:
            heart.sety(y)
    screen.update()
    screen.ontimer(animate_hearts, 50)

# Botón Sí
yes_btn = turtle.Turtle()
yes_btn.shape("square")
yes_btn.color("green")
yes_btn.shapesize(2, 5)
yes_btn.penup()
yes_btn.goto(-60, -200)
yes_btn.write("Si", align="center", font=("Arial", 30, "bold"))
yes_btn.onclick(lambda x, y: say_yes())

# Botón No
no_btn = turtle.Turtle()
no_btn.shape("square")
no_btn.color("red")
no_btn.shapesize(2, 5)
no_btn.penup()
no_btn.goto(60, -200)
no_btn.write("No", align="center", font=("Arial", 14, "bold"))
no_btn.onclick(lambda x, y: move_no())

# Función cuando dice sí
def say_yes():
    screen.clear()
    screen.bgcolor("pink")
    
    # Añadir flor morada animada
    flower = turtle.Turtle()
    flower.color("purple")
    flower.speed(0)
    flower.hideturtle()
    flower.penup()
    flower.goto(0, -300)
    flower.pendown()
    for i in range(46):
        for _ in range(2):
            flower.circle(300, 60)
            flower.left(120)
        flower.left(10)
    
    # Animación de la flor moviéndose
    def move_flower():
        flower.sety(flower.ycor() + 5)  # Mueve la flor hacia arriba
        if flower.ycor() > 100:
            flower.goto(0, -150)  # Resetea la flor cuando sube mucho
        screen.ontimer(move_flower, 50)

    move_flower()

    msg = turtle.Turtle()
    msg.color("red")
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 0)
    msg.write("¡Será el mejor día de tu vida!", align="center", font=("Arial", 14, "bold"));
	

# Función cuando dice no (se mueve)
def move_no():
    no_btn.goto(random.randint(-100, 100), random.randint(-250, -150))

# Iniciar animación
animate_hearts()

# Mantener pantalla activa
turtle.done()