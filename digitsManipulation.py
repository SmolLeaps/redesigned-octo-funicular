def digitsManipulation(n):
    '''
    
    '''
    n = str(n)

    total = 0
    product = 1  
    for eachDigit in n:
        eachDigit = int(eachDigit)
        total = int(total)
        total += eachDigit
        product *= eachDigit
        print(product)
    
    print(product, total)
    return product-total

print(digitsManipulation(123))

#keep as string or number?