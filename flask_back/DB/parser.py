from habits import Habits

def get_data():
    db = Habits()
    habits = []
    for habit in db.get_all():    
        print(type(habit['start']))
        habits.append(habit)
    return habits

def get_habit(name_habit):
    db = Habits()
    try:
        return db.get(name_habit=name_habit)
    except:
        return None
def check():
    db = Habits()
    #db.del_habits()
    db.add('Зарядка', 'admin', '1-04-2020', '15-04-2020')
    db.add_check('Зарядка', 'admin', '1-04-2020', '15-04-2020')
check()
print(get_data())
