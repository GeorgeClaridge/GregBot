import random

Title =['Archbishop', 'Overlord', 'Baron', 'Patriarch', 'Emperor', 'Chancellor', 'Elder', 'Lord', 'Prince', 'Assistant', 'Cleric', 'Nun', 'Consul', 'Curator', 'Headman', 'Delegate', 'High Priest', 'Governor', 'Master', 'Sage', 'King', 'Administrator', 'Intern']
Job = ['Relations', 'Warfare', 'Technology', 'Forestry', 'Communications', 'Mining', 'Agriculture', 'Purity', 'Affairs', 'Tourism', 'Scouts', 'Aviation', 'Defense', 'Fishing', 'Nations' , 'Education', 'Planning', 'Dancing']
Name = 'Greg'

NewName = (f'{Name} The {random.choice(Title)} of {random.choice(Job)}')
print(NewName)




 
