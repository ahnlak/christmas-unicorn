# snow.py - part of the Christmas Unicorn
#
# Snowflakes that twinkle, fall and drift out of sight...
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

import random

from galactic import GalacticUnicorn

class Snow:

  # Class variables defining the general nature of snow
  fall_speed = 600
  twinkle_speed = 50

  # Initialise
  def __init__(self, tick, gfx):
    self.x = random.randint(0, GalacticUnicorn.WIDTH)
    self.y = 0
    self.twinkle_pen = gfx.create_pen(200, 200, 200)
    self.gfx = gfx

    self.fall_next = Snow.fall_speed + tick
    self.twinkle_next = Snow.twinkle_speed + tick

  # Update
  def update(self, tick):
    # If we've hit the next fall, move down
    if tick > self.fall_next:
      self.y += 1
      self.fall_next += Snow.fall_speed

    # If it's time to twinkle, vary our brightness
    if tick > self.twinkle_next:
      self.twinkle = random.randint(100, 150)
      self.twinkle_pen = self.gfx.create_pen(self.twinkle, self.twinkle, self.twinkle)
      self.twinkle_next += Snow.twinkle_speed

  # Render
  def render(self):
    # Just draw a single, white, twinkling pixel
    self.gfx.set_pen(self.twinkle_pen)
    self.gfx.pixel(self.x, self.y)
