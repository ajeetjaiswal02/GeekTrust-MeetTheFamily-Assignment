from tests import *
import unittest
  
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
  
    def test_strings_a(self):
        self.assertEqual( 'a'*4, 'aaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*5, 'aaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*6, 'aaaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*7, 'aaaaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*8, 'aaaaaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*9, 'aaaaaaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*10, 'aaaaaaaaaa')
    def test_strings_a(self):
        self.assertEqual( 'a'*11, 'aaaaaaaaaaa')
        
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')
  
    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
  
    # Returns true if the string is stripped and 
    # matches the given output.
    def test_strip(self):        
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')
  
    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
  
if __name__ == '__main__':
    unittest.main()