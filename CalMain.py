Card_Value = []
class Calculation:
    def __init__(self, value_dic):
        self.value_dic = value_dic

    def main_cal(self):
        global Card_Value
        # for each individual players
        for init_value in self.value_dic:
            # for each card of individual player
            temp_list = self.value_dic[init_value]
            for card in temp_list:
                print(self.value_dic[init_value][card])
                Card_Value = self.value_dic[init_value][card]
                print(init_value[card][Card_Value])
