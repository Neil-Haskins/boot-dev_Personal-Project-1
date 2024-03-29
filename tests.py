import unittest
import parser
import packer
import filters
import tests_data

class Tests(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(
            True,
            True
        )

    def test_filter_dict_by_path(self):
        c_dict = tests_data.test_dict
        self.assertEqual(
            filters._filter_dict_by_path(c_dict, ['Jan', 'Record high']),
            {
                'Vancouver, Canada, North America': {
                    'Climate': {
                        'Jan': {
                            'Record high': 15.3
                        }
                    }
                }, 
                'Tokyo, Japan, Asia': {
                    'Climate': {
                        'Jan': {
                            'Record high': 22.6
                        }
                    }
                }
            }
        )
        self.assertEqual(
            filters._filter_dict_by_path(c_dict, [['Jan', 'Mar'], 'Record high']),
            {
                'Vancouver, Canada, North America': {
                    'Climate': {
                        'Jan': {
                            'Record high': 15.3
                        },
                        'Mar': {
                            'Record high': 20.0
                        }
                    }
                }, 
                'Tokyo, Japan, Asia': {
                    'Climate': {
                        'Jan': {
                            'Record high': 22.6
                        },
                        'Mar': {
                            'Record high': 25.3
                        }
                    }
                }
            }
        )
    
    def test_filter_months(self):
        self.assertEqual(
            filters.filter_months(tests_data.test_dict, 'Feb', 'Apr'),
            {
                'Vancouver, Canada, North America': {
                    'Climate': {
                        'Feb': {
                            'Record high': 18.4,
                            'Record low': -16.1
                        },
                        'Mar': {
                            'Record high': 20.0,
                            'Record low': -9.4
                        },
                        'Apr': {
                            'Record high': 26.1,
                            'Record low': -3.3,
                        }
                    }
                }, 
                'Tokyo, Japan, Asia': {
                    'Climate': {
                        'Feb': {
                            'Record high': 24.9,
                            'Record low': -7.9
                        },
                        'Mar': {
                            'Record high': 25.3,
                            'Record low': -5.6
                        },
                        'Apr': {
                            'Record high': 29.2,
                            'Record low': -3.1,
                        }
                    }
                }
            }
        )
        self.assertEqual(
            filters.filter_months(tests_data.test_dict, 'Dec', 'Jan'),
            {
                'Vancouver, Canada, North America': {
                    'Climate': {
                        'Jan': {
                            'Record high': 15.3,
                            'Record low': -17.8
                        },
                        'Dec': {
                            'Record high': 15.0,
                            'Record low': -17.8,
                        },
                    }
                }, 
                'Tokyo, Japan, Asia': {
                    'Climate': {
                        'Jan': {
                            'Record high': 22.6,
                            'Record low': -9.2
                        },
                        'Dec': {
                            'Record high': 24.8,
                            'Record low': -6.8,
                        },
                    }
                }
            }
        )

    


if __name__ == "__main__":
    unittest.main()



# def get_max_temp(my_dict):
#     cities_2 = _filter_dict_by_path(my_dict, ['Climate', 'Record high'])
#     print(cities_2)

#     print('\nThese should both be empty:')
#     print(_filter_dict_by_path(my_dict, ['Climate', 'jsjhdhbvn']))
#     print(_filter_dict_by_path(my_dict, ['tvuyih', 'Record high']))

#     print('\nThis should show everything under "Climate":')
#     print(_filter_dict_by_path(my_dict, ['Climate']))

#     print('\nThis should show all "Record high"s:')
#     print(_filter_dict_by_path(my_dict, ['Record high']))

#     print('\nThis should show everything under "Jan":')
#     print(_filter_dict_by_path(my_dict, ['Jan']))