# Importing All The Nessecary Modules
import random

# Important*
# Rock = 1
# Paper = 2
# Scissors = 3

# Creating The Main Game Class
class RockPaperScissors(random.Random):
    def __init__(self):
        # Printing Info Message To Tell The User That The Games At 5Points
        print("The Player Who Reaches 5Points First Wins The Race! ")

        # Variables, Lists
        self.player1_score = 0
        self.player2_score = 0
        self.compplayer_score = 0
        self.comp_score = 0
        self.inputchoice = ["rock", "paper", "scissors"]
        self.chose()

    # Asking The Player Would They Like To Play The Game Or Not
    def chose(self):
        self.choserunning = True
        while self.choserunning:
            self.ask = input("Would You Like To Play The Game(y/n): ").lower()
            if self.ask == "y":
                print("You Chose To Play")
                self.main()
                break

            if self.ask == "n":
                print("You Chose Not To Play")
                quit()

            elif self.ask != "y" or "n":
                print("Invalid Input!")
                continue

    # Checking The Inputs In This Function
    def check(self):
        # Checking If Players Reached 5 points Or Not
        if self.compplayer_score == 5:
            print("Player Reached 5Points, Player Wins The Game :)")
            quit()

        if self.comp_score == 5:
            print("Computer Reached 5Points, Computer Wins The Game :(")
            quit()

        # Checking Cases Of Rock
        if self.userinput2 == "rock" and self.compchosenum == 3:
            print("Player Chosed Rock and Computer Chosed Scissors, Player Gets A Point")
            self.compplayer_score += 1
            return
        elif self.userinput2 == "rock" and self.compchosenum == 1:
            print("Both Chosed Rock Tie!")
            return
        else:
            print("Player Chosed Rock And Computer Chosed Paper, Computer Gets A Point")
            self.comp_score+=1
            return

        # Checking Cases Of Paper
        if self.userinput2 == "paper" and self.compchosenum == 1:
            print("Player Chosed Paper and Computer Chosed Rock, Player Gets A Point")
            self.compplayer_score += 1
            return
        elif self.userinput2 == "paper" and self.compchosenum == 2:
            print("Both Chosed Paper Tie!")
            return
        else:
            print(
                "Player Chosed Paper And Computer Chosed Scissors, Computer Gets A Point")
            self.comp_score+=1
            return

        # Checking Cases Of Scissors
        if self.userinput2 == "scissors" and self.compchosenum == 2:
            print("Player Chosed Scissors and Computer Chosed Paper, Player Gets A Point")
            self.compplayer_score += 1
            return
        elif self.userinput2 == "scissors" and self.compchosenum == 3:
            print("Both Chosed Scissors Tie!")
            return
        else:
            print(
                "Player Chosed Scissors And Computer Chosed Rock, Computer Gets A Point")
            self.comp_score+=1
            return

    # Main Game Function
    def main(self):
        self.running = True
        while self.running:
            self.userinput2 = input("Rock, Paper Or Scissors: ").lower()
            self.compchosenum = self.randint(1, 3)
            if self.userinput2 not in self.inputchoice:
                print("Invalid Choice")
                continue
            self.check()


# Running The Code By Creating An Instance Of The Class
if __name__ == "__main__":
    RockPaperScissors()