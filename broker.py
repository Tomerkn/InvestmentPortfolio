import requests

class Broker:
    """
    מחלקת מנהל התיק - מבצעת פעולות קנייה, מכירה ועדכון מחירים.
    """
    def __init__(self, model):
        self.model = model
        self.api_key = "87RYKHP1CUPBGWY1"

    def buy(self, security, quantity):
        """
        קנייה של נייר ערך מסוים והוספה לתיק ההשקעות.
        """
        if security.security_type == 2:  # אג"ח
            updated_price = security.price
        else:
            updated_price = self.update_price(security.name)
        security.price = updated_price
        self.model.add_security(
            security.name,
            security.price,
            security.variance,
            security.security_type,
            quantity
        )
        print(f"נרכשו {quantity} יחידות של {security.name} במחיר מעודכן של {updated_price} ש״ח")

    def sell(self, name, quantity):
        """
        מכירה של נייר ערך מסוים.
        """
        updated_price = self.update_price(name)
        portfolio = self.model.get_portfolio()
        for sec in portfolio:
            if sec[1] == name:
                if sec[5] < quantity:
                    raise ValueError("כמות לא מספיקה למכירה")
                total_price = updated_price * quantity
                if sec[5] == quantity:
                    self.model.clear_portfolio(name)
                else:
                    self.model.update_quantity(name, sec[5] - quantity)
                print(f"נמכרו {quantity} יחידות של {name} בסכום כולל של {total_price} ש״ח")
                return
        raise ValueError("נייר ערך לא נמצא בתיק")

    def update_price(self, symbol):
        """
        עדכון מחיר נייר ערך מ-API.
        """
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()

        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            updated_price = float(data["Global Quote"]["05. price"])
            print(f"מחיר מעודכן לנייר {symbol}: {updated_price} ש״ח")
            return updated_price
        else:
            raise ValueError(f"לא ניתן לעדכן את המחיר עבור {symbol}")
