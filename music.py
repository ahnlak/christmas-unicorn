# music.py - part of the Christmas Unicorn
#
# A lot of this is pretty much taken from Pimoroni's Feature Test samples
# (specifically the timer callback and note beat wrangling)
# 
# Copyright (C) 2022 Pete Favelle <ahnlak@ahnlak.com>
# Released under the MIT License; see LICENSE for details

import machine

import galactic

class Music:

  # Define our tunes in one place...
  tunes = [
    [
      (
        147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 220, 0, 196, 0, 147, 0, 175, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 220, 0, 196, 0, 147, 0, 175, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
        247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 262, 0, 294, 0, 392, 0, 440, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0
      )
    ]
  ]

  # Initialise
  def __init__(self, gu):
    self.playing = False
    self.gu = gu
    self.init_tune(0)
    self.timer = machine.Timer(-1)


  # Initialise a tune, set up the notes and channels
  def init_tune(self, idx):
    # Select the active tune
    self.tune_note = 0
    self.tune_data = Music.tunes[idx]
    self.tune_length = len(Music.tunes[idx][0])

    # Set up the channels for that
    self.channels = [self.gu.synth_channel(i) for i in range(len(self.tune_data))]

    # Hackily init the channel for now (come back to this!)
    self.channels[0].configure(waveforms=galactic.Channel.TRIANGLE + galactic.Channel.SQUARE,
                               attack=0.016,
                               decay=0.168,
                               sustain=0xafff / 65535,
                               release=0.168,
                               volume=10000 / 65535)


  # Callback to handle playing notes
  def next_note(self, timer):

    # Work through each channel
    for idx, channel_data in enumerate(self.tune_data):
      if channel_data[self.tune_note] > 0:
        self.channels[idx].frequency(channel_data[self.tune_note])
        self.channels[idx].trigger_attack()
      elif channel_data[self.tune_note] == -1:
        self.channels[idx].trigger_release()

    self.tune_note = (self.tune_note + 1) % self.tune_length


  # Start playing
  def play(self):
    self.gu.play_synth()
    self.timer.init(freq=10, mode=machine.Timer.PERIODIC, callback=self.next_note)
    #self.channels[0].play_tone(1000, 0.06)
    self.playing = True
    print("playing music")


  # And stop playing
  def stop(self):
    self.timer.deinit()
    self.gu.stop_playing()
    self.playing = False
    print("stop music")


  # Toggle audio on/off, so we don't have to check externally
  def toggle(self):
    if self.playing:
      self.stop()
    else:
      self.play()
