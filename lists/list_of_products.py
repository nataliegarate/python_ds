def findProduct(arr):
    products = []
    product = 1
    for x in arr:
        product *= x

    for num in arr:
        products.append(product/num)
    return products


print(findProduct([1, 2, 3, 4]))
