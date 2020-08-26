#fullarray

import unittest

class NameBuilding:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    
    def getfirstname (self):
        return self.fname   
    
    def getlastname(self):
        return self.lname
        
    def fullname(self):
        return self.getfirstname() +' '+ self.getlastname()

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_fullname(self):
        name = NameBuilding('John','oe')
        name_glued = name.fullname()
        self.assertEqual('John Doe',name_glued)
    
    def test_strings_a(self):
        self.assertEqual('aaaa','aaaa')
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello', 'world'])
       
    def test_uppercase(self):
        #s1 = 'hello'
        s2 = 'JELLO'
        #self.assertTrue(s1.isupper())
        self.assertTrue(s2.isupper())
   
if __name__=='__main__':
    unittest.main()