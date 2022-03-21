import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import openpyxl

Player_Value = []
color_value = []


class Calculation:
    def __init__(self, value_dic):
        self.value_dic = value_dic

    def main_cal(self):
        global color_value
        # for each individual players
        for init_value in self.value_dic:
            # for each card of individual player
            temp_list = self.value_dic[init_value]
            # for number of first, second and third card
            one_num_card = temp_list["First"][2]
            two_num_card = temp_list["Second"][2]
            three_num_card = temp_list["Third"][2]
            # sorting the number
            num = (one_num_card, two_num_card, three_num_card)
            num_sorted = sorted(num)
            num1 = num_sorted[0]
            num2 = num_sorted[1]
            num3 = num_sorted[2]

            # for shape of first, second and third card
            color1 = temp_list["First"][1]
            color2 = temp_list["Second"][1]
            color3 = temp_list["Third"][1]
            if color1 == color2 == color3:
                color_value.append(True)
            else:
                color_value.append(False)

            # read file
            read_file = pd.read_excel(r'NumberRule.xlsx')

            # ML to predict
            dataset_cond = read_file.drop(columns=['priority'])
            output_dataset = read_file['priority']

            # using tree
            mod_tree = DecisionTreeClassifier()

            # form above for prediction using tree for number value
            mod_tree.fit(dataset_cond.values, output_dataset)
            # prediction with given data
            prediction_result = mod_tree.predict([[num1, num2, num3]])
            # prediction based on previous data
            Player_Value.append(prediction_result[0])
        self.winner(Player_Value, color_value)

    def winner(self, pla_vlu, col_vlu):

        # for each individual players
        for i, init_value in enumerate(self.value_dic):
            if pla_vlu[i] <= pla_vlu[i + 1]:
                temp_pla_vlu = pla_vlu[i]
                # if 1 <= pla_vlu[i] <= 13:
                #     print("Trail")
                # elif 14 <= pla_vlu[i] <= 25 and col_vlu[i]:
                #     print("color and Sequence")
                # elif 14 <= pla_vlu[i] <= 25 and not col_vlu[i]:
                #     print("Sequence")
                # elif 26 <= pla_vlu[i] <= 181:
                #     print("Double")
                # else:
                #     print("normal")