# demo @property


class Bill:
    def __init__(self, customer, value, tax):
        self.customer = customer
        self.value = value
        self.tax = tax

    @property
    def total(self):
        print('abc')
        return self.value + self.value*self.tax/100

    @total.setter
    def total(self, total):
        self.value = total/(1+self.tax/100)

    # total = property(fget=get_total, fset=set_total)


bill = Bill('John', 1000, 50)
bill.total = 3000
print(bill.customer)
print(bill.value)
print(bill.tax)
print(bill.total)

