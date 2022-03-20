priority = []


class Calculation:
    def __init__(self, value_dic):
        self.value_dic = value_dic

    def main_cal(self):
        # for each individual players
        for init_value in self.value_dic:
            # for each card of individual player
            temp_list = self.value_dic[init_value]
            # for number of first, second and third card
            one_num_card = temp_list["First"][2]
            two_num_card = temp_list["Second"][2]
            three_num_card = temp_list["Third"][2]
            # for shape of first, second and third card
            one_shape_card = temp_list["First"][1]
            two_shape_card = temp_list["Second"][1]
            three_shape_card = temp_list["Third"][1]

            if one_num_card == two_num_card and two_num_card == three_num_card:
                print("Trial")
                priority[init_value] = 1
