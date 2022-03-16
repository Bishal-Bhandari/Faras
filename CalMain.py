class Calculation:
    def __init__(self, value_dic):
        self.value_dic = value_dic

    def main_cal(self):
        # for each players
        for init_value in self.value_dic:
            # print(f"this {self.value_dic}")
            # print(self.value_dic[init_value])
            # for each card of individual player
            temp_list = self.value_dic[init_value]
            for card in temp_list:
                # print(type(temp_list))
                # print(temp_list[card])
                # for each cards number, color, suit of individual card
                temp_feature = temp_list[card]
                # for feature in range(len(temp_feature)):
                #     print("H")
