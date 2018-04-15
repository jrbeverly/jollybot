'''
A base class for a Prisoners' Dilemma A.I. bot.
'''
from abc import ABCMeta, abstractmethod


class PDBot:
    __metaclass__ = ABCMeta

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def get_play(self):
        pass

    @abstractmethod
    def make_play(self, opponent_play):
        pass
