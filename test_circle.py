import unittest
from circle import *


class test_circle(unittest.TestCase):
    #def test_somthing(self):
    #    self.assertEqual(function, answer)

    def test_initNeg(self):
        #you shouldn't be allowed to initialize a negative radius
        #this test should fail
        c = Circle(-1)
        self.assertNotEqual(c.getRadius(), -1)

    def test_getRadius(self):
        c = Circle(10)
        self.assertEqual(c.getRadius(), 10)

        c.setRadius(3)
        self.assertEqual(c.getRadius(), 3)

    def test_setRadius(self):
        c = Circle(1)
        self.assertEqual(c.setRadius(5), True)
        self.assertEqual(c.setRadius(-1), False)
        self.assertEqual(c.setRadius(0), True)

    def test_get_when_setNegRadius(self):
        c = Circle(1)
        c.setRadius(-1)

        self.assertEqual(c.getRadius(), 1)

    def test_getArea(self):
        c = Circle(0)
        self.assertEqual(c.getArea(), 0)
        
       #sigh... do we really want so many decimal points 
        c.setRadius(1)
        self.assertEqual(c.getArea(), 3.141592653589793)
        
        c.setRadius(539209938)
        self.assertEqual(c.getArea(), 9.134097615494344e+17 )
        
        c.setRadius(4)
        self.assertEqual(c.getArea(), 50.26548245743669)
      
        c.setRadius(.2)
        self.assertEqual(c.getArea(), 0.12566370614359174)

        #why is that if statement even there? should it be 0?
        c.setRadius(2)
        self.assertEqual(c.getArea(), 12.56)

    def test_getCircumference(self):
        c = Circle(0)
        self.assertEqual(c.getCircumference(), 0)
        
        c.setRadius(1)
        self.assertEqual(c.getCircumference(), 6.283185307179586)

        c.setRadius(2)
        self.assertEqual(c.getCircumference(), 12.566370614359172)

        c.setRadius(.2)
        self.assertEqual(c.getCircumference(), 1.2566370614359172)





