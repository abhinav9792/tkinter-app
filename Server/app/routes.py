import json
from datetime import datetime
from app import db


class ClientRoutes:
    def login(self, *args, **kwargs):
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM user WHERE email=%s',
            (kwargs.get('email'),)
        )
        data = cur.fetchone()
        print(data)
        if data and data[1] == kwargs.get('password'):
            cur.execute(
                'UPDATE user SET `vollet`=`vollet`+%s WHERE email=%s', (kwargs.get('cash', 0), kwargs.get('email'),)
            )
            db.commit()
            return json.dumps({'status': True, 'new': False, 'username': kwargs.get('email'),
                               'password': kwargs.get('password')}), True, kwargs.get('email'), kwargs.get('password')
        else:
            cur.execute(
                'INSERT INTO user (email, password, vollet, datetime) VALUES (%s, %s, %s, %s)',
                (kwargs.get('email'), kwargs.get('password'), kwargs.get('cash', 0), datetime.now())
            )
            db.commit()
            return json.dumps({'status': True, 'new': True, 'username': kwargs.get('email'),
                               'password': kwargs.get('password')}), True, kwargs.get('email'), kwargs.get('password')
