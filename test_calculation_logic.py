import pytest
from calculation_logic import CalculationLogic
from data_provider import DataProvider

d = DataProvider()
data = d.extract_data()
x = CalculationLogic()

def test_task1():
    assert x.task1(data,2010,'Pomorskie') == 10481.5

def test_task1_only_women():
    assert x.task1(data,2010,'Pomorskie','kobiety') == 11798

def test_task1_only_men():
    assert x.task1(data,2010,'Pomorskie','mężczyźni') == 9165

def test_task2():
    assert x.task2(data,'Pomorskie') == {2010: 81, 2011: 74, 2012: 80, 2013: 80, 2014: 71, 2015: 73, 2016: 79, 2017: 78, 2018: 77}

def test_task2_only_women():
    assert x.task2(data,'Pomorskie','kobiety') == {2010: 81, 2011: 73, 2012: 79, 2013: 80, 2014: 70, 2015: 72, 2016: 79, 2017: 77, 2018: 77}

def test_task2_only_men():
    assert x.task2(data,'Pomorskie','mężczyźni') == {2010: 81, 2011: 76, 2012: 80, 2013: 80, 2014: 71, 2015: 74, 2016: 80, 2017: 78, 2018: 77}

def test_task3():
    assert x.task3(data,2010) == '2010: Kujawsko-pomorskie'

def test_task3_only_women():
    assert x.task3(data,2018,'kobiety') == '2018: Małopolskie'

def test_task3_only_men():
    assert x.task3(data,2017,'mężczyźni') == '2017: Lubuskie'


def test_task5():
    assert x.task5(data,'Wielkopolskie','Pomorskie') == ['2010: Pomorskie','2011: Wielkopolskie', '2012: Pomorskie',
                                                        '2013: Pomorskie','2014: Pomorskie','2015: Pomorskie',
                                                        '2016: Pomorskie','2017: Pomorskie','2018: Wielkopolskie']

def test_task5_only_women():
    assert x.task5(data,'Mazowieckie','Łódzkie','kobiety') == ['2010: Łódzkie','2011: Łódzkie', '2012: Mazowieckie',
                                                        '2013: Łódzkie','2014: Łódzkie','2015: Mazowieckie',
                                                        '2016: Łódzkie','2017: Łódzkie','2018: Mazowieckie']
def test_task5_only_men():
    assert x.task5(data,'Podkarpackie','Świętokrzyskie','mężczyźni') == ['2010: Podkarpackie','2011: Świętokrzyskie', '2012: Podkarpackie',
                                                        '2013: Podkarpackie','2014: Świętokrzyskie','2015: Podkarpackie',
                                                        '2016: Świętokrzyskie','2017: Podkarpackie','2018: Świętokrzyskie']