multiples = []
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0: # if the modulo of x divided by 3/5 = 0, ie x is divisible by 3 or 5 then append to the array multiples
       multiples.append(x)
print(sum(multiples))
