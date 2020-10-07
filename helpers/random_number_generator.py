from random import Random

seed = 0
min_value = 0
max_value = 15

class RandomNumberGenerator:
    def __init__(self, min_value, max_value, seed=0):
        self.sequence = []
        self.seed = 0
        self.min_value = min_value
        self.max_value = max_value

    def generate_sequence(self, length):
        result = []
        random = Random(seed)
        for _ in range(length):
            result.append(random.randint(self.min_value, self.max_value))

        self.sequence += result
        return self.sequence
