


from development.computer_vision import computer_vision
from maths import sortAlgorithm

import timer

import numpy

if __name__ == '__main__':
    
    
    a = sortAlgorithm.sort_algorithm()

    array = [5,4,3,2,1,0,89,4564,4151,215,354,454,8,789451,45,2,3215,54652,56,89,786,35,69,78,285,365,12,24]
    array2 = [5,4,3,2,1]

    a.test_run_time(array2)
    
    
    """
    print("\n")
    bub = a.bubbleSort(array)
    print(bub)
    cou = a.countingSort(array)
    print(cou)
    print("\n")
    print(type(cou[1]))
 
    """

##################################################################
    """
    b = computer_vision.Computer_vision()

    #image_loc = '/home/wrongside/Documents/git/development/computer_vision/drone3.jpg'
    #b.resize_image(image_loc, 400,200)

##################################################################
    
    kernel = numpy.ones((5 ,5), numpy.uint8)
    #print(type(kernel))
    kernel2 = numpy.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]], numpy.uint8)
    #print(type(kernel2))
    #print(kernel2)
    print(type(kernel))
    b.detect_colorRange(0,[110, 70, 70],[130, 255, 255])
    """