from pdbot import PDBot

import random

static_cooperate = "give 2"
static_defect = "take 1"
olive_branch = 0.4


class JollyBot(PDBot):
    '''
    A Prisoners' Dilemma A.I. bot performing an 'Olive Branch' strategy focusing on attempting to cooperate whenever possible.
    '''

    def __init__(self):
        self.init()

    def init(self):
        self.other_last_play = static_cooperate
        self.current_play = 1

    def get_play(self):
        '''
        Returns a string denoting the next play that JollyBot will take in the game.

        :return: The next play that JollyBot will take in the game
        :rtype: string
        '''
        if (self.current_play <= 3):
            myplay = static_cooperate
        elif self.other_last_play == static_cooperate:
            myplay = static_cooperate
        else:
            if random.random() < olive_branch:
                myplay = static_cooperate
            else:
                myplay = static_defect

        self.my_last_play = myplay
        self.current_play += 1
        return myplay

    def make_play(self, opponent_play):
        '''
        Notify Jollybot of the opponent's last play in the game.

        :param str sender: The person sending the message
        :return: None
        :raises ValueError: if the opponent_play is not a valid play
        '''
        if (opponent_play not in [static_cooperate, static_defect]):
            raise ValueError(
                'The opponent did not play one of the valid options.')

        self.other_last_play = opponent_play
        return
