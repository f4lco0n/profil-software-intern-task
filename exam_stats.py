class ExamsStats:
    def __init__(self, year, district, amount, status,gender):
        self.year = year #col4
        self.district = district #col1
        self.amount = amount #col5
        self.status = status #col2
        self.gender = gender #col3



    def __repr__(self):
         return 'Dane(%s, %s,%s,%s,%s)' % (self.year, self.district,self.amount,self.status,self.sex)

