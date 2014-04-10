from overlapping_rectangles import *
'''To run all of these tests, execute 
$ nosetests
from the bash command line
See if you can find the error.
'''

def test_touch_on_corner() :
    '''Test the boundary case where they touch on a corner'''

    one = ((0,0),(1,1))
    two = ((1,1),(2,2))

    assert find_overlap(one,two) == None

def test_unit_with_itself() :
    '''A good test'''
    
    unit = ((0,0),(1,1))

    assert find_overlap(unit, unit) == unit

def test_partial_overlap() :
    '''Tests a case where one rectangle is skinnier than the other.'''

    red = ((0,3),(2,5))
    blue = ((1,0),(2,4))

    assert find_overlap(red, blue) == ((1,3),(2,4))


