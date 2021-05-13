## @file CircleT.py
#  @author Abdullah Abdullah
#  @brief Contains a generic CircleT type
#  @date 02/16/2021

from Shape import Shape

## @brief CircleT is a class that implements a Shape object containing year, month and a day
#  @details extends from Shape


class CircleT(Shape):

	## @brief constructor method for class CircleT, initalizes a CircleT given
	#   mass, radius, centre of mass x and y coordinates
	#  @details The shape is initalized with value's for mass and radius to be
	#   greater than 0 and the centre of mass is taken from the parameters.
	#  These parameters can come together to define what properties a circle shape has.
	#  @param x_s is the x coordinate of the centre of mass
	#  @param y_s is the y coordinate of the centre of mass
	#  @param r_s is the radius of the circle shape
	#  @param m_s is the mass of the circle shape
	#  @throws Value error if both the radius or the mass are less than or equal to 0
    def __init__(self, x_s, y_s, r_s, m_s):
        if(r_s > 0 and m_s > 0):
            self.x = x_s
            self.y = y_s
            self.r = r_s
            self.m = m_s

        else:
            raise ValueError

	## @brief A generic method that returns the centre of mass in the x
	## @return  x coordinate of the centre of mass
    def cm_x(self):
        return self.x

	## @brief A generic method that returns the centre of mass in the y
	## @return  y coordinate of the centre of mass
    def cm_y(self):
        return self.y

	## @brief A generic method that return the mass of the shape
	## @return the mass of the shape
    def mass(self):
        return self.m

	## @brief A generic method that return the m_inertia of the shape
	## @return the m_inertia of the shape object
    def m_inert(self):
        return ((self.m) * ((self.r) ** 2)) / 2
