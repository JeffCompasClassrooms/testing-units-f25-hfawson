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
        
        c.setRadius(1)
        self.assertEqual(round(c.getArea(), 2), 3.14)
        
        #apparently rounding dosn't work when numbers get that high
        c.setRadius(539209938)
        self.assertEqual(round(c.getArea(), 2), 9.134097615494344e+17 )
        
        c.setRadius(4)
        self.assertEqual(round(c.getArea(), 2), 50.27)
      
        c.setRadius(.2)
        self.assertEqual(round(c.getArea(), 2), 0.13)

        #why is that if statement even there? should it be 0?
        c.setRadius(2)
        self.assertEqual(round(c.getArea(), 2), 12.57)

    def test_getCircumference(self):
        c = Circle(0)
        self.assertEqual(c.getCircumference(), 0)
        
        c.setRadius(1)
        self.assertEqual(round(c.getCircumference(), 2), 6.28)

        c.setRadius(2)
        self.assertEqual(round(c.getCircumference(), 2), 12.57)

        c.setRadius(.2)
        self.assertEqual(round(c.getCircumference(), 2), 1.26)





