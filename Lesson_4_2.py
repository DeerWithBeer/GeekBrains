
import requests
import datetime
def currency_rates(code_name_in):
    #import pdb
    #pdb.set_trace()
    code=str(code_name_in).upper()
    code=code.replace('{','').replace("'",'').replace('}','')
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if (response.status_code != 200):
        print("Error Connection")
        return -1
    response = response.text
    position = response.find(f'<CharCode>{code}</CharCode>')
    if position == -1:
        print("Неверный код валюты")
        return None
    position=[response.find('<Value>',position)+7, response.find('</Value>',position)]
    date_of_curse=response[response.find('" name')-10:response.find('" name')]
    date_of_curse=datetime.datetime.strptime(date_of_curse, '%d.%m.%Y').date()
    return (float(response[position[0]:position[1]].replace(',','.')),date_of_curse)

if __name__ == '__main__':
    import sys
    var = sys.argv[1]
    print(f'Курс {var}:{currency_rates({var})[0]} на {currency_rates({var})[1]}')
