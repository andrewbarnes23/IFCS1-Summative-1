def equation(max_factor):
    import random    
    factor_one = random.randint(1,max_factor)
    factor_two = random.randint(1,max_factor)
    product = factor_one*factor_two
    return factor_one,factor_two,product