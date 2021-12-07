import psp2d

controls = \
{
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
    "cross": 0,
    "circle": 0,
    "square": 0,
    "triangle": 0,
    "l": 0,
    "r": 0,
    "start": 0,
    "select": 0,
    "analogX": 0,
    "analogY": 0,
}

w = 480
h = 272
font = psp2d.Font("font.png")
image = psp2d.Image(w, h)
screen = psp2d.Screen()
blank = psp2d.Color(0, 0, 0)
origin = 0

def blank_screen(r = 30, g = 0, b = 255):
    global screen, blank
    blank = psp2d.Color(r, g, b)
    image.clear(blank)
    screen.blit(image)
    screen.swap()

def draw_text(message):
    global origin, image, screen
    font.drawText(image, 0, origin, "[INFO]: " + message)
    screen.blit(image)
    screen.swap()
    origin += 30

def update_controls():
    pad = psp2d.Controller()
    for control in controls.keys():
        controls[control] = getattr(pad, control)

blank_screen()
draw_text("Hello World")
draw_text("Press Cross to Exit")

running = True
while running:
    update_controls()
    if controls["cross"]:
        draw_text("Restarting...")
        running = False
