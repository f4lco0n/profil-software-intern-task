import argparse

from calculation_logic import CalculationLogic
from data_provider import DataProvider

class UserActionHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--task", "-t", type=str, help="number of task")
        self.parser.add_argument("--district", "-d", type=str, help="voivodeship")
        self.parser.add_argument("--district2", "-d2", type=str, help="voivodeship2")
        self.parser.add_argument("--year", "-y", type=int, help="year")
        self.parser.add_argument("--gender","-g",type=str)

    def execute_command(self):
        args = self.parser.parse_args()

        d = DataProvider()
        data = d.extract_data()
        x = CalculationLogic()
        if args.task == 't1':
            if args.district and args.year:
                if args.gender:
                    print(x.task1(data, args.year, args.district,args.gender))
                else:
                    print(x.task1(data, args.year, args.district))
        elif args.task == 't2':
            if args.district:
                if args.gender:
                    print(x.task2(data,args.district,args.gender))
                else:
                    print(x.task2(data, args.district))
        elif args.task == 't3':
            if args.year:
                if args.gender:
                    print(x.task3(data,args.year,args.gender))
                else:
                    print(x.task3(data,args.year))
        elif args.task == 't4':
            if args.gender:
                print(x.task4(data,args.gender))
            else:
                print(x.task4(data))
        elif args.task == 't5':
            if args.district and args.district2:
                if args.gender:
                    print(x.task5(data,args.district,args.district2,args.gender))
                else:
                    print(x.task5(data,args.district,args.district2))


