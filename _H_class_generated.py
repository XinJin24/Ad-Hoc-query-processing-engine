class H:
    def __init__(self):
        self.attributes = {}
        self.attributes['cust'] = None
        self.attributes['1_max_quant'] = 0
        self.attributes['2_max_quant'] = 0

    def __getitem__(self, key):
        return self.attributes.get(key, None)

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def __repr__(self):
        return f'H({self.attributes})'
        
    def __contains__(self, key):
        return key in self.attributes
    