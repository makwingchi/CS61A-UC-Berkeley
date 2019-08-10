## Q1: Write three different classes, Mailman, Client, and Email

class Email:
    """Every mail object has 3 instance attributes: the message,
    the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Mailman:
    """Each Mailman has an instance attribute clients, which is a dictionary that
    associates client names with client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is
        addressed to.
        """
        client_name = email.recipient_name
        client_object = self.clients[client_name]
        client_object.inbox.append(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is used for addressing
    emails to the client), mailman (which is used to send emails out to other
    clients), and inbox (a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        return Email(msg, self.name, recipient_name)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

## Q2: Inheritance
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False.
        """
        self.lives -= 1

        if self.lives == 0:
            self.is_alive = False

## Q3: NoisyCat
class NoisyCat(Cat):
    """A cat that repeats things twice."""
    def talk(self):
        for _ in range(2):
            print(self.name + ' says meow!')

## Q4: Implement the Foo class so that the following interpreter session works as expected
class Foo:
    def __init__(self, bar):
        self.bar = 1

    def g(self, num):
        return self.bar + num
