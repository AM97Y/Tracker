from pymongo import MongoClient
import datetime	
from datetime import date

from bson.objectid import ObjectId

class Habits():
    '''
    Данный класс работает с удалекнной базой данной ПРИВЫЧЕК.
    
    '''
    
    def __init__(self):
        
        self.client = MongoClient("mongodb+srv://admin:admin@cluster0-2quke.mongodb.net/test?retryWrites=true&w=majority")
        self.habits = self.client.habits.habits
             
    def add(self, name, id_user, start, end):
        #Формат вроемени по договоренности '06-06-2018'
        el = {"name": str(name),
            	 "start": datetime.datetime.strptime(start, '%d-%m-%Y'),
                 "id_user": ObjectId(id_user),
            	 "end": datetime.datetime.strptime(end, '%d-%m-%Y'),
            	 "check": []
            }
        
        self.habits.insert(el)
    
    def add_check(self, _id_habit, start, end):
        print(date.today())
        if not(datetime.datetime.strptime(str(date.today()), '%Y-%m-%d') >= datetime.datetime.strptime(start, '%d-%m-%Y') and datetime.datetime.strptime(str(date.today()), '%Y-%m-%d') <= datetime.datetime.strptime(end, '%d-%m-%Y')):
            return False
        
        #Формат вроемени по договоренности '06-06-2018'
        el = {
          	 "start": datetime.datetime.strptime(start, '%d-%m-%Y'),
             "_id": ObjectId(_id_habit),
          	 "end": datetime.datetime.strptime(end, '%d-%m-%Y'),
             }
        
        find_elem = self.habits.find(el)
        check = list(find_elem[0]['check'])
        if check.count(datetime.datetime.strptime(str(date.today()), '%Y-%m-%d')) == 0:
            check.append(datetime.datetime.strptime(str(date.today()), '%Y-%m-%d'))
            self.habits.update(el, {'$set': {'check': check}})
        else:
            return False
        
        return True
    
    def delete_check(self, _id_habit, data_del):

        #Формат вроемени по договоренности '06-06-2018'
        el = {"_id": ObjectId(_id_habit)}
        
        find_elem = self.habits.find(el)
        check = list(find_elem[0]['check'])
        try:
            index = check.index(datetime.datetime.strptime(data_del, '%d-%m-%Y'))
            check.pop(index)
            self.habits.update(el, {'$set': {'check': check}})
        except:
            return False
        
        return True
        
        
    def get(self, arg={'name': "Зарядка"}):
        return self.habits.find(arg)  
    	
    def save(self):
        self.habits.save()
   
    def delete(self, id_habit):
        self.habits.delete_one({ '_id': ObjectId(id_habit) })
        return True
    
    def update(self, last, new):
        self.habits.update_many(last, new)
        
    def get_one(self, _id_habit):
        el = {
             "_id": ObjectId(_id_habit),
             }
        return self.habits.find_one(el)

    def get_all(self):
        return self.habits.find({})
    
    def del_habits(self):
        self.habits.remove({})