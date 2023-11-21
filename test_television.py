from television import *
import pytest

class Test:
    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):#Fixed
        assert self.t1._Television__status == False
        assert self.t1._Television__muted == False
        assert self.t1._Television__volume == self.t1.MIN_VOLUME
        assert self.t1._Television__channel == self.t1.MIN_CHANNEL

    def test_power(self):#Fixed
        self.t1.power()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        assert (self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)

    def test_mute(self): #Fixed
        self.t1.mute()
        assert (not self.t1._Television__muted, self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        self.t1.mute()
        assert (self.t1._Television__muted, self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.mute()
        assert (not self.t1._Television__muted, self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
    def test_channel_up(self):
        self.t1.channel_up()
        assert (self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.channel_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 1,  self.t1._Television__volume == 0)
        self.t1.channel_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 2,  self.t1._Television__volume == 0)
        self.t1.channel_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 3,  self.t1._Television__volume == 0)
        self.t1.channel_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)

    def test_channel_down(self):
        self.t1.channel_down()
        assert (self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.channel_down()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 3,  self.t1._Television__volume == 0)
        self.t1.channel_down()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 2,  self.t1._Television__volume == 0)
        self.t1.channel_down()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 1,  self.t1._Television__volume == 0)
        self.t1.channel_down()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)

    def test_volume_up(self):
        self.t1.volume_up()
        assert (self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.volume_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 1)
        self.t1.volume_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 2)
        self.t1.volume_up()
        assert (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 2)

    def test_volume_down(self):
        self.t1.volume_down()
        (self.t1._Television__status == False, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.power()
        (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)
        self.t1.volume_down()
        (self.t1._Television__status == True, self.t1._Television__channel == 0,  self.t1._Television__volume == 0)

    def test_str(self):
        test_str = self.t1.__str__()
        assert test_str == 'Power = False, Channel = 0, Volume = 0'
