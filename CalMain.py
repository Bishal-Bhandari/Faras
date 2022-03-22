import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import openpyxl
import numpy

Player_Value = []
Player_Name = []


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
                color_value = 1
            else:
                color_value = 0

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
            prediction_result = mod_tree.predict([[num1, num2, num3, color_value]])
            # prediction based on previous data
            Player_Value.append(prediction_result[0])

        # getting the key
        for key in self.value_dic:
            Player_Name.append(key)
        # making the dict from two lists
        result_dict = dict(zip(Player_Name, Player_Value))

        self.winner(result_dict)

    def winner(self, res_dict):
        # sorting the dict according to its value
        result = dict(sorted(res_dict.items(), key=lambda item: item[1]))

        # result printing
        print(f'Rank : Name')
        for i, val in enumerate(result):
            print(f'{i + 1}    :   {val}')
