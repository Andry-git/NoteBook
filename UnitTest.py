import unittest
import TimeInterval
import parserJSON

class Test(unittest.TestCase):
    
    def test_TimeInterval1(self):
        self.assertFalse(TimeInterval.TimeInterval("01/01/2003, 00:01",
                                                "01/01/2003, 00:02",
                                                "01/01/2003, 00:03",
                                                "01/01/2003, 00:04"))
        
    def test_TimeInterval2(self):
        self.assertTrue(TimeInterval.TimeInterval("01/01/2003, 00:01",
                                                "01/01/2003, 00:04",
                                                "01/01/2003, 00:02",
                                                "01/01/2003, 00:03"))
    def test_TimeInterval3(self):
        self.assertTrue(TimeInterval.TimeInterval("01/01/2003, 00:01",
                                                "01/01/2003, 00:03",
                                                "01/01/2003, 00:02",
                                                "01/01/2003, 00:04"))
    def test_TimeInterval4(self):
        self.assertTrue(TimeInterval.TimeInterval("01/01/2003, 00:01",
                                                "01/01/2003, 00:02",
                                                "01/01/2003, 00:02",
                                                "01/01/2003, 00:04"))
                                                
    def test_ProverkaInterval1(self):
        self.assertFalse(TimeInterval.ProverkaInterval("01/01/2003, 00:02","01/01/2003, 00:01"))
        
    def test_ProverkaInterval2(self):
        self.assertTrue(TimeInterval.ProverkaInterval("01/01/2003, 00:01","01/01/2003, 00:02"))
    
if __name__ == '__main__':
    unittest.main()