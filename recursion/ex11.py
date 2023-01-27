def nestedEvenSum(obj):

    if type(obj) == type(1): return obj

    # TBC
    for key, value in obj.items():
        print(value)

print(nestedEvenSum({
    "abc": 1,
    "def": {
        "ghi": 4
    }
}))