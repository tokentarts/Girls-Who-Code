#!/bin/python3
from turtle import *

# write(0)
# forward(100)
# write(5)

# write(0)
# forward(20)
# write(1)
# forward(20)
# write(2)
# forward(20)
# write(3)
# forward(20)
# write(4)
# forward(20)
# write(5)

# Hmm, that only prints numbers up to 4.
# In Python range(5) returns five numbers, from 0 up to 4.
# To get it to also return 5 you’ll need to use range(6):
for step in range(5):
    write(step)
    forward(20)
