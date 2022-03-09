import math
r = abs(3.0*(4.0/3.0-1)-1)
print(r)
epsilon_machine = 1
while (1+epsilon_machine)!=1:
    e1 = epsilon_machine
    epsilon_machine /= 2
print(e1)
print(r-e1)
