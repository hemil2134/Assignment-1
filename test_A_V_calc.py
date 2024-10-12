'''
TPRG 2131 Fall 2024 Assignment 1, Test file template.
Oct, 2024
Hemil Prajapati (100942152).
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s).


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''
# Importing functions from the A_V_calc module
from A_V_calc import area_square, volume_rectangle, area_circle, volume_cone, area_triangle

# Test function for the area_square function
def test_area_square():
    assert area_square(5) == 25.0
    assert area_square(18) == 324.0
    assert area_square(30) == 900.0

# Test function for the volume_rectangle function
def test_volume_rectangle():
    assert volume_rectangle(11,13,15) == 2145.0
    assert volume_rectangle(28,4,4) == 448.0
    assert volume_rectangle(10,8,23) == 1840.0

# Test function for the area_circle function
def test_area_circle():
    assert area_circle(13) == 530.9
    assert area_circle(11) == 380.1
    assert area_circle(66) == 13684.8

# Test function for the volume_cone function
def test_volume_cone():
    assert volume_cone(6,5) == 155.5
    assert volume_cone(14,11) == 1756.2
    assert volume_cone(37,17) == 11085.7

# Test function for the area_triangle function
def test_area_triangle():
    assert area_triangle(9,10) == 45.0
    assert area_triangle(16,21) == 168.0
    assert area_triangle(44,55) == 1210.0