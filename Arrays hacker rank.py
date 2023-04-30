def arrays(arr):
    my_array = []
    a = numpy.array(arr, float)
    for i in range(len(a)):
        my_array.append(a[(len(a)-1)-i])
        
    return numpy.array(my_array,float)