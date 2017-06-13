import unittest.py

class TempConverterTest(unittest.TestCase):
  #given temp in celcius = correct value in Fht
  def test_Celcius_is_converted_to_farenheight(self):
   actual = convert_celcius_to_farenheight(10)
   expected = 50
   self.assertEqual(actual, expected, msg = "celcius should conert to correct farenheight")
if _name_ =='_main_':
   unittest.main()  