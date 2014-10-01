''' Computing Mandelbrot sets.'''

import math

def mandel(real, imag):
    ''' Compute a point in the Mandelbrot.
    
    The logarithm of number of iterations needed to determine whether a complex point is in the Mandelbrot set
    
    Args:
        real: The real coordinate
        imag: The imaginary coordinate
        
    Returns:
        An integer in the range 1-255
    '''

