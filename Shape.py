## @file Shape.py
#  @author Abdullah Abdullah
#  @brief An interface for shape
#  @date 02/16/2021

from abc import ABC

## @brief Shape contains cm_x, cm_y, mass and m_inert methods

class Shape(ABC):

	## @brief A generic method that returns the centre of mass in the x
	#  @return  x coordinate of the centre of mass
	def cm_x(self):
		pass

	## @brief A generic method that returns the centre of mass in the y 
	#  @return  y coordinate of the centre of mass
	def cm_y(self):
		pass

	## @brief A generic method that return the mass of the shape
	# @return the mass of the shape 
	def mass(self):
		pass

	## @brief A generic method that return the m_inertia of the shape
	#  @return the m_inertia of the shape object
	def m_inert(self):
		pass
