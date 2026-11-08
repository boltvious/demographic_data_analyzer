import unittest
from demographic_data_analyzer import calculate_demographic_data

if __name__ == '__main__':
    print("--- Menjalankan Analisis Data Demografi ---")
    calculate_demographic_data(print_data=True)

    print("\n--- Menjalankan Unit Test ---")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_module')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
