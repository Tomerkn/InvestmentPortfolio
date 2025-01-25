from model import Model
from stock import Stock, Bond
from broker import Broker
from ai_agent import AI_Agent
import matplotlib.pyplot as plt

def translate_security_names(data):
    translations = {"אג״ח מדינה": "Government Bond"}
    return [(translations.get(name, name), quantity) for name, quantity in data]

def create_portfolio_graph(data):
    translated_data = translate_security_names(data)
    names = [item[0] for item in translated_data]
    quantities = [item[1] for item in translated_data]

    plt.figure(figsize=(10, 6))
    plt.bar(names, quantities, color='skyblue')
    plt.title('Investment Portfolio Distribution', fontsize=16)
    plt.xlabel('Securities', fontsize=14)
    plt.ylabel('Quantity', fontsize=14)
    plt.tight_layout()
    plt.show()

# אובייקטים
model = Model()
broker = Broker(model)
ai_agent = AI_Agent(risk_level=1.5)

# מניות ואג"ח
apple = Stock("AAPL", 150, 1.2, 1)
google = Stock("GOOGL", 200, 1.5, 1)
bond = Bond("אג״ח מדינה", 100, 0.5, 2)

# פעולות
broker.buy(apple, 10)
broker.buy(google, 5)
broker.buy(bond, 3)

# ייעוץ
advice = ai_agent.get_advice(apple)
print(f"ייעוץ AI עבור AAPL: {advice}")

broker.sell("AAPL", 5)

portfolio = model.get_portfolio()
print("תיק ההשקעות הנוכחי:")
for sec in portfolio:
    print(sec)

portfolio_data = model.get_portfolio_for_graph()
create_portfolio_graph(portfolio_data)
