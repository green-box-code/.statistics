def standard_deviation(data):
    mean = sum(data)/len(data)
    sum_sq_diff = 0
    for i in data:
        sum_sq_diff += (i - mean)**2
    return (sum_sq_diff/len(data))**0.5

data = [1,2,3,4,5]
print(standard_deviation(data))
