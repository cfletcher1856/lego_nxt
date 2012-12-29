import nxt, thread, time
b = nxt.find_one_brick()
mx = nxt.Motor(b, nxt.PORT_B)
my = nxt.Motor(b, nxt.PORT_C)
motors = [mx, my]

def turnmotor(m, power, degrees):
            m.turn(power, degrees)

instructions = (
    [0, 0, 80, 1080],
    [0, 1, 80, 1080],
    [3, 0, 100, 1080],
    [3, 1, 100, 1080],
    [6, 0, 100, 1080],
    [6, 1, -100, 1080],
    [9, 0, 100, 2000],
    [9, 1, 100, 2000],
)

length = 5

def runinstruction(i):
    motorid, speed, degrees = i
    #THIS IS THE IMPORTANT PART!
    thread.start_new_thread(
        turnmotor,
        (motors[motorid], speed, degrees))

seconds = 0
while 1:
    print "tick %d" % seconds
    for i in instructions:
        if i[0] == seconds:
            runinstruction(i[1:])
    seconds = seconds + 1
    if seconds >= 15:
        mx.brake()
        my.brake()
        break
    time.sleep(1)
