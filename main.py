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


class Electric:
    """
    Represents an Electric object powered by a battery.

    Attributes:
    - battery (int): The battery level of the Electric object.
    """
    def __init__(self, battery: int) -> None:
        """
        Initializes a new Electric object with a specified battery level.

        Args:
        - battery (int): The initial battery level of the Electric object.
        """
        self.__battery = battery

    def charge(self) -> None:
        """
        Charges the battery of the Electric object to 100%.
        """
        self.__battery = 100


class ElectricCar(Vehicle, Electric):
    """
    Represents an electric car, which is both a type of Vehicle and an electronic device powered by a battery.

    Inherits from Vehicle and Electric classes.
    """
    pass


class ElectricMoto(Moto, Electric):
    """
    Represents an electric motorcycle, which is both a type of Moto and an electronic device powered by a battery.

    Inherits from Moto and Electric classes.
    """
    pass


def main() -> None:
    """
    Main function to demonstrate the usage of ElectricCar and ElectricMoto classes.
    """

    car_electric = ElectricCar("BMW", "X1")
    moto_electric = ElectricMoto("Mercedes", "S500", 2)
    print(car_electric.get_info())
    print(moto_electric.get_info())
    print(ElectricCar.mro())
    print(ElectricMoto.mro())


if __name__ == "__main__":
    main()
