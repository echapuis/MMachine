import json, requests

class Time_Series:
    def __init__(self, sym, start_date, end_date, freq='daily'):
        self.sym = sym
        self.freq = freq
