def check(numbers):
    max = numbers[0]
    min = numbers[0]
    for i in numbers:
        if i >= max:
            maxmum = i
        if i <= min:
            minmum = i
    return maxmum,minmum

print(check([10,5,30,2,50,15]))
