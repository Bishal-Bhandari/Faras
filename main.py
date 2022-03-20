import random
from CalMain import Calculation

Card_Color = ["Red", "Black"]
Card_Shape = ["Hearts", "Diamonds", "Clubs", "Spades"]
Card_Turn = ["First", "Second", "Third"]
Card_Deck = 52
Players_Name = []
check_card_list = []
prim_dict = {}


# for card calculation
class CalcCard:
    def __init__(self, num_of_players):
        self.num_of_players = num_of_players

    def name_players(self):
        for players in range(1, self.num_of_players + 1, 1):
            print(f"\nPlease enter the name for player {players}")
            players = str(input("Game name:  "))
            Players_Name.append(players)
        self.value_assign(Players_Name)

    def value_assign(self, players_name):
        for name in players_name:
            sec_dict = {}
            for turn in Card_Turn:
                sec_list = []
                self.feature_card(sec_list, check_card_list)
                for check_key in check_card_list[:-1]:
                    if check_key == sec_list:
                        sec_list = []
                        self.feature_card(sec_list, check_card_list)
                sec_dict[turn] = sec_list
            prim_dict[name] = sec_dict.copy()
        calculations = Calculation(prim_dict)
        calculations.main_cal()

    def feature_card(self, sec_list, check_card_list):
        sec_list.append(random.choice(Card_Color))
        if sec_list[0] == Card_Color[0]:
            rand_num = random.randint(0, 1)
            sec_list.append(Card_Shape[rand_num])
        else:
            rand_num = random.randint(2, 3)
            sec_list.append(Card_Shape[rand_num])
        sec_list.append(random.randint(1, 13))
        # to check if program doesnt generate same card again
        check_card_list.append(sec_list)
        return sec_list, check_card_list


# MAIN FUNCTION
def main():
    print("\nWELCOME TO 3 CARDS GAME.")
    try:
        number_of_players = int(input("\nEnter the number of players: "))
        # make sure cards are sufficient for all players
        if 2 <= number_of_players <= int(17):
            calculation = CalcCard(number_of_players)
            calculation.name_players()
        else:
            print("\nPlease this game is only for players between 2 to 17.\n Thank You!!!")
    except ValueError:
        print("\nPlease enter valid number of player.")


main()
