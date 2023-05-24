# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return sum(self.data)/len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n//2
        if n%2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid])/2
        else : 
            return sorted_data[mid]
        
    def mode(self):
        frequencies = {}
        for value in self.data:
            frequencies[value] = frequencies.get(value, 0) + 1
        max_frequency = max(frequencies.values())
        modes = [value for value, frequency in frequencies.items() if frequency == max_frequency]
        return modes
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def variance(self):
        mean = self.mean()
        return sum((x - mean)**2 for x in self.data)/ len(self.data)
    
    def standard_deviation(self):
        return self.variance()** 0.5
    
    def minimum(self):
        return min(self.data)
    
    def maximum(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def percentile(self, percentile):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        index = (percentile / 100) * (n - 1)
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower = sorted_data[int(index)]
            upper = sorted_data[int(index) + 1]
            return lower + (upper - lower)*(index % 1)

    def sum(self):
        return sum(self.data)
    
        
    def frequency_distribution(self):
        frequencies = {}
        for value in self.data:
            frequencies[value] = frequencies.get(value, 0) + 1
        return frequencies
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.minimum()) 
print('Max: ', data.maximum())
print('Range: ', data.range()) 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.standard_deviation()) 
print('Variance: ', data.variance()) 
print('Frequency Distribution: ', data.frequency_distribution())


# Exercises: Level 2
# 1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
        
    def add_income(self, amount, description):
        self.incomes.add((amount, description))
        
    def add_expenses(self, amount, description):
        self.expenses.add((amount, description))
    
    def total_income(self):
        return sum(amount for amount, _ in self.incomes)
    
    def total_expenses(self):
        return sum(amount for amount, _ in self.expenses)
    
    def account_info(self):
        return f"Account Information: \nName: {self.firstname} {self.lastname}\n"\
            f"Total Income: {self.total_income}\n Total Expenses : {self.total_expenses()}\n"\
                f"Account Balance: {self.account_balance()}"
    def account_balance(self):
        return self.total_income() - self.total_expenses()
    
    
account = PersonAccount("Ashley","Flower")
account.add_income(10000, "Salary")
account.add_income(5000,"Bonus")
account.add_expenses(3000, "Groceries")
account.add_expenses(2000,"Utilities")

print(account.account_info())