class Car:

    def __init__(self, engine, gear) -> None:
        self.engine = engine
        self.gear = gear

    def __repr__(self) -> str:
        return f"Car : {self.engine} {self.gear}"


class ElectricCar(Car):
    def __init__(self, engine, gear) -> None:
        self.fuel_type = "Electric"
        self.model, self.price = None, None
        super().__init__(engine, gear)

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def __repr__(self) -> str:
        return f"Car : {self.engine} {self.gear}, {self.fuel_type}, {self.price}, {self.model}"


electric_1 = ElectricCar("1500cc", "0")
electric_1.set_price(50000)
electric_1.set_model("VXi")
