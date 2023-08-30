import sqlalchemy.types as types
from sqlalchemy import LargeBinary

from src.credit_card.utils import CryptHandler


class CreditCardNumber(types.TypeDecorator):
    '''
        pre load to cypher credit_number
    '''

    impl = LargeBinary

    cache_ok = True

    def process_bind_param(self, value, dialect):
        crypt_handler = CryptHandler()
        crypt_handler.load_fernet()
        value = crypt_handler.encrypt(value)
        return value

    def process_result_value(self, value, dialect):
        crypt_handler = CryptHandler()
        crypt_handler.load_fernet()
        value = crypt_handler.decrypt(value)
        return value

    def copy(self, **kw):
        return CreditCardNumber(self.impl.length)
