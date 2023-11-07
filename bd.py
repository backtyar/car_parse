from datetime import datetime
from decouple import config
from peewee import *

db = PostgresqlDatabase(database=config('DATABASE'),
                        user=config('USRNAME'),
                        password=config('PASSWORD'),
                        host=config("HOST"),
                        port=config('PORT'),)

class Car(Model):
    price_som = IntegerField(verbose_name='Цена в соaмах')
    price_dollar = IntegerField(verbose_name='Цена в долларах')
    name = CharField(max_length=100,verbose_name='Название')
    image = CharField(max_length=100,verbose_name='картинка')
    description = TextField(verbose_name='картинка')
    view = IntegerField(default=0,verbose_name='количество просмотров')

    class Meta:
        database = db
        db_table = 'car'


db.connect()
db.create_tables([Car])

with open('range_rover.csv', 'r') as fp:
    for i, v in enumerate(fp):
        if i == 0:
            continue
        else:
            new_list = v.split(',')

            Car.create(price_som=int(new_list[0][2:].replace(' ','')), price_dollar=int(new_list[1][:-4].replace(' ','')), name=new_list[2],
                       image=new_list[3], description=new_list[4],view=int(new_list[5]))


