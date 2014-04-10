'''This module contains a method for overlapping rectangles'''

def overlap(red, blue) :
    '''Takes in two a tuple of tuples that mark out the corners of a
    rectangle.  Returns overlap between the two rectangles or None.
    Sample Usage : 
    $ overlap( ((0,0),(1,1)) , ((1,1),(2,2)) )
    >>>> None
    '''

    ( (red_lo_x, red_lo_y), (red_hi_x, red_hi_y) ) = red
    ( (blue_lo_x, blue_lo_y), (blue_hi_x, blue_hi_y) ) = blue

    # First check if the rectangle x or y bounds are completely
    # outside of one another and there is clearly no overlap.
    if (red_lo_x >= blue_hi_x) or (red_hi_x <= blue_lo_x) or \
            (red_lo_y >= blue_hi_x) or (red_hi_y <= blue_lo_y) :
        return None

    lo_x = max( red_lo_x, blue_lo_x )
    lo_y = max( red_lo_y, blue_lo_y )
    hi_x = min( red_hi_x, blue_hi_x )
    hi_y = min( red_hi_y, blue_hi_y ) 

    return ( (lo_x, lo_y), (hi_x, hi_y) )
