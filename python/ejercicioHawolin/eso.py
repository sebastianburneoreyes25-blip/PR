import turtle
import math

# --- Funciones Auxiliares ---

def ir_a(t, x, y):
    """Mueve la tortuga a una posición sin dibujar."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def dibujar_circulo(t, radio, color_relleno, color_borde):
    """Dibuja un círculo relleno."""
    t.color(color_borde, color_relleno)
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

def dibujar_triangulo(t, base, altura, color):
    """Dibuja un triángulo relleno (ojo o nariz) en la posición actual."""
    t.color("black", color)
    t.begin_fill()
    
    # Dibuja la base
    t.forward(base)
    # Gira para la altura y dibuja (calculando el ángulo para un triángulo isósceles)
    angulo = math.degrees(math.atan(2 * altura / base))
    t.left(180 - angulo)
    lado = math.sqrt((base/2)**2 + altura**2)
    t.forward(lado)
    
    # Gira para cerrar el triángulo
    t.left(2 * angulo)
    t.forward(lado)

    t.end_fill()
    # Corrige orientación de la tortuga para futuras operaciones
    t.setheading(0)

# -----------------------------
# --- FUNCIÓN PRINCIPAL DE DIBUJO ---
# -----------------------------

def dibujar_calabaza_halloween():
    """
    Configura el entorno de Turtle y dibuja una calabaza de Halloween completa.
    """
    
    # Configuración de la Ventana
    ventana = turtle.Screen()
    ventana.setup(width=600, height=600)
    ventana.bgcolor("black") 
    ventana.title("¡Calabaza de Halloween con Python!")

    # Inicializar la tortuga para el dibujo
    t = turtle.Turtle()
    t.speed(0) # Máxima velocidad de dibujo
    t.hideturtle()
    
    # --- Parámetros de la Calabaza ---
    radio_calabaza = 150
    color_luz = "yellow"
    
    # 1. Dibujar el Cuerpo Naranja de la Calabaza
    ir_a(t, 0, -radio_calabaza) 
    dibujar_circulo(t, radio_calabaza, "orange", "darkorange")

    # 2. Dibujar el Tallo Verde
    tamanio_tallo = 40
    ir_a(t, -15, radio_calabaza)
    t.color("green", "darkgreen")
    t.begin_fill()
    t.setheading(90) # Orientación hacia arriba
    for _ in range(2):
        t.forward(tamanio_tallo)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()
    t.setheading(0) # Restablecer

    # 3. Dibujar Ojos (Triángulos)
    base_ojo = 40
    altura_ojo = 60

    # Ojo Izquierdo
    ir_a(t, -50, 50)
    dibujar_triangulo(t, base_ojo, altura_ojo, color_luz)

    # Ojo Derecho
    ir_a(t, 10, 50)
    dibujar_triangulo(t, base_ojo, altura_ojo, color_luz)

    # 4. Dibujar la Nariz (Triángulo pequeño)
    base_nariz = 20
    altura_nariz = 20
    ir_a(t, -10, 10)
    dibujar_triangulo(t, base_nariz, altura_nariz, color_luz)

    # 5. Dibujar la Boca Dentada
    ir_a(t, -60, -50)
    t.color("black", color_luz)
    t.begin_fill()
    t.setheading(0) # Orientación horizontal

    # Dibuja la línea y luego los dientes (simplificado)
    t.forward(120) 
    t.right(90)
    t.forward(10) # Altura del diente
    t.left(135)
    t.forward(math.sqrt(2) * 10)
    t.right(90)
    t.forward(math.sqrt(2) * 10)
    t.left(135)
    t.forward(10) 

    t.left(90)
    t.forward(120)

    t.end_fill()

    # Mantener la ventana abierta
    ventana.mainloop()

# ------------------------------------

# Ejemplo de cómo se usaría en tu main.py:
# if __name__ == "__main__":
#     dibujar_calabaza_halloween()