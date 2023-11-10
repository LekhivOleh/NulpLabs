class Pool:
    def __init__(self, address, volume, max_visitors, name, price_per_hour):
        self.__address = address
        self.__volume = volume
        self.__max_visitors = max_visitors
        self.name = name
        self.price_per_hour = price_per_hour

    def get_address(self):
        return self.__address

    def get_volume(self):
        return self.__volume

    def get_max_visitors(self):
        return self.__max_visitors

    def __str__(self):
        return f"{self.__address}, {self.__volume}, {self.__max_visitors}, {self.name}, {self.price_per_hour}"

    def __repr__(self):
        return f"{self.__address}, {self.__volume}, {self.__max_visitors}, {self.name}, {self.price_per_hour}"

    def __del__(self):
        """
        """

