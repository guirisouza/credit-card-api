import calendar
from datetime import datetime

from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound
from fernet import Fernet


class CryptHandler:
    def __init__(self):
        self.key: str
        self.fernet: Fernet

    def _write_key(self):
        """
            Generate and save it into file
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    def _load_key(self):
        """
            Loads the key from the current directory named `key.key`
        """
        self.key = bytes(open("key.key", "rb").read())
        self.fernet = Fernet(self.key)

    def load_fernet(self):
        """
            Runner to load or write fernet key token
        """
        try:
            self._load_key()
        except FileNotFoundError:
            self._write_key()

    def encrypt(self, data: str) -> bytes:
        """
            Perform encripty data
        :param data: data to be encrypted
        :return:
        """
        return self.fernet.encrypt(data)

    def decrypt(self, data: bytes) -> str:
        """
            Perform decrypt data
        :param data: data to be decrypted
        :return:
        """
        return self.fernet.decrypt(data)


class CreditCardHelper:

    @classmethod
    def credit_card_number_validator(cls, number: str) -> bool:
        """
            Check if credit card number is valid
        :return: boolean
        """
        return CreditCard(number=number).is_valid()

    @classmethod
    def get_brand_card(cls, number: str) -> str:
        """
            Get credit card brand by number
        :return: string
        """
        try:
            return CreditCard(number=number).get_brand()
        except BrandNotFound:
            return "Visa" # Todo: is Visa the default? Should be a param of the function or even come from the configs?

    @classmethod
    def parse_date(cls, date: str) -> datetime:
        month, year = date.split('/')
        last_day_month = calendar.monthrange(int(year), int(month))[1]
        return datetime(int(year), int(month), last_day_month)
