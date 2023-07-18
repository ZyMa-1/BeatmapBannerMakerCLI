from typing import List


class TestDataGenerator:
    @staticmethod
    def generate_test_data(data: List[List[str]]):
        """
        Generates test data with O(n^2 * m), not O(m^n).
        Just 1 test case for every parameter with whatever other arguments to check if that one parameter works fine.
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
