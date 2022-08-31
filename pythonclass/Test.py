class Test:
    def __init__(self) -> None:
        self.name = "Huang"

    def hello(self, param: int) -> bool:
        """Print hello.

        Args:
            param (int): Refer to time section.

        Returns:
            bool: The sitution of execution.
        """
        if param == 1:
            print("Hello, {} good morning!".format(self.name))
            return True
        if param == 2:
            print("Hello, {} good afternoon!".format(self.name))
            return True
        if param == 3:
            print("Hello, {} good evening!".format(self.name))
            return True

        return False
