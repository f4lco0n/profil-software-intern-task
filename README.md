# profil-software-intern-task

**Setup**

Before you run program use:

*pip install -r requriments.txt*

**Available flags**

-t [t1,t2,t3,t4,t5] - run specific task

-d [polish voivodeship starting with capital letter] - extract data for specific district

-d2 [like above] - needed in task 5

-y [2010-2018] - extract data for specific year

-g [kobiety,mężczyźni] - optional flag to extract men or women

**Usage example**

*python main.py -t t5 -d Mazowieckie -d2 Dolnośląskie -g kobiety*


**Tests**

*pytest test_calculation_logic.py -vv*

**What should be fixed**
- Exceptions
- Enums
- Better solution to extract male or female
- Mocks for testing - at this moment they last too long
