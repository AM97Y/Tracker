import json

class Habits(object):
'''
Класс содержит в себе 
список всех привычек и работу с ними.

'''

  def __init__(self):
	with open("data/habits.json") as file:
            data = json.load(file)  

	self.habits = data['habits']
          
  def add_habit(self, el):
	self.habits.append(el)
	
  def save_habits(self):
	with open("data/habits.json") as f:
                pk.dump(self.habits, f)
    
  def del_habit(self, name):
	print("Del ", name)

  def update_habit(self, name):
	print("Update ", name)
