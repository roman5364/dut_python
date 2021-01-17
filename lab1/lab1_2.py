import math

x = int(28)
t = int(1)

z = ((9*math.pi*t + 10*math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t))))*math.exp(x)
print(z)
