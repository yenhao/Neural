from datetime import datetime
import random
import numpy as np

class RandomNumber:
    """
    Random Number Generator 
    """
    def random(self, number = 5, upper = 0, lower = 1):
        """
        Input :
        number [Int] How many random number
        upper [Float] Upper bound
        lower [Float] Lower Bound

        Output:
        e.g.
        (
        [0.21847849415593434, 0.8534677532586386, 0.13292800530283566, 0.2181492681999555, 0.9555924797891898], 
        datetime.datetime(2017, 4, 19, 16, 17, 21, 645692), 
        datetime.datetime(2017, 4, 19, 16, 17, 21, 645723)
        )
        """
        start = datetime.now()
        random_list = [random.uniform(lower, upper) for _ in range(number)]
        end = datetime.now()
        return (random_list, start, end)

    def show(self, number = 5, upper = 0, lower = 1):
        """
        e.g.
        Random Number: 
        [0.9187906963594417, 0.6172421763627418, 0.7722049236314029, 0.9477594018354711, 0.021069555376928673]

        Cost Time:
        0:00:00.000024
        """
        rn = self.random(number, upper, lower)
        print('\nRandom Number: \n{}\n\nCost Time:\n{}\n'.format(rn[0], (rn[2]-rn[1])))

    def eva(self):
        """
        Evaluation via 100000 Number.
        Mean: 0.499021540693602
        STD: 0.2885785606571967
        """
        np_array = np.array(self.random(number = 100000)[0])
        print('\nEvaluation via 100000 Number.\nMean: {}\nSTD: {}\n'.format(np.mean(np_array), np.std(np_array)))
