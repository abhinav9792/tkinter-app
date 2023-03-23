import json
from datetime import datetime
from app import db
import requests
from bs4 import BeautifulSoup


def get_investment_price():
    URL = "https://coinranking.com/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')

    price_data = {}
    # count = 5
    for name, price_td in zip(soup.findAll('a', attrs = {'class':'profile__link'}), soup.findAll('td', attrs={'class':'table__cell table__cell--2-of-8 table__cell--responsive'})):
        price = price_td.find("div")
        price_data[name.text.strip()] = "".join(filter(lambda x: x if x.isdigit() or x == '.' else '', price.text.strip()))
        # count -= 1
        # if not count:
        #     break

    URL = "https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF&guccounter=1"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    gold=soup.find('fin-streamer', attrs = {'class':"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    price_data["Gold"] = gold

    URL = "https://finance.yahoo.com/quote/SI%3DF?p=SI%3DF"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')

    silver=soup.find('fin-streamer', attrs={'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    price_data['Silver'] = silver

    return price_data


class ClientRoutes:
    def login(self, *args, **kwargs):
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE email=%s',
            (kwargs.get('email'),)
        )
        data = cur.fetchone()
        if data and data[1] == kwargs.get('password'):
            cur.execute(
                'UPDATE user SET `vollet`=`vollet`+%s WHERE email=%s', (kwargs.get('cash', 0), kwargs.get('email'),)
            )
            cur.close()
            db.commit()
            return json.dumps({'status': True, 'new': False, 'username': kwargs.get('email')}), True, kwargs.get('email'), kwargs.get('password')
        else:
            cur.execute(
                'INSERT INTO user (email, password, vollet, datetime) VALUES (%s, %s, %s, %s)',
                (kwargs.get('email'), kwargs.get('password'), kwargs.get('cash', 0), datetime.now())
            )
            cur.close()
            db.commit()
            return json.dumps({'status': True, 'new': True, 'username': kwargs.get('email')}), True, kwargs.get('email'), kwargs.get('password')

    def stock_price(self, *args, **kwargs):
        response = get_investment_price()
        print(response)
        return json.dumps(response)

    def get_investments(self, **kwargs):
        cur = db.cursor()
        cur.execute(
            'select id, stock_name, buy_price from bought_stock where user=%s', (kwargs.get('email'),)
        )
        data = cur.fetchall()
        return json.dumps({'data': data})

    def get_user_cash(self, **kwargs):
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE email=%s',
            (kwargs.get('email'),)
        )
        data = cur.fetchone()
        cur.close()
        if data is None:
            return json.dumps({'cash': float(0)})
        cash = data[2]
        return json.dumps({'cash': float(cash)})

    def confirm_buy(self, **kwargs):
        option = kwargs['option']
        price = float(kwargs['price'])
        amount = int(kwargs['amount'])
        name = kwargs['name']
        if str(option) == '1':  # amount
            buy_price = amount
            buy_quantity = price // buy_price
        else:  # quantity
            buy_quantity = amount
            buy_price = price // buy_quantity

        cur = db.cursor()
        dt = datetime.now()
        cur.execute(
            'insert into bought_stock (user, stock_name, buy_price, buy_quantity, price_at_buy, date) values(%s, %s, %s, %s, %s, %s)',
            (kwargs.get('email'), name, buy_price, buy_quantity, price, dt)
        )
        cur.execute(
            'UPDATE user set vollet=vollet-%s WHERE email=%s', (buy_price, kwargs.get('email'))
        )
        db.commit()
        cur.close()
        return json.dumps({'currency': name, 'quantity': buy_quantity, 'amount': buy_price, 'date': str(dt)})

    def sell_stock(self, **kwargs):
        id_ = kwargs['id']
        amount = kwargs['amount']
        cur = db.cursor()
        cur.execute(
            'DELETE FROM bought_stock where id=%s', (id_,)
        )
        cur.execute(
            'UPDATE user SET vollet=vollet+%s where email=%s', (amount, kwargs['email'])
        )
        db.commit()
        cur.close()
        return json.dumps({'currency': kwargs['name'], 'price': amount})

    def update_cash(self, **kwargs):
        cur = db.cursor()
        cur.execute(
            'UPDATE user SET vollet=vollet+%s where email=%s', (kwargs.get('amount'), kwargs['email'])
        )
        return json.dumps({'status': True})
















