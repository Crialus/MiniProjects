target = 999999999
def SumDivisibleBy(x):
    p = target // x
    return x*(p*(p+1)) // 2 # some maths magic

print(SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15))