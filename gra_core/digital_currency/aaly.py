class AALYTransaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.foam = max(0, amount - 100)

    def is_valid(self):
        return self.foam == 0
