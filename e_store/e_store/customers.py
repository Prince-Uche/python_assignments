class Customers:
    def __init__(self, name, email, password, phone_number, age, home_address, billing_information):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone_number = phone_number
        self.__age = age
        self.__home_address = home_address
        self.__billing_information = billing_information
        self.__cart = []