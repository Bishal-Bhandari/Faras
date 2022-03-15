import random

Card_Color = ["Red", "Black"]
Card_Shape = ["Hearts", "Diamonds", "Clubs", "Spades"]
Card_Deck = 52
Players_Name = []


# for card calculation
class CalcCard:
    def __init__(self, num_of_players):
        self.num_of_players = num_of_players

    def name_players(self):
        for players in range(1, self.num_of_players + 1, 1):
            print(f"Please enter the name for player {players}")
            players = str(input("Game name:  "))
            Players_Name.append(players)
        self.main_cal(Players_Name)

    def main_cal(self, players_name):
        sec_list = []
        prim_list = []
        # for x in range(len(players_name)):
        #



def main():
    print("\nWELCOME TO 3 CARDS GAME.")
    number_of_players = int(input("\nEnter the number of players: "))
    # make sure cards are sufficient for all players
    if number_of_players <= int(17):
        calculation = CalcCard(number_of_players)
        calculation.name_players()
    else:
        print("\nPlease this game is only for player less than 17.\n Thank You!!!")


main()
