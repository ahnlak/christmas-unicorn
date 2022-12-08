# music.py - part of the Christmas Unicorn
#
# A lot of this is pretty much taken from Pimoroni's Feature Test samples
# (specifically the timer callback and note beat wrangling)
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

class Music:

  # Define our tunes in one place...

  # Initialise
  def __init__(self, gu):
    self.playing = False
    self.tune = 0
    self.gu = gu


  # Start playing
  def play(self):
    self.playing = True
    print("playing music")


  # And stop playing
  def stop(self):
    self.playing = False
    print("stop music")


  # Toggle audio on/off, so we don't have to check externally
  def toggle(self):
    if self.playing:
      self.stop()
    else:
      self.play()
