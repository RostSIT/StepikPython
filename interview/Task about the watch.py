hours = int(input())
minutes = int(input())

if hours > 12:
    hours %= 12
if minutes > 60:
    minutes %= 60
if hours == 12:
    hours = 0
if minutes == 60:
    minutes = 0

degreesPerCircle = 360
degreesPerHour = degreesPerCircle / 12
degreesPerMinute = degreesPerCircle / 60

allDegreesInHours = hours * degreesPerHour
allDegreesInMinutes = minutes * degreesPerMinute

if allDegreesInHours >= allDegreesInMinutes:
    theAngleBetweenPoints = (allDegreesInHours + allDegreesInMinutes/12) - allDegreesInMinutes
if allDegreesInMinutes > allDegreesInHours:
    theAngleBetweenPoints = allDegreesInMinutes - (allDegreesInHours + allDegreesInMinutes / 12)
if theAngleBetweenPoints > 180:
    theAngleBetweenPoints = degreesPerCircle - theAngleBetweenPoints

print(float(theAngleBetweenPoints), end=' ' + 'degrees between points')

