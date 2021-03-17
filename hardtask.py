a1 = int(input('Units of first number  a1 - '))
a2 = int(input('Tens of firs number  a2 - '))
b = int(input('Single number   B - '))
d = (a1 + b) % 10
f = a2 + (a1 + b) // 10
print('Numbers of sum ', f, ' ', d)
