from typing import List

from .connector import StoreConnector
from pandas import DataFrame, Series
from datetime import datetime

"""
    В данном модуле реализуется API (Application Programming Interface)
    для взаимодействия с БД с помощью объектов-коннекторов.
    
    ВАЖНО! Методы должны быть названы таким образом, чтобы по названию
    можно было понять выполняемые действия.
"""


def insert_rows_into_processed_data_doctor(connector: StoreConnector, dataframe: DataFrame):
    """ Вставка строк из DataFrame в БД с привязкой данных к последнему обработанному файлу (по дате) """
    rows = dataframe.to_dict('records')

    for row in rows:
        connector.execute(
            f'INSERT INTO processed_data_doctor (doctor_id, firstname, lastname, specialization, contact_info) VALUES (\'{row["doctor_id"]}\',  \'{row["firstname"]}\',  \'{row["lastname"]}\',  \'{row["specialization"]}\',  \'{row["contact_info"]}\')')
    print('Data was inserted successfully')


def insert_rows_into_processed_data_patient(connector: StoreConnector, dataframe: DataFrame):
    """ Вставка строк из DataFrame в БД с привязкой данных к последнему обработанному файлу (по дате) """
    rows = dataframe.to_dict('records')

    for row in rows:
        connector.execute(
            f'INSERT INTO processed_data_patient (patient_id, firstname, lastname) VALUES (\'{row["patient_id"]}\', \'{row["firstname"]}\',  \'{row["lastname"]}\')')
    print('Data was inserted successfully')


def insert_rows_into_processed_data_appointment(connector: StoreConnector, dataframe: DataFrame):
    """ Вставка строк из DataFrame в БД с привязкой данных к последнему обработанному файлу (по дате) """
    rows = dataframe.to_dict('records')

    for row in rows:
        connector.execute(
            f'INSERT INTO processed_data_appointment (doctor_id, patient_id, date_time) VALUES (\'{row["doctor_id"]}\', \'{row["patient_id"]}\',  \'{row["date_time"]}\')')
    print('Data was inserted successfully')
