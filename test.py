
import unittest
import numpy as np
from assignment import analyze_ab_test

class TestABTesting(unittest.TestCase):
    def test_analyze_ab_test(self):
        # Create sample data for control and experiment groups
        control_group = np.random.normal(loc=10, scale=2, size=100)
        experiment_group_significant = np.random.normal(loc=12, scale=2, size=100)
        experiment_group_insignificant = np.random.normal(loc=10.5, scale=2, size=100)

        # Test for a significant difference
        self.assertTrue(analyze_ab_test(control_group, experiment_group_significant))

        # Test for no significant difference
        self.assertFalse(analyze_ab_test(control_group, experiment_group_insignificant))

if __name__ == '__main__':
    unittest.main()
