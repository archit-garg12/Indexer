class Token_Attributes:
    def __init__(self):
        self._frequency = 0
        self._positional_index = {}

    def frequency(self) -> int:
        return self._frequency

    def positional_index(self) -> set:
        return self.positional_index

    def update_positional_index(self, location: int) -> None:
        self._positional_index.add(location)

    def update_frequency(self) -> None:
        self._frequency += 1
