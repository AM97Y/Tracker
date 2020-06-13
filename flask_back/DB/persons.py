import json
import pymongo
from pymongo import MongoClient
import datetime

class Persons():
    '''
    Данный класс работает с удаленной базой данной персон.
    
    '''
    
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-2quke.mongodb.net/test?retryWrites=true&w=majority")
        self.persons = self.client.persons.persons
        print(self.persons)
              
    def add(self, el):
        self.persons.insert(el)
        
    def get(self, arg):
        return self.persons.find(arg) 
    
    def get_one(self, arg):
        return self.persons.find_one(arg) 
    	
    def save(self):
        self.persons.save()
   
    def delete(self, id_person):
        self.persons.delete_one({ '_id': id_person })
    
    def update(self, last, new):
        self.persons.update_many(last, new)

    def get_all(self):
        return self.persons.find({})