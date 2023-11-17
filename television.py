class Television:
    '''
    A class representing a television
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Function to initialize Television class
        :param status: boolean to indicate if the tv is on or off
        :param muted: boolean to indicate if tv is muted/unmuted
        :param volume: int to indicate the volume number the tv is set to
        :param channel: int to indicate the channel number the tv is set to
        '''
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self):
        '''
        Function to switch the Television status to true/false, e.g. turn the tv on/off
        '''
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        '''
        Function to mute/unmute the tv
        '''
        if(self.status):
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self):
        '''
        Function to raise the tv channel by one, or in the case it's on the highest channel, reset it to the lowest
        '''
        if(self.status):
            self.channel = self.channel + 1
            if self.channel > self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL

    def channel_down(self):
        '''
        Function to lower the tv channel by one, or in the case it's on the lowest channel, reset it to the highest
        '''
        if(self.status):
            if (self.channel == self.MIN_CHANNEL):
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1


    def volume_up(self):
        '''
        Function to raise the volume by one, or in the case its the max volume, keep it the same. Can also unmute if muted.
        '''
        if(self.status):
            if(self.muted):
                self.muted = False
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                
    def volume_down(self):
        '''
        Function to lower the volume by one, or in the case its the min volume, keep it the same. Can also unmute if muted.
        '''
        if(self.status):
            if(self.muted):
                self.muted = False
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        '''
        Function to return the description of the Television object
        :return: A string detailing the description of Television
        '''
        return f'Power = [{self.status}], Channel = [{self.channel}], Volume = [{self.volume}]'
