from sikuli import *
import unittest

class UnitTestA(unittest.TestCase):

    def test_uitest1(self):
        usernameLable = find("1407072367275.png")
        click(Location(usernameLable.x + 50, usernameLable.y + 50))
        type("a", KEY_CTRL)
        type("abc")
        
        click(Location(usernameLable.x - 50, usernameLable.y))
        
        passwordLable = find("1407072805844.png")
        click(Location(passwordLable.x + 50, passwordLable.y + 50))
        type("a", KEY_CTRL)
        type("abc")
