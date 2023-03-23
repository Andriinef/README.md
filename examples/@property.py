class MyClass:
    def __init__(self, attr: str):
        self._attr = attr

    @property
    def attr_in(self):
        return self._attr

    @attr_in.setter
    def attr_out(self, new_value: str):
        self._attr = new_value


obj = MyClass("value")
print(obj.attr_in)  # 'value'
print(obj.attr_out)  # 'value'
obj.attr_out = "new_value"
print(obj.attr_out)  # 'new_value'
