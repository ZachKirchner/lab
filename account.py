class Account:
    def __init__(self, name: str):
        """
        This function initializes the account

        :param name: This is the name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        """
        This function adds a value to the account balance then returns True if added successfully and False if it
        failed.

        :param amount: This is the value to be added
        :return: A boolean value representing whether the addition succeeded or failed
        """
        if amount > 0:
            pass
        else:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float):
        """
        This functions subtracts a vlue from the account balance then returns True if subtracted successfully and
        False if it failed.

        :param amount: This is the value to be subtracted
        :return: A boolean value representing whether the subtraction succeeded or failed
        """
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        """
        This functions returns the account balance.

        :return: The account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        This function returns the name of the account.

        :return: The name of the account
        """
        return self.__account_name
