import tehtava1 as t1
import numpy as np
import matplotlib as plt
from tehtava1 import signalAnalyser as s

Fs = 1000

time = int(input("input time in seconds: "))
print(" = ",time, "sec")

frequency = int(input("insert frequency 0-500: "))
print("u gave", frequency)

lkm = int(input("insert dot count: "))
print("u gave ", lkm,"dots")

olio = s(Fs,time)
olio.create(frequency)
olio.plot(0,lkm)