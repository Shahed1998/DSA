try:
    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    sum = 0
    # Formula:
    # sum = ((highest num - lowest num +1) * (highest num + lowest num))/2
    sum = ((b-a+1)*(b+a))/2 if b>a else ((a-b+1)*(b+a))/2
    print(f"Sum of all numbers from a to b: {int(sum)}")

except ValueError:
    print("Invalid input") 