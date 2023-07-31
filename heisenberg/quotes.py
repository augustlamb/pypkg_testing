import random

quotes = [
    "Stay out of my territory.",
    "We're done when I say we're done.",
    "If that's true, if you don't know who I am, then maybe your best course... would be to tread lightly.",
    "It's over. I won.",
    "I am the one who knocks.",
    "Why are you blue?",
    "Apply yourself."
]

def get_quote():
    '''Returns a random Heisenberg quote.'''
    idx = random.randint(0, len(quotes))
    print(quotes[idx])