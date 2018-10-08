class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, obj, obj_type):
        return self.amount

    @staticmethod
    def _get_commission(value, commission):
        return value - value * commission

    def __set__(self, obj, value):
        self.amount = self._get_commission(value, obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
