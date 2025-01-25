from abc import ABC, abstractmethod

class Security(ABC):
    """
    מחלקת בסיס לנייר ערך
    """
    def __init__(self, name, price, variance, security_type):
        self.name = name
        self.price = price
        self.variance = variance
        self.security_type = security_type

    @abstractmethod
    def calculate_risk(self):
        """
        פונקציה לחישוב סיכון של נייר ערך.
        """
        pass

class Stock(Security):
    """
    מחלקה שמייצגת מניה
    """
    def calculate_risk(self):
        alpha = 0.5
        beta = 0.3
        gamma = 0.2
        return alpha * self.price + beta * self.variance + gamma * self.security_type

class Bond(Security):
    """
    מחלקה שמייצגת אג"ח
    """
    def calculate_risk(self):
        alpha = 0.5
        beta = 0.3
        gamma = 0.2
        return alpha * self.price + beta * self.variance + gamma * self.security_type
