from pt1 import pt1
import unittest

class test_bmi_value(unittest.TestCase):
    def test_bmi_height(user):
        bm=bmi_calculation()
        user.assertEqual(bm.calculate_bmi(0,0,0),"Height can't be zero.")
        user.assertEqual(bm.calculate_bmi(-1,0,0),"Height can't be negative.")
        user.assertEqual(bm.calculate_bmi(-1,-1,0),"Height can't be negative.")
        user.assertEqual(bm.calculate_bmi(0,0,1501),"Height can't be zero.")
        user.assertEqual(bm.calculate_bmi(-1,0,1500),"Height can't be negative.")
        user.assertEqual(bm.calculate_bmi(-1,-1,-1),"Height can't be negative.")
        user.assertEqual(bm.calculate_bmi(5,-1,0),"Height can't be negative.")
        user.assertEqual(bm.calculate_bmi(0,12,0),"Inches value should be in between 0 to 11.")
        user.assertEqual(bm.calculate_bmi(10,0,0),"Height can't be 10 feet or more.")
        user.assertEqual(bm.calculate_bmi(10,0,-1),"Height can't be 10 feet or more.")
        user.assertEqual(bm.calculate_bmi(10,0,140),"Height can't be 10 feet or more.")
        user.assertEqual(bm.calculate_bmi(10,0,1500),"Height can't be 10 feet or more.")
        user.assertEqual(bm.calculate_bmi(10,0,1501),"Height can't be 10 feet or more.")

    def test_bmi_weight(user):
        bm = bmi_calculation()
        user.assertEqual(bm.calculate_bmi(5,10,0),"Weight can't be negative or zero.")
        user.assertEqual(bm.calculate_bmi(5,10,-1),"Weight can't be negative or zero.")
        user.assertEqual(bm.calculate_bmi(6,3,1500),"Your bmi is 192.0 and you are considered as obese.")

    def test_bmi_correct(user):
        bm=bmi_cal()
        user.assertEqual(bm.calculate_bmi(5,0,140),"Your bmi is 28.0 and you are considered as over weight.")
        
