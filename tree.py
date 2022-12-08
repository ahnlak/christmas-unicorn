# tree.py - part of the Christmas Unicorn
#
# A tree that knows how to grow, to twinkle, and to fade with age.
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
     ( 0, 4, 0)],
    [( 0, 1, 1),
     (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0),
     (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), 
     (-1, 4, 0), ( 0, 4, 0), ( 1, 4, 0), 
     ( 0, 5, 0)],
    [( 0, 1, 1),
     (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0),
     (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), 
     (-2, 4, 0), (-1, 4, 0), ( 0, 4, 0), ( 1, 4, 0), ( 2, 4, 0),
     (-1, 5, 0), ( 0, 5, 0), ( 1, 5, 0), 
     ( 0, 6, 0)],
    [( 0, 1, 1),
     (-3, 2, 0), (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0), ( 3, 2, 0),
     (-2, 3, 0), (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), ( 2, 3, 0),
     (-1, 4, 0), ( 0, 4, 0), ( 1, 4, 0), 
     (-2, 5, 0), (-1, 5, 0), ( 0, 5, 0), ( 1, 5, 0), ( 2, 5, 0),
     (-1, 6, 0), ( 0, 6, 0), ( 1, 6, 0), 
     ( 0, 7, 0)],
    [( 0, 1, 1),
     (-3, 2, 0), (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0), ( 3, 2, 0),
     (-2, 3, 0), (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), ( 2, 3, 0),
     (-1, 4, 0), ( 0, 4, 0), ( 1, 4, 0), 
     (-3, 5, 0), (-2, 5, 0), (-1, 5, 0), ( 0, 5, 0), ( 1, 5, 0), ( 2, 5, 0), ( 3, 5, 0),
     (-2, 6, 0), (-1, 6, 0), ( 0, 6, 0), ( 1, 6, 0), ( 2, 6, 0),
     (-1, 7, 0), ( 0, 7, 0), ( 1, 7, 0), 
     ( 0, 8, 0)],
    [( 0, 1, 1),
     (-4, 2, 0), (-3, 2, 0), (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0), ( 3, 2, 0), ( 4, 2, 0),
     (-3, 3, 0), (-2, 3, 0), (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 0), ( 2, 3, 0), ( 3, 3, 0),
     (-2, 4, 0), (-1, 4, 0), ( 0, 4, 0), ( 1, 4, 0), ( 2, 4, 0),
     (-1, 5, 0), ( 0, 5, 0), ( 1, 5, 0), 
     (-3, 6, 0), (-2, 6, 0), (-1, 6, 0), ( 0, 6, 0), ( 1, 6, 0), ( 2, 6, 0), ( 3, 6, 0),
     (-2, 7, 0), (-1, 7, 0), ( 0, 7, 0), ( 1, 7, 0), ( 2, 7, 0),
     (-1, 8, 0), ( 0, 8, 0), ( 1, 8, 0), 
     ( 0, 9, 0)],
    [( 0, 1, 1),
     (-4, 2, 0), (-3, 2, 6), (-2, 2, 0), (-1, 2, 0), ( 0, 2, 0), ( 1, 2, 0), ( 2, 2, 0), ( 3, 2, 4), ( 4, 2, 0),
     (-3, 3, 0), (-2, 3, 4), (-1, 3, 0), ( 0, 3, 0), ( 1, 3, 6), ( 2, 3, 0), ( 3, 3, 0),
     (-2, 4, 0), (-1, 4, 0), ( 0, 4, 6), ( 1, 4, 4), ( 2, 4, 0),
     (-1, 5, 0), ( 0, 5, 4), ( 1, 5, 0), 
     (-3, 6, 0), (-2, 6, 6), (-1, 6, 0), ( 0, 6, 0), ( 1, 6, 0), ( 2, 6, 4), ( 3, 6, 0),
     (-2, 7, 0), (-1, 7, 4), ( 0, 7, 0), ( 1, 7, 6), ( 2, 7, 0),
     (-1, 8, 0), ( 0, 8, 6), ( 1, 8, 0), 
     ( 0, 9, 0),
     ( 0,10, 2)]
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
      (150, 80, 0),
      (180, 180, 180),
      (120, 120, 120),
      (180, 0, 0),
      (10, 150, 10),
      (10, 150, 10),
      (0, 0, 180)
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
        self.palette_colours = [ 
          tuple(math.trunc(channel/2) for channel in colour) 
          for colour in self.palette_colours if True
        ]
        self.update_palette()


    # If it's time to twinkle, change our lights
    if tick > self.twinkle_next:
      # Sight cheat here; we just swap a couple of palette entries
      self.palette_colours[2], self.palette_colours[3] = self.palette_colours[3], self.palette_colours[2]
      self.palette_colours[4], self.palette_colours[5] = self.palette_colours[5], self.palette_colours[4]
      self.palette_colours[6], self.palette_colours[7] = self.palette_colours[7], self.palette_colours[6]
      self.twinkle_next += Tree.twinkle_speed
      self.update_palette()


  # Render
  def render(self):
    # Draw the pixels suitable for this height
    for pixel in Tree.pixels[self.height]:
      self.gfx.set_pen(self.palette[pixel[2]])
      self.gfx.pixel(pixel[0] + self.x, GalacticUnicorn.HEIGHT - pixel[1])
