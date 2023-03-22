#Write a Python class to get all possible unique subsets from a set of distinct integers Input: [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class SubsetGenerator:
    def __init__(self, input_set):
        self.input_set = input_set
        self.subsets = []
    def generate_subsets(self):
        self._generate_helper([], 0)
        return self.subsets
    def _generate_helper(self, current_subset, start_index):
        self.subsets.append(current_subset)
        for i in range(start_index, len(self.input_set)):
            self._generate_helper(current_subset + [self.input_set[i]], i + 1)