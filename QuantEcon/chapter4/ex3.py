from numpy.random import uniform

def expected_value(n):
    p = 0.5
    payout = 0
    k = 0
    for i in range(n):
        if k == 1:
            payout +=1
        if uniform(0,1) > p:
            k = 1
        else:
            k = 0
    return payout

print(expected_value(10))


