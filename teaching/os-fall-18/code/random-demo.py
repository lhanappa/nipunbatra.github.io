import random
import sys

CPU_LENGTH = int(sys.argv[1])
CPU_PROB = float(sys.argv[2])
IO_LENGTH = int(sys.argv[3])

count = 0
while count < CPU_LENGTH:
    if random.random() < CPU_PROB/100.0:
        count = count + 1
        print("CPU")
    else:
        print(("IO\n"*IO_LENGTH)[:-1])
     


