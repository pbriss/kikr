class Event(object):
    index = 0
    movetype = ""
    movename = ""
    movedata = ""
    starttime = 0
    endtime = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, index, movetype, movename, movedata, starttime, endtime):
        self.index = index
        self.movetype = movetype
        self.movename = movename
        self.movedata = movedata
        self.starttime = starttime
        self.endtime = endtime
