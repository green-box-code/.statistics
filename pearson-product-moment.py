def pearson_product_moment(data):
    """Calculate the Pearson product-moment correlation coefficient at a given data.
    
    Parameters
    ----------
    data : 2d array
        A 2d array of data points.
    
    Returns
    -------
    float
        The Pearson product-moment correlation coefficient.
    """
    
    # calculate mean of data points
    mean_x = sum(data[0])/len(data[0])
    mean_y = sum(data[1])/len(data[1])
    
    # calculate numerator and denominator
    numerator = 0
    denominator_x = 0
    denominator_y = 0
    for i in range(len(data[0])):
        numerator += (data[0][i] - mean_x) * (data[1][i] - mean_y)
        denominator_x += (data[0][i] - mean_x) ** 2
        denominator_y += (data[1][i] - mean_y) ** 2
        
    denominator = (denominator_x * denominator_y) ** 0.5
    
    # calculate Pearson product-moment correlation coefficient
    r = numerator / denominator
    
    return r
