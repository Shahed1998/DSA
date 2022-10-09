def factorial(num):
    # iterative
    # total = 1
    # while num > 1:
    #     total *= num
    #     num -= 1
    # return total

    # recursive
    if num == 1: return 1 # base case
    return num * factorial(num - 1)


print(factorial(4)) # 4! = 4 * 3 * 2 * 1