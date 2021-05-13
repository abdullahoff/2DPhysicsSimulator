## @file BodyT.py
#  @author Abdullah Abdullah
#  @brief Creates a a bodyT shape
#  @date 02/16/2021
from Shape import Shape

## @brief BodyT creates a body object
#  @details extends Shape


## @brief calculates the centre of mass of the bodyT object
#  @param m is the mass sequcene which represents the BodyT object
#  @param z is a sequence
#  @param m is a sequence that is representative of the mass
#  @return The centre of mass of the shape in question
def cm(z, m):
    s = 0
    for i in range(len(m)):
        s += (z[i] * m[i])
    return s / sum(m)


## @brief calculates the sum of the inputed mass sequence
#  @details utilises a for loop to calculate the sum of the mass sequence given
#  @param m_s is the sequence for the mass of the BodyT object
#  @return the sum of the entire mass of the bodyT object
def sum(m_s):
    total = 0
    for i in m_s:
        total += i
    return total


## @brief calculates the momentum of a shape
#  @details the momentum is the force acting on a particle with units Kg*m/s
#  @param x is the sequence of the centre of masses
#  @param y is the sequence of the centre of masses
#  @param m is the sequence of the masses for the shape
#  @return the moment for the specified shape
def mmom(x, y, m):
    total = 0
    for i in range(len(m)):
        total += m[i] * (x[i] ** 2 + y[i] ** 2)
    return total


class BodyT(Shape):

    ## @brief constructor method for BodyT
    #  @details This creates an BodyT object
    #  @param x_s is the x sequence of the centre of mass
    #  @param y_s is the y sequence of the centre of mass
    #  @param m_s is the mass of the BodyT object
    def __init__(self, x_s, y_s, m_s):
        for i in m_s:
            if(i <= 0):
                raise ValueError
        if(not (len(x_s) == len(y_s) == len(m_s))):
            raise ValueError
        else:
            self.cmx = cm(x_s, m_s)
            self.cmy = cm(y_s, m_s)
            self.m = sum(m_s)
            self.moment = mmom(x_s, y_s, m_s) - (sum(m_s) * ((cm(x_s, m_s)) ** 2 + (cm(y_s, m_s)) ** 2))

	

    ## @brief A generic method that returns the centre of mass in the x
	## @return  x coordinate of the centre of mass
    def cm_x(self):
        return self.cmx

	## @brief A generic method that returns the centre of mass in the y
	## @return  y coordinate of the centre of mass
    def cm_y(self):
        return self.cmy

	## @brief A generic method that return the mass of the shape
	## @return the mass of the shape
    def mass(self):
        return self.m

	## @brief A generic method that return the m_inertia of the shape
	## @return the m_inertia of the shape object
    def m_inert(self):
        return self.moment
