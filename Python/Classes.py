class Calculator:
    def __init__(self, initial_value=0):
        """
        Constructor method to initialize the calculator with an initial value.
        """
        self.value = initial_value
    
    def add(self, amount):
        """
        Adds the given amount to the current value.
        """
        self.value += amount
        return self.value
    
    def subtract(self, amount):
        """
        Subtracts the given amount from the current value.
        """
        self.value -= amount
        return self.value
    
    def multiply(self, factor):
        """
        Multiplies the current value by the given factor.
        """
        self.value *= factor
        return self.value
    
    def divide(self, divisor):
        """
        Divides the current value by the given divisor.
        """
        if divisor != 0:
            self.value /= divisor
        else:
            print("Error: Cannot divide by zero.")
        return self.value
    
    def reset(self):
        """
        Resets the current value to zero.
        """
        self.value = 0
        return self.value

# Creating an instance of the Calculator class
calc = Calculator()

# Calling methods on the instance
print("Initial value:", calc.value)
print("After adding 10:", calc.add(10))
print("After subtracting 3:", calc.subtract(3))
print("After multiplying by 4:", calc.multiply(4))
print("After dividing by 2:", calc.divide(2))
print("After reset:", calc.reset())

print("After adding 10:", calc.add(30))
