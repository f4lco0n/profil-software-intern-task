from collections import defaultdict

class CalculationLogic:

    def task1(self, data,year,district,gender=None):

        if gender:
            result = [stat.amount for stat in data if stat.status == 'przystąpiło'
                      and stat.year <= year
                      and stat.district == district and stat.gender == gender]
        else:
            result = [stat.amount for stat in data if stat.status == 'przystąpiło'
                      and stat.year <= year
                      and stat.district == district]

        return (sum(result) / len(result))

    def task2(self,data,district,gender=None):
        passed_result = defaultdict(int)
        proceeded_result = defaultdict(int)

        if gender:
            for stat in data:
                if stat.status == 'zdało' and stat.district == district and stat.year <= 2018 and stat.gender == gender:
                    passed_result[int(stat.year)] += stat.amount
                if stat.status == 'przystąpiło' and stat.district == district and stat.year <= 2018 and stat.gender == gender:
                    proceeded_result[int(stat.year)] += stat.amount
        else:
            for stat in data:
                if stat.status == 'zdało' and stat.district == district and stat.year <= 2018:
                    passed_result[int(stat.year)] += stat.amount
                if stat.status == 'przystąpiło' and stat.district == district and stat.year <= 2018:
                    proceeded_result[int(stat.year)] += stat.amount

        result = {k: int(passed_result[k]/ proceeded_result[k] * 100) for k in proceeded_result}
        return result

    def task3(self,data,year,gender=None):
        passed_list = []
        proceeded_list = []

        if gender:
            for w in data:
                if w.status == 'zdało' and w.year == year and w.district != 'Polska' and w.gender == gender:
                    passed_list.append(tuple((w.district, w.amount)))
                if w.status == 'przystąpiło' and w.year == year and w.district != 'Polska' and w.gender == gender:
                    proceeded_list.append(tuple((w.district, w.amount)))

        else:
            for w in data:
                if w.status == 'zdało' and w.year == year and w.district != 'Polska':
                    passed_list.append(tuple((w.district, w.amount)))
                if w.status == 'przystąpiło' and w.year == year and w.district != 'Polska':
                    proceeded_list.append(tuple((w.district, w.amount)))

        passed_dict = defaultdict(int)
        proceeded_dict = defaultdict(int)
        for k,v in passed_list:
            passed_dict[k] += v
        for k,v in proceeded_list:
            proceeded_dict[k] += v

        result = {k: int(passed_dict[k]/ proceeded_dict[k] * 100) for k in proceeded_dict if k in passed_dict}
        maximum = max(result, key=result.get)

        return "{}: {}".format(year,maximum)

    def task4(self,data,gender=None):
        voivodeship = {d.district for d in data}
        voivodeship.remove('Polska')
        final_result = list()
        if gender:
            for district in voivodeship:
                result = self.task2(data, district,gender)
                for year in range(2010, 2018):
                    if result[year] > result[year + 1]:
                        final_result.extend(["{}: {} -> {} ".format(district, year, year + 1)])
        else:
            for district in voivodeship:
                result = self.task2(data, district)
                for year in range(2010, 2018):
                    if result[year] > result[year + 1]:
                        final_result.extend(["{}: {} -> {} ".format(district, year, year + 1)])

        return final_result



    def task5(self,data,district1, district2,gender=None):
        result1 = self.task2(data,district1,gender)
        result2 = self.task2(data,district2,gender)
        final_result = list()
        for year in range(2010, 2019):
            if result1[year] > result2[year]:
                final_result.extend(["{}: {}".format(year, district1)])
            else:
                final_result.extend(["{}: {}".format(year,district2)])

        return final_result