class Calculation:
    def __init__(self, value_dic):
        self.value_dic = value_dic

    def main_cal(self):
        for init_value in self.value_dic:
            print(f"this {self.value_dic}")
            print(self.value_dic[init_value])
