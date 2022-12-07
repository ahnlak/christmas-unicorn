# main.py - part of the Christmas Unicorn
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

import random, time

import snow, tree

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN

# One time initialisation of the board
gu = GalacticUnicorn()
gfx = PicoGraphics(DISPLAY_GALACTIC_UNICORN)

# Some universal settings
background_pen = gfx.create_pen(0, 0, 0)

# Set up the stuff we use for our various sections
snow_rate_front = 500
snow_flakes_front = []
snow_rate_rear = 500
snow_flakes_rear = []

tree_rate = 500
trees = []

# Brightness handling
gu.set_brightness(0.5)
last_bright = 0


# Now we dive into the main loop; it's a hopefully fairly simple affair
while True:

  # Different things run on different timers; it's messy
  tick_ms = time.ticks_ms()

  ######
  # UI #
  ######
  # Check for buttons being pressed; brightness first
  if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
    if tick_ms > last_bright + 200:
      gu.adjust_brightness(0.1)
      last_bright = tick_ms
  if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
    if tick_ms > last_bright + 200:
      gu.adjust_brightness(-0.1)
      last_bright = tick_ms


  ##########
  # UPDATE #
  ##########
  # Run through all our sections, updating as appropriate

  # Snow, run through and update each flake
  for flake in snow_flakes_front:
    flake.update(tick_ms)
  for flake in snow_flakes_rear:
    flake.update(tick_ms)

  # Quickly clean up anything that dropped off the bottom
  snow_flakes_front = [flake for flake in snow_flakes_front if flake.y <= GalacticUnicorn.HEIGHT]
  snow_flakes_rear = [flake for flake in snow_flakes_rear if flake.y <= GalacticUnicorn.HEIGHT]

  # On a random whim, spawn some new ones
  if random.randint(0,snow_rate_front) == 0:
    snow_flakes_front.append(snow.Snow(tick_ms, gfx))
  if random.randint(0,snow_rate_rear) == 0:
    snow_flakes_rear.append(snow.Snow(tick_ms, gfx))


  # Trees, follow a very similar process
  for branch in trees:
    branch.update(tick_ms)

  # And any trees that are too old, remove
  trees = [branch for branch in trees if branch.age < 16]

  # And spawn new trees every now and then
  if random.randint(0,tree_rate) == 0:
    trees.append(tree.Tree(tick_ms, gfx))

  print(len(trees))


  ##########
  # RENDER #
  ##########
  # Render everything, regardless of if we've updated it

  # Clear everything to the background
  gfx.set_pen(background_pen)
  gfx.clear()

  # Rear snow, to be covered by other things
  for flake in snow_flakes_rear:
    flake.render()

  # Trees
  for branch in trees:
    branch.render()

  # Front snow, which appears in front of everything else
  for flake in snow_flakes_front:
    flake.render()

  # Last thing to do is to update the graphics
  gu.update(gfx)

  # From examples: pause for a moment (important or the USB may fail)
  time.sleep(0.001)