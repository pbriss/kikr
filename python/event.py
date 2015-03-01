class Event(object):
    move = ""
    start = 0
    end = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, start, end, move):
        self.move = move
        self.start = start
        self.end = end
