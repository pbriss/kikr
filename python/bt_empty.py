import time

print "starting"
while 1:
    f = open('python/state.txt', 'r')
    if f.readline() == "0":
        break
    print "running..."
    time.sleep(1)
print "done"