import unittest
from TimeInterval import TimeInterval

class TimeInterval(unittest.TestCase):
  def setUp(self):
    self.TimeInterval = TimeInterval()
  #Each test method starts with the keyword test_
  def TimeInterval(self):
    self.assertTrue(self.TimeInterval.TimeInterval(1,5,5,8))
    self.assertTrue(self.TimeInterval.TimeInterval(1,7,5,8))
    self.assertTrue(self.TimeInterval.TimeInterval(5,8,1,9))
    self.assertTrue(self.TimeInterval.TimeInterval(1,5,5,8))
    self.failIf(self.TimeInterval.TimeInterval(1,5,7,8))
  def ProverkaInterval(self):
    self.assertTrue(self.TimeInterval.ProverkaInterval(1,5))
    self.failIf(self.TimeInterval.ProverkaInterval(5,1))

if __name__ == "__run__":
  unittest.run()