# Particle class example used to simulate diffusion of molecules

import simpleguitk as simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
particle_radius = 5
color_list = ["Red", "Green", "Blue", "White"]
direction_list = [[1,0],[0,1],[-1,0],[0,-1]]

# definition of particle class
class Particle:

    # initializer for particles
    def __init__(self, position, color):
        self.position = position
        self.color = color

    # method that updates position of a particle
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]

    # draw method of particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, particle_radius, 1, "Black", self.color)

    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + "and color = " + str(self.color)

# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(direction_list))
    for p in particle_list:
        p.draw(canvas)

# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(500):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(color_list))
    particle_list.append(p)
    print(p)
    print(type(p))

# start frame
frame.start()

