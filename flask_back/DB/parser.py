from flask_back.DB.habits import Habits
from flask_back.DB.persons import Persons
#from habits import Habits
#from persons import Persons


def get_person_data(login='test', password='test'):
    db_habits = Habits()
    db_persons = Persons()
    
    habits = []
    person = db_persons.get_one({'login': login, 'password': password})
    _id = person['_id']
    
    for habit in db_habits.get({'id_user': _id}):    
        habits.append(habit)
    
    return habits
    
def add_person(login, password):
    if check_person(login, password):
        db_persons = Persons()
        db_persons.add({'login': str(login), 'password': str(password)})
    else:
        return None

def check_person(login, password):
    db_persons = Persons()
    person = db_persons.get({'login': login, 'password': password})
    
    if person.count() == 1:
        return False
    else:
        return True
    
def add_person_habit(login, password, name, start, end):
    db_habits = Habits()
    db_persons = Persons()
    person = db_persons.get_one({'login': login, 'password': password})
    _id = person['_id']
    db_habits.add(name, _id, start, end)
    
def check():
    db_habits = Habits()
    db_habits.del_habits()
    db_habits.add('Зарядка', 'admin', '1-04-2020', '15-04-2020')
    db_habits.add_check('Зарядка', 'admin', '1-04-2020', '15-04-2020')

def add_check_for_person_habit(login, password, name, start, end):
    db_habits = Habits()
    db_persons = Persons()
    person = db_persons.get_one({'login': login, 'password': password})
    _id = person['_id']
    db_habits.add_check(name, _id, start, end)
'''    
check()
add_person_habit('test', 'test', "Бегать", '06-06-2018', '06-06-2018')
add_check_for_persons_habit('test', 'test', "Бегать", '06-06-2018', '06-06-2018')
print(get_person_data(login='test', password='test'))
'''