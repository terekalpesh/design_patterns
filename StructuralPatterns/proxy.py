# Proxy design pattern

class College:
    def studying_in_college(self):
        print('Studying In College...')

class CollegeProxy:
    def __init__(self, feebalance):
        self.feebalance = feebalance
        self.college = None

    def studying_in_college(self):
        if self.feebalance <= 500:
            self.college = College()
            self.college.studying_in_college()
        else:
            print('Your fee balance is greater than 500, first pay the fee.')


college_proxy = CollegeProxy(501)
college_proxy.studying_in_college()