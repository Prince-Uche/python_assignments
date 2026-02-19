MIN_VOLUME = 0
MAX_VOLUME = 10
MAX_CHANNEL = 100
MIN_CHANNEL = 1

class Television:
    def __init__(self):
        self.__tv_state = False
        self.__volume = 0
        self.__channel = 1

    def get_state(self):
        return self.__tv_state

    def set_is_on(self):
        self.__tv_state = True

    def set_is_off(self):
        self.__tv_state = False

    def increase_tv_volume(self):
        if not self.__volume > MAX_VOLUME:
            self.__volume += 1
        self.__volume = MAX_VOLUME


    def decrease_tv_volume(self):
        if not self.__volume < MIN_VOLUME:
            self.__volume -= 1
        self.__volume = MIN_VOLUME

    def get_tv_volume(self):
        return self.__volume

    def increase_channel(self):
        self.__channel += 1

    def decrease_channel(self):
        self.__channel -= 1

    def get_channel(self):
        return self.__channel
