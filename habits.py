import json
import pymongo
from pymongo import MongoClient
import datetime

class Habits():
    
    def __init__(self):
        
        self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-2quke.mongodb.net/test?retryWrites=true&w=majority")
        self.habits = self.client.habits.habits
        print(self.habits)
    
              
    def add(self, el):
        self.habits.insert(el)
        
    def get(self, name_habit):
        return self.habits.find({'name': name_habit})  
    	
    def save(self):
        self.habits.save()
    
    #по id? db.bios.find( { _id: 5 } )    
    def delete(self, id_habit):
        self.habits.delete_one({ '_id': id_habit })
    
    def update(self, last, new):
        self.habits.update_many(last, new)
