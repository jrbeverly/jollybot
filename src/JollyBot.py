from pdbot import PDBot

import random

class JollyBot(PDBot):
    '''
    A Prisoners' Dilemma A.I. bot performing an 'Olive Branch' strategy focusing on attempting to cooperate whenever possible.
    '''

    def __init__(self):
        self.take = 'take 1'
        self.take_value = 1

        self.give = 'give 2'
        self.give_value = 2

        self.nice_chance = 0.05
        self.nice_count = 3

        self.init()

    def init(self):
        self.default_play = self.give
        self.o_last_play = self.give
        self.m_last_play = self.give
        self.turn_count = 0

        self.current_trust = 1.0
        self.current_sum = 0.0
        self.opponent_sum = 0.0
        self.current_potential_sum = 0.0
        self.trust_established = False


    def get_play(self):
        '''
        Returns a string denoting the next play that JollyBot will take in the game.

        :return: The next play that JollyBot will take in the game
        :rtype: string
        '''
        result = self.default_play

        self.turn_count = self.turn_count + 1

        if self.turn_count == self.nice_count:
            if self.o_last_play == self.give:
                self.trust_established = True

        if self.turn_count < self.nice_count:
            result = self.give
        elif self.trust_established:
            if self.o_last_play == self.give:
                result = self.give
            else:
                result = self.take
                self.trust_established = False
        elif self.opponent_sum <= self.current_sum:
            result = self.give
        elif self.opponent_sum > self.current_sum:
            if random.random() < self.nice_chance:
                result = self.give
            else:
                result = self.take
        else:
            result = self.give

        if result == self.take:
            self.current_sum += self.take_value
        else:
            self.opponent_sum += self.give_value

        self.current_potential_sum = self.take_value
        self.m_last_play = result

        return result

    def make_play(self, opponent_play):
        '''
        Notify Jollybot of the opponent's last play in the game.

        :param str sender: The person sending the message
        :return: None
        :raises ValueError: if the opponent_play is not a valid play
        '''
        if (opponent_play not in [self.take, self.give]):
            raise ValueError('The opponent did not play one of the valid options.')

        self.o_last_play = opponent_play
        self.current_potential_sum = self.give_value

        if opponent_play == self.give:
            self.current_sum = self.current_sum + self.give_value
        else:
            self.opponent_sum = self.opponent_sum + self.take_value

        return
