from time import strftime
import omega_gpio

# Function to set RGB LED
def setrgb(red,green,blue):
  omega_gpio.setoutput(7,1 if red==0 else 0)
  omega_gpio.setoutput(8,1 if green==0 else 0)
  omega_gpio.setoutput(6,1 if blue==0 else 0)

######## Main routine starts here ########

#Initialize pins for RGB LED
for x in range(6,8):
  omega_gpio.initpin(x,'out')

#Start with the current time
curtime=strftime("%H%M%S")
newtime=curtime

# Infinite loop. 
while True:
  #Wait for time to change
  while newtime == curtime:
    newtime=strftime("%H%M%S")

  curtime=newtime

  #Set LED according to seconds
  seconds=int(curtime[-2:])
  ledtic=seconds % 6

  if seconds==59:
    setrgb(0,0,0) # off
    print "off"
  elif seconds==0:
    setrgb(1,1,1) # white
    print "white"
  elif ledtic==0:
    setrgb(1,0,0) # red
    print "red"
  elif ledtic==1:
    setrgb(0,1,0) # green
    print "green"
  elif ledtic==2:
    setrgb(0,0,1) # blue
    print "blue"
  elif ledtic==3:
    setrgb(0,1,1) # cyan
    print "cyan"
  elif ledtic==4:
    setrgb(1,0,1) # magenta
    print "megenta"
  else:
    setrgb(1,1,0) # yellow
    print "yellow"

  R=1-omega_gpio.readinput(7)
  G=1-omega_gpio.readinput(8)
  B=1-omega_gpio.readinput(6)
  #S=("R" if R==1 else " ") + ("G" if G==1 else " ") + ("B" if B==1 else " ")
  #print S

# We'd like to see the dog kennels, please.

