class Time_Series:
    def __init__(self, sym, freq='daily', api='AV'):
        self.sym = sym
        self.freq = freq
        self.api = api
