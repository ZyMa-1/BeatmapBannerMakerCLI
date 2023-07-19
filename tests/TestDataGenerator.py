from typing import List, Dict


class TestDataGenerator:
    @staticmethod
    def generate_test_data_from_list(data: List[List[str]]) -> List[List[str]]:
        """
        Generates test data with O(n^2 * m), not O(m^n).
        Just 1 test case for every parameter with whatever other arguments to check if that one parameter works fine.

        For example: [[0, 1], [2, 3, 4]] -> [[0, 2], [1, 2], [0, 2], [0, 3], [0, 4]]
        """
        res_test_data = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                current_test_data = []
                for k in range(len(data)):
                    if k != i:
                        current_test_data.append(data[k][0])

                current_test_data.insert(i, data[i][j])

                res_test_data.append(current_test_data)

        return res_test_data

    @staticmethod
    def generate_test_data_from_dict(data: Dict[str, List[str]]) -> List[Dict[str, str]]:
        """
        Generates test data with O(n^2 * m), not O(m^n).
        Just 1 test case for every parameter with whatever other arguments to check if that one parameter works fine.

        For example input:
        {
            'entry_1': [0, 1],
            'entry_2': [2, 3, 4]
        }

        Should result in following output:
        [
            {'entry_1': 0, 'entry_2' 2},
            {'entry_1': 1, 'entry_2' 2},
            {'entry_1': 0, 'entry_2' 2},
            {'entry_1': 0, 'entry_2' 3},
            {'entry_1': 0, 'entry_2' 4}
        ]

        """
        res_test_data = []
        for key, val in data.items():
            for j in range(len(val)):
                current_test_data = {}
                for k2, val2 in data.items():
                    if k2 != key:
                        current_test_data[k2] = val2[0]

                current_test_data[key] = val[j]

                res_test_data.append(current_test_data)

        return res_test_data
