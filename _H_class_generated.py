class H:
    def __init__(self):
        self.attributes = {}
        self.attributes['cust'] = None
        self.attributes['_1_sum_quant'] = None
        self.attributes['_1_avg_quant'] = None
        self.attributes['_2_sum_quant'] = None
        self.attributes['_3_sum_quant'] = None
        self.attributes['_3_avg_quant'] = None

    def __getitem__(self, key):
        return self.attributes.get(key, None)

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def __repr__(self):
        return f'H({self.attributes})'
    