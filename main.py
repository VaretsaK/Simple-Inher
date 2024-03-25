class Vehicle:
    """
    Represents a generic vehicle.

    Attributes:
    - maker (str): The maker of the vehicle.
    - model (str): The model of the vehicle.
    """
    def __init__(self, maker: str, model: str) -> None:
        """
        Initializes a new Vehicle object.

        Args:
        - maker (str): The maker of the vehicle.
        - model (str): The model of the vehicle.
        """
        self.maker = maker
        self.model = model

    def get_info(self) -> str:
        """
        Returns a string representing the maker and model of the vehicle.

        Returns:
        - str: A string representation of the maker and model of the vehicle.
        """
        return f"{self.maker}, model: {self.model}"


class Car(Vehicle):
    """
    Represents a car, which is a type of vehicle.

    Inherits from Vehicle class.
    """
    def __init__(self, maker: str, model: str, wheels: int) -> None:
        """
        Initializes a new Car object.

        Args:
        - maker (str): The maker of the car.
        - model (str): The model of the car.
        - wheels (int): The number of wheels the car has.
        """
        super().__init__(maker, model)
        self.wheels = wheels


class Moto(Vehicle):
    """
    Represents a moto, which is a type of vehicle.

    Inherits from Vehicle class.
    """
    def __init__(self, maker: str, model: str, wheels: int) -> None:
        """
        Initializes a new Moto object.

        Args:
        - maker (str): The maker of the motorcycle.
        - model (str): The model of the motorcycle.
        - wheels (int): The number of wheels the moto has.
        """
        super().__init__(maker, model)
        self.wheels = wheels


def main() -> None:
    """
    Main function to demonstrate the usage of Car and Moto classes.
    """
    car1 = Car("BMW", "X5", 4)
    moto1 = Moto("Suzuki", "GSX-R600", 2)
    print(car1.get_info())
    print(moto1.get_info())


if __name__ == "__main__":
    main()
