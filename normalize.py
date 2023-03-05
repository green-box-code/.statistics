def normalize_array(arr):
    minVal = min(arr)
    print(minVal)
    maxVal = max(arr)                         
    print(maxVal)
    normalizedArr = []
    for i in arr:
        # x'' = 2\frac{x - \min{x}}{\max{x} - \min{x}} - 1
        normalizedVal = (2*(i - minVal)/(maxVal-minVal)) - 1     
        normalizedArr.append(normalizedVal)                                 
    return normalizedArr
    
data = [-3,-2,1,0,3,4,5]

print(normalize_array(data))
