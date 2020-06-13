from flask_back.DB.habits import Habits
from flask_back.DB.persons import Persons

def get_person_id(login='test', password='test'):
    '''
    Возвращает id полдьзователя по login, password.

    '''
    db_persons = Persons()
    
    person = db_persons.get_one({'login': login, 'password': password})
    _id = person['_id']

    return _id

def get_person_data(_id):
    '''
    Возвращает все привычки пользователя.
    
    '''
    db_habits = Habits()
    habits = []
    for habit in db_habits.get({'id_user': _id}):    
        habits.append(habit)
    
    return habits
    
def add_person(login, password):
    '''
    Добовляет новую персону.
    
    '''
    if check_person(login):
        db_persons = Persons()
        db_persons.add({'login': str(login), 'password': str(password)})
        return True
    else:
        return None

def check_person(login):
    '''
    Проверяет наличие пользователя с такпим именем.
    
    '''
    db_persons = Persons()
    person = db_persons.get({'login': login})
    
    if person.count() == 1:
        return False
    else:
        return True
    
def add_person_habit(_id, name, start, end):
    '''
    Добавляет новую привычку пользователю.
    
    '''
    db_habits = Habits()
    db_habits.add(name, _id, start, end)

def add_check_for_person_habit(_id, name, start, end):
    '''
    Добавляет информаци о выполнение привычки.
    
    '''
    db_habits = Habits()
    db_habits.add_check(name, _id, start, end)

