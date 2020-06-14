import json
import pymongo
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

class Habits():
    '''
    Данный класс работает с удалекнной базой данной ПРИВЫЧЕК.
    
    '''
    
    def __init__(self):
        
        self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-2quke.mongodb.net/test?retryWrites=true&w=majority")
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
    
    def add_check(self, name, id_user, start, end):
        #Формат вроемени по договоренности '06-06-2018'
        el = {"name": str(name),
          	 "start": datetime.datetime.strptime(start, '%d-%m-%Y'),
             "id_user": ObjectId(id_user),
          	 "end": datetime.datetime.strptime(end, '%d-%m-%Y'),
             }
        
        find_elem = self.habits.find(el)
        check = list(find_elem[0]['check'])
        check.append(datetime.datetime.now())
        self.habits.update(el, {'$set': {'check': check}})
        
        
    def get(self, arg={'name': "Зарядка"}):
        return self.habits.find(arg)  
    	
    def save(self):
        self.habits.save()
   
    def delete(self, id_habit):
        self.habits.delete_one({ '_id': id_habit })
    
    def update(self, last, new):
        self.habits.update_many(last, new)

    def get_all(self):
        return self.habits.find({})
    
    def del_habits(self):
        self.habits.remove({})