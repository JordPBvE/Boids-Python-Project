import copy
import random
import pygame
from pygame import Color
from pygame.math import Vector2

class Boid:
  def __init__(self, 
                pos=Vector2(0, 0),
                size=16,
                velocity=Vector2(1,1),
                color=Color(255,255,255)): # window as input aswell??
    self.pos = pos
    self.size = size
    self.velocity = velocity
    self.color = color
    # self.time = random.random(0.0, 10000) # perlin noise for angle noise?


  def draw(self, surface):
    # draw boid with pygame
    s = self.size * self.velocity.normalize() # use the normalized velocity vector to draw the head
    head = self.pos + s
    # makes a copy of s rotated 90 degrees to the right
    # deepcopy is used to prevent unintended changes to s
    s_right = copy.deepcopy(s) 
    s_right.x, s_right.y = s_right.y, -s_right.x 
    foot_1 = self.pos - s + 0.5 * s_right
    # same thing, but rotated 90 degrees to the left
    s_left = copy.deepcopy(s)
    s_left.x , s_left.y = -s_left.y, s_left.x 
    foot_2 = self.pos - s + 0.5 * s_left
    pygame.draw.polygon(surface, self.color, (head, foot_1, foot_2))

  def do_step(self, dt):
    self.pos = self.pos + dt * self.velocity
    self.pos.x = self.pos.x % 512
    self.pos.y = self.pos.y % 512

  def changeVelocity(self, boidArray):
      # self.angle += perlin(self.time)
      v1 = rule1(self, boidArray)
      v2 = rule2(self, boidArray)
      v3 = rule3(self, boidArray)

      self.velocity = self.velocity + v1 + v2 + v3

  def rule1():
      print("") 
  def rule2():
      print("")
  def rule3():
      print("")


### time input for noise function
  # def timeChange(self):
  #   self.time += 1

  # def move(self):



