# tree.py - part of the Christmas Unicorn
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

import math, random

from galactic import GalacticUnicorn

class Tree:

  # Class variables defining the general nature of trees
  grow_speed = 2000
  twinkle_speed = 250

  pixels = [
    [( 0, 1, 0)],
    [( 0, 1, 1), 
     ( 0, 2, 0)],
    [( 0, 1, 1), 
     (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), 
     ( 0, 3, 0)],
    [( 0, 1, 1),
     (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0),
     (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), 
     ( 0, 4, 0)]
  ]

  # Initialise
  def __init__(self, tick, gfx):
    # Initialise our location
    self.x = random.randint(0, GalacticUnicorn.WIDTH)
    self.height = 0
    self.age = 0

    # Keep a copy of the graphics object
    self.gfx = gfx

    # And our palette
    self.palette_colours = [
      (10, 150, 10),
      (150, 80, 0)
    ]
    self.update_palette()

    # Set up future timers
    self.grow_next = Tree.grow_speed + tick
    self.twinkle_next = Tree.twinkle_speed + tick


  # Update our palette, based on the defaults and our age
  def update_palette(self):
    self.palette = [ self.gfx.create_pen(*rgbval) for rgbval in self.palette_colours if True ]


  # Update
  def update(self, tick):
    # If we've hit the next growth - and we're not grown - grow more
    if tick > self.grow_next:
      if self.height < len(Tree.pixels)-1:
        self.height += 1
      else:
        self.age += 1
      self.grow_next += Tree.grow_speed

      # Check our age; as we get older, fade our palette
      if self.age > 10:
        print("ageing...")
        self.palette_colours = [ 
          tuple(math.trunc(channel/2) for channel in colour) 
          for colour in self.palette_colours if True
        ]
        self.update_palette()


    # If it's time to twinkle, change our lights
    #if tick > self.twinkle_next:
    #  self.twinkle = random.randint(100, 150)
    #  self.twinkle_next += Snow.twinkle_speed


  # Render
  def render(self):
    # Draw the pixels suitable for this height
    for pixel in Tree.pixels[self.height]:
      self.gfx.set_pen(self.palette[pixel[2]])
      self.gfx.pixel(pixel[0] + self.x, GalacticUnicorn.HEIGHT - pixel[1])
