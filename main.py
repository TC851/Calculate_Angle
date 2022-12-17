# This program calculates the angle of an analog clock


# Formula Hour
def hour(H, M):
    return (60 * H + M) / 2


# Formula Minute
def minute(M):
    return 6 * M


hourAngle = hour(11, 15)
minuteAngle = minute(15)

# main ------------------------------------------------------------------------------------------------------

print("Calculate the angles:")

print()

output = "The hour angle are" + " " + str(hourAngle) + " " + "and the minute angle are" + " " + str(minuteAngle) + "."

print(output)


