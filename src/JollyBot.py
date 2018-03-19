from pdbot import PDBot

import random

static_cooperate = "give 2"
static_defect = "take 1"
olive_branch = 0.4

class JollyBot(PDBot):

    def __init__(self):
        self.init()

    def init(self):
        self.other_last_play=static_cooperate
        self.current_play=1

    #get_play is a function that takes no arguments
    #and returns one of the two strings "give 2" or "take 1"
    #denoting the next play your agent will take in the game
    def get_play(self):
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

    #make_play is a function that takes a single string argument
    #that is either "give 2" or "take 1" denoting the opponent's
    #last play in the game
    def make_play(self,opponent_play):
        self.other_last_play = opponent_play
        return

if __name__ == "__main__":


    pd_agent = JollyBot()

    done = False
    iteration = 1
    maxiterations = 15
    agent_score = 0
    client_score = 0
    while iteration < maxiterations and not done:
        print(100 * "*")
        print ("game "+str(iteration)+": JollyBot is thinking ...")
        agent_action = pd_agent.get_play()

        client_action = input("your action (give 2 or take 1, anything else stops play): ")

        print ("JollyBot's action is to: ",agent_action)


        if client_action == "give 2" or client_action == "take 1":
            pd_agent.make_play(client_action)
        else:
            print ("The game has ended")
            done = True

        if client_action == "give 2":
            agent_score += 2
        if agent_action == "give 2":
            client_score += 2
        if agent_action == "take 1":
            agent_score += 1
        if client_action == "take 1":
            client_score += 1

        print ("your score:    ",client_score," -:",client_score*"*")
        print ("pd-bots score: ",agent_score," -:",agent_score*"*")

        iteration += 1
