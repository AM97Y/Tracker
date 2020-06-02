import json
import pymongo
from pymongo import MongoClient
import datetime

class Persons():
    '''
    Данный класс работает с удалекнной базой данной персон.
    
    '''
    
    def __init__(self):
        #Other path!
        self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-2quke.mongodb.net/test?retryWrites=true&w=majority")
        self.persons = self.client.persons.persons
        print(self.persons)
    
              
    def add(self, el):
        self.persons.insert(el)
        
    def get(self, user):
        return self.persons.find({'user': user})  
    	
    def save(self):
        self.persons.save()
   
    def delete(self, id_person):
        self.persons.delete_one({ '_id': id_person })
    
    def update(self, last, new):
        self.persons.update_many(last, new)
