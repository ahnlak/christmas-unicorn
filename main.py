# main.py - part of the Christmas Unicorn
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

import random, time

import snow

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN

# One time initialisation of the board
gu = GalacticUnicorn()
gfx = PicoGraphics(DISPLAY_GALACTIC_UNICORN)

# Some universal settings
background_pen = gfx.create_pen(0, 0, 0)

# Set up the stuff we use for slowly falling snow
snow_rate = 500
snow_flakes = []

# Now we dive into the main loop; it's a hopefully fairly simple affair
while True:

  # Different things run on different timers; it's messy
  tick_ms = time.ticks_ms()

  ##########
  # UPDATE #
  ##########
  # Run through all our sections, updating as appropriate

  # Snow, run through and update each flake
  for flake in snow_flakes:
    flake.update(tick_ms)

  # Quickly clean up anything that dropped off the bottom
  snow_flakes = [flake for flake in snow_flakes if flake.y <= GalacticUnicorn.HEIGHT]

  # On a random whim, spawn some new ones
  if random.randint(0,snow_rate) == 0:
    snow_flakes.append(snow.Snow(tick_ms))

  print(len(snow_flakes))


  ##########
  # RENDER #
  ##########
  # Render everything, regardless of if we've updated it

  # Clear everything to the background
  gfx.set_pen(background_pen)
  gfx.clear()

  # Snow next
  for flake in snow_flakes:
    flake.render(gfx)

  # Last thing to do is to update the graphics
  gu.update(gfx)
