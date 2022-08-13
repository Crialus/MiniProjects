max = int(4000000)
n1 = 1
n2 = 2
divisible = []
while n2 < max:
    y = n1 + n2
    if n2 % 2 == 0 :
        divisible.append(n2)
    n1 = n2
    n2 = y

print(sum(divisible))

