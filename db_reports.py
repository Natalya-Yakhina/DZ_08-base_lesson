import db_tools as db
import view_result as vr
import sqlite3 as sl
import logger as log


def db_repotrs():
    marker = 1
    is_OK = True
    db_name = "pupils.db"
    while is_OK:
        vr.view("Текущая база данных: ", db_name)
        marker = vr.input_data(
            " Press 1 - Общий перечень. Имена с оценками по всем предметам \n press 2 - working with the database \n press 3 - ввести свой запрос к БД \n press 4 - to previous menu\n: "
        )
        log.logger("User klick", marker)

        match marker:
            case "1":
                input_str = "SELECT name,  MATHEMATICS, RUSSIAN, HISTORY FROM PUPILS, ESTIMATE  WHERE pupil_id = PUPILS.id"
                log.logger("User print report: ", input_str)
                # print(db.get_col_names(db_name, input_str))
                db.print_str_db("pupils.db", input_str)

            case "2":
                input_str = "SELECT name,  MATHEMATICS, RUSSIAN, HISTORY FROM PUPILS, ESTIMATE  WHERE pupil_id = PUPILS.id"
                log.logger("User print report: ", input_str)
                db.print_str_db("pupils.db", input_str)

            case "3":
                input_str = vr.input_data(
                    "Введите запрос, например ('SELECT * FROM pupils;'): "
                )
                log.logger("User print report: ", input_str)
                db.print_str_db("pupils.db", input_str)
            case "4":
                log.logger("Exit previous menu", "")
                is_OK = False
            case _:
                print("Error")
    is_OK = True


# database_request = 0
db_repotrs()
