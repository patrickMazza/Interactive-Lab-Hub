# Use touched_pins to get current state of all pins.
touched = mpr121.touched_pins
# Test if 0 and 11 are touched.
if touched[0] and touched[11]:
    print('Input 0 and 11 touched!')