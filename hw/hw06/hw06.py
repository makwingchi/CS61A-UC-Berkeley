# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            result = Fib(1)
        else:
            result = Fib(self.value + self.prev)

        result.prev = self.value
        return result

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.dep = 0

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.dep < self.price:
            return 'You must deposit ${} more.'.format(self.price - self.dep)
        elif self.dep == self.price:
            self.dep, self.stock = 0, self.stock - 1
            return 'Here is your {}.'.format(self.product)
        elif self.dep > self.price:
            change = self.dep - self.price
            self.dep, self.stock = 0, self.stock - 1
            return 'Here is your {} and ${} change.'.format(self.product, change)

    def deposit(self, money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(money)
        else:
            self.dep += money
            return 'Current balance: ${}'.format(self.dep)

    def restock(self, amount):
        self.stock += amount
        return 'Current {} stock: {}'.format(self.product, self.stock)
