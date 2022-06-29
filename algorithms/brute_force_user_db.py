import sys
sys.path.append(".")

from utils.users import User, UserDatabase

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(jadhesh)
database.insert(biraj)
database.insert(sonaksh)
database.insert(vishal)

print(database.find('siddhant'))
database.update(User(username='siddhant', name='Siddhant U',
                email='siddhantu@example.com'))
print(database.find('siddhant'))
print(database.list_all())