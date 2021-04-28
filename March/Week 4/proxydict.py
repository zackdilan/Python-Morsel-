#from abc import ABC
from collections.abc import Mapping


class ProxyDict(Mapping):

    def __init__(self, input_dict):
        super().__init__()
        self.input_dict = input_dict

    def __len__(self):
        return len(self.input_dict)

    def __getitem__(self, item):
        return self.input_dict[item]

    def __iter__(self):
        pass

    def __repr__(self):
        ProxyDict({'name': 'Trey Hunner', 'active': False})
        ```

        return f"ProxyDict({self.keys()}: {self.values()}"

    def keys(self):
        return self.input_dict.keys()

    def values(self):
        return self.input_dict.values()

    def items(self):
        return self.input_dict.items()




