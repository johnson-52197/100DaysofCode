'''
Power digit sum

Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

import time
n = 1000 # nth power

value = 2**n
total = 0
val1 = value
val2 = value
start_time_1 = time.time()

while(val1>0):
    temp = val1%10
    total += temp
    val1 = (val1//10)

print(total)

print("Time of Execution for approach 1 {} seconds".format(time.time()-start_time_1))

start_time_2 = time.time()

val2 = list(map(int,str(val2)))
print(sum(val2))

print("Time of Execution for approach 2 {} seconds".format(time.time()-start_time_2))


'''
1366
Time of Execution for approach 1 0.000997304916381836 seconds
1366
Time of Execution for approach 2 0.0 seconds
'''
# approach 2 seems to work faster (in this case)