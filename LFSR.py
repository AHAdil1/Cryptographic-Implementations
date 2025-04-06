# Linear Feedback Shift Register 
# 4 - Bit LFSR For PRNG
state = 0b1001
# Itterating it 20 times
for i in range(20):
    print("{:04b}".format(state))
    newbit = (state ^ (state >> 1))&1
    state = (state >> 1) | (newbit << 3)
    
