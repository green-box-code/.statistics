import numpy as np # <--- Get rid of numpy
def pearson_correlation(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    X_diffs = [x - mean_X for x in X]
    Y_diffs = [y - mean_Y for y in Y]
    sum_X_diffs_sq = sum([x ** 2 for x in X_diffs])
    sum_Y_diffs_sq = sum([y ** 2 for y in Y_diffs])
    sum_XY_diffs = sum([x * y for (x, y) in zip(X_diffs,Y_diffs)])
    r = sum_XY_diffs / (np.sqrt(sum_X_diffs_sq) * np.sqrt(sum_Y_diffs_sq))
    return r

X = [1,2,3,4,4,4,5,6,7]
Y = [1,2,3,3,3,3,5,5,6]
print(pearson_correlation(X,Y))
