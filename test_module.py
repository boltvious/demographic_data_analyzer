import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_calculate_demographic_data(self):
        result = calculate_demographic_data(print_data=False)
        
        # Check if the return dictionary has the correct keys
        expected_keys = [
            'race_count', 'average_age_men', 'percentage_bachelors',
            'higher_education_rich', 'lower_education_rich',
            'min_work_hours', 'rich_percentage',
            'highest_earning_country', 'highest_earning_country_percentage',
            'top_IN_occupation'
        ]
        self.assertEqual(list(result.keys()), expected_keys)
        
        # Validate a few known results from the dataset
        self.assertIsInstance(result['race_count'], pd.Series)
        self.assertEqual(result['average_age_men'], 39.4)
        self.assertEqual(result['percentage_bachelors'], 16.4)
        self.assertEqual(result['higher_education_rich'], 46.5)
        self.assertEqual(result['lower_education_rich'], 17.4)
        self.assertEqual(result['min_work_hours'], 1)
        self.assertEqual(result['rich_percentage'], 10.0)
        self.assertEqual(result['highest_earning_country'], 'Iran')
        self.assertEqual(result['highest_earning_country_percentage'], 41.9)
        self.assertEqual(result['top_IN_occupation'], 'Prof-specialty')

if __name__ == '__main__':
    unittest.main()
