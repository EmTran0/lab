class Account:
    """
    A class representing details for an account object
    """

    def __init__(self, name: str) -> None:
        """
        Function to set up object.
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to add to account balance.
        :param amount: Amount deposited
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Function to subtract from account balance.
        :param amount: Amount removed
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access an account's balance.
        :return: An account's balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access an account's name.
        :return: An account's name
        """
        return self.__account_name
