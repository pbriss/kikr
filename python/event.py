class Event(object):
    start = 0
    end = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, start, end):
        self.start = start
        self.end = end
