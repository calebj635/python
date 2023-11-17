from television import *
import pytest

class Test:
    def setup(self):#initializing television object
        self.t1 = Television()

    def teardown(self):
        del self.t1

    def test_init(self):#Testing __init__
        assert self.t1.status == False
        assert self.t1.muted == False
        assert self.t1.volume == self.t1.MIN_VOLUME
        assert self.t1.channel == self.t1.MIN_CHANNEL

    def test_power(self):#testing power()
        self.t1.power()
        assert self.t1.status == True
        self.t1.power()
        assert self.t1.status == False

    def test_mute(self):#testing mute()
        self.t1.mute()
        assert self.t1.muted == False#testing mute() does nothing if status is False
        self.t1.power()
        self.t1.mute()
        assert self.t1.muted == True#testing muted switched to true(if false) if status is true
        self.t1.mute()
        assert self.t1.muted == False#testing muted switches back to false if already true

    def test_channel_up(self):
        self.t1.channel_up()
        assert self.t1.channel == 0
        self.t1.power()
        assert self.t1.channel == 0
        self.t1.channel_up()
        assert self.t1.channel == 1
        self.t1.channel_up()
        assert self.t1.channel == 2
        self.t1.channel_up()
        assert self.t1.channel == 3
        self.t1.channel_up()
        assert self.t1.channel == 0

    def test_channel_down(self):
        self.t1.channel_down()
        assert self.t1.channel == 0
        self.t1.power()
        assert self.t1.channel == 0
        self.t1.channel_down()
        assert self.t1.channel == 3
        self.t1.channel_down()
        assert self.t1.channel == 2
        self.t1.channel_down()
        assert self.t1.channel == 1
        self.t1.channel_down()
        assert self.t1.channel == 0

    def test_volume_up(self):
        self.t1.volume_up()
        assert self.t1.volume == 0
        self.t1.power()
        assert self.t1.volume == 0
        self.t1.volume_up()
        assert self.t1.volume == 1
        self.t1.volume_up()
        assert self.t1.volume == 2
        self.t1.volume_up()
        assert self.t1.volume == 2

    def test_volume_down(self):
        self.t1.volume_down()
        assert self.t1.volume == 0
        self.t1.power()
        assert self.t1.volume == 0
        self.t1.volume_down()
        assert self.t1.volume == 0

    def test_str(self):
        testStr = self.t1.__str__()
        assert testStr == 'Power = [False], Channel = [0], Volume = [0]'