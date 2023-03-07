def mean(arr):
    """ Find the mean value of an array """
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum/len(arr)

def sqrt(x):
    """ Find the positive square root of a value """
    if x > 0:
        sqrt_x = x**(1/2)
        return sqrt_x
    elif:
        print("The value must be positive")
        

def pearson_correlation(X, Y):
    mean_X = mean(X)
    mean_Y = mean(Y)
    X_diffs = [x - mean_X for x in X]
    Y_diffs = [y - mean_Y for y in Y]
    sum_X_diffs_sq = sum([x ** 2 for x in X_diffs])
    sum_Y_diffs_sq = sum([y ** 2 for y in Y_diffs])
    sum_XY_diffs = sum([x * y for (x, y) in zip(X_diffs,Y_diffs)])
    r = sum_XY_diffs / (sqrt(sum_X_diffs_sq) * sqrt(sum_Y_diffs_sq))
    return r

X = [1,2,3,4,4,4,5,6,7]
Y = [1,2,3,3,3,3,5,5,6]

print(pearson_correlation(X,Y))
