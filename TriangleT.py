## @file TriangleT.py
#  @author Abdullah Abdullah
#  @brief Contains the TriangleT type to represent a triangle shape
#  @date 02/16/2021

from Shape import Shape

## @brief TriangleT is used to represent a Triangle shape


class TriangleT(Shape):
	## @brief constructor for class TriangleT, represents a Triangle
	#   which will be used in simulations
	#  @details The shape is initalized with value's for mass and side lengths to be greater
	#   than 0 and the centre of mass is taken from the parameters.
	#  These parameters can come together to define what properties a circle shape has.
	#  @param x_s  is the x coordinate of the centre of mass
	#  @param t_s is the y coordinate of the centre of mass
	#  @param s_s is contains the side lengths of the triangle
	#  @param m_s is the mass of the triangle shape
	#  @throws ValueError if the mass or the side length are less than or equal to 0
	def __init__(self, x_s, y_s, s_s, m_s):
		if(s_s > 0 and m_s > 0):
			self.x = x_s
			self.y = y_s
			self.s = s_s
			self.m = m_s

		else:
			raise ValueError

	## @brief getter method for the x coordinate of the centre of mass
	#  @details indicates the centre of mass for the triangle shape
	#  @return the x coordinate of the centre of mass
	def cm_x(self):
		return self.x

	## @brief getter method for the y coordinate of the centre of mass
	#  @details indicates the centre of mass of the triangle shape
	#  @return the y coordinate of the centre of mass
	def cm_y(self):
		return self.y

	## @brief getter method for the mass of the triangle object
	#  @details indicates the mass of the of the triangle
	#  @return the mass of the shape
	def mass(self):
		return self.m

	## @brief A generic method that return the m_inertia of the shape
	#  @details indicates the moment of inertia of the shape
	#  @return the m_inertia of the shape object
	def m_inert(self):
		return ((self.m) * ((self.s) ** 2)) / 12
