def binomial_rv(n, p):
    from numpy.random import uniform
    x = 0
    for i in range(n):
        if p >= uniform(0, 1):
            x += 1
    return x

binomial_rv(14, 0.8)
