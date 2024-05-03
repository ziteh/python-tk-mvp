class Model:
    def __init__(self):
        self.data: float = 5

    def get_data(self) -> float:
        print("                 |                  | [M] get_data()")
        return self.data

    def set_data(self, value: float):
        print(f"                 |                  | [M] set_data({value})")
        self.data = value
