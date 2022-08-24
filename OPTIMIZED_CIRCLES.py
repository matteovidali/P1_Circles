# Adapted from:  
# https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/

# This was optimized by Matteo Vidali (mvidali@iu.edu)

# I belive this is one of the best solutions physically possible... But I will tinker with it a bit more! :)
# If you are reading this nicole, im so sorry for the disgustingness - the optimizations leave it yucky as heck

# Ok nicole, I think this is the best possible solution using just lists
# maybe if i found a clever way to use sets or linked lists it could be faster,
# but i doubt it. Pls 


class MyCircleDrawer:
    def __init__(self):
        pass

    def midPointCircleDraw(self,x_centre, y_centre, r): 
        x = r 
        y = 0

        # Set up an array for each octant
        # Octant one is just left of negative y axis
        # octant 2 is directly clockwise after that etc.
        oct1 = []
        oct2 = []
        oct3 = []
        oct4 = []
        oct5 = []
        oct6 = []
        oct7 = []
        oct8 = []
 
        # Quick return if radius is less than 0
        if r <= 0:
            return [(x + x_centre, y_centre)]

        # Axis points 
        oct2 += (-x+x_centre, y_centre),
        oct4 += (x_centre, y_centre+x),
        oct6 += (x + x_centre, y_centre),
        oct8 += (x_centre, -x+y_centre),

        # Initialising the value of P  
        P = 1 - r  

        # Adjusted this while loop so we can have one less conditional
        # check inside of it. (removed last if (if x != y) 
        # because that only occurs in one instance)
        while x-1 > y+1: 
            y += 1

            # Mid-point inside or on the perimeter 
            if P <= 0:  
                P = P + 2 * y + 1

            # Mid-point outside the perimeter  
            else:          
                x -= 1
                # break here if x<y, dont want to check if we didn't adjust
                # x
                if x<y: break
                P = P + 2 * y - 2 * x + 1

            # Precalculating these 8 numbers otherwise we double calculate
            xmx, ymy = x_centre-x, y_centre-y
            xpx, ypy = x_centre+x, y_centre+y
            xmy, ymx = x_centre-y, y_centre-x
            xpy, ypx = x_centre+y, y_centre+x


            # adding points to each octant as necessary
            # The comma after the tuple adds a "tuple" to the
            # end of the list, which since the second value is empty,
            # just appends the first value. This is faster than append,
            # Because it doesnt create a funciton call, and instead
            # uses arithmetic to do it slightly faster
            oct2 += (xmx, ymy),
            oct3 += (xmx, ypy),
            oct6 += (xpx, ypy),
            oct7 += (xpx, ymy),
            oct1 += (xmy, ymx),
            oct4 += (xmy, ypx),
            oct5 += (xpy, ypx),
            oct8 += (xpy, ymx),


        # Now we check for the point y==x and adjust accordingly
        # basically running one more iteration of the loop outside
        # the loop to change it subtly
        y += 1

        # removed much of the P logic for faster processing
        if P>0:          
            x -= 1
        
        xmx, ymy = x_centre-x, y_centre-y
        xpx, ypy = x_centre+x, y_centre+y

        # Using a for loop here so we can leverage
        # break to allow for fewer conditionals
        # This does infact give us speedup in this case!
        for _ in range(1):
            # do nothing if there is no point here
            if x<y: break

            # This gets added in the case when x >= y
            oct2 += (xmx, ymy),
            oct3 += (xmx, ypy),
            oct6 += (xpx, ypy),
            oct7 += (xpx, ymy),

            # This gets added if x>y strictly
            if x > y:
                # only compute these values here 
                # since dont need them if we don't 
                # enter the conditional
                xmy, ymx = x_centre-y, y_centre-x
                xpy, ypx = x_centre+y, y_centre+x
                oct1 += (xmy, ymx),
                oct4 += (xmy, ypx),
                oct5 += (xpy, ypx),
                oct8 += (xpy, ymx),
            
            break

        # We have to reverse the even octants because
        # the were built backwards
        # this is the fastest way to reverse lists
        oct6 = oct6[::-1]
        oct4 = oct4[::-1]
        oct2 = oct2[::-1]
        oct8 = oct8[::-1]

        # now combine the octants into one circle
        return [*oct1, *oct2,*oct3, *oct4, *oct5,*oct6, *oct7, *oct8, oct1[0]]

    def draw_circles(self, inputs):
        circles = []
        # Using the tuple addition meathod is slightly faster 
        # than appending here! even faster than list comprehension!
        for x,y,r in inputs:
            circles += self.midPointCircleDraw(x,y,r),
        return circles

