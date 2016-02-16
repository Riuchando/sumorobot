#http://jeremyblythe.blogspot.com/2012/09/raspberry-pi-distance-measuring-sensor.html

def write_distance():
    display.position_cursor(1, 1)
    r = []
    for i in range (0,10):
        r.append(mcp3008.readadc(1))
    a = sum(r)/10.0
    v = (a/1023.0)*3.3
    d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
    cm = int(round(d))
    val = '%d cm' % cm
    percent = int(cm/1.5)
    display.ser.write(str(val).ljust(16))
    display.capped_bar(16, percent)
