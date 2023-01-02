import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': "Sam",
    'Score': 333,
    'Awards': ["Gold", "Platina", "Paladi"]
}

player2 = {
    'PlayerName': "Frodo",
    'Score': 654,
    'Awards': ["Serebro", "Platina3", "Navoz"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers, myfile)
myfile.close()

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print('Player name is: ' + str(user['PlayerName']))
    print('Score is: ' + str(user['Score']))
    print('Player awards №1: ' + str(user['Awards'][0]))
    print('Player awards №2: ' + str(user['Awards'][1]))
    print('Player awards №3: ' + str(user['Awards'][2]) + '\n')