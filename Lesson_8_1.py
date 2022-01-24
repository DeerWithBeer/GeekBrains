import re


def email_parse(email_address='username@domain.com'):
    result = dict()
    validate_symbol = r'[A-Z a-z 0-9 # ! % $ ‘ & + * – / = ? ^ _`. { | } ~]+'
    if not re.fullmatch(validate_symbol + r'@' + validate_symbol + r'[.]' + validate_symbol, email_address):
        raise ValueError('Неверный Email')
    result['username'] = re.search(validate_symbol + r'[^@]', email_address).group()
    result['domain'] = re.search(r'[^@]' + validate_symbol + r'[.]' + validate_symbol, email_address).group()
    return result


print(email_parse())
