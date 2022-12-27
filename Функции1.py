# Создаём словарь.
def create_record(name, telephone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record('Vasya', '+79483647338', 'Plahotnogo 160')
user2 = create_record('Petya', '+79128473646', 'Krasny 130')
user3 = create_record('Vova', '+79221348337', 'Tulenina 40')

print(user1)
print(user2)
print(user3)

# Пересылаем неограниченное количество параметров Persons функции.
def give_awards(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print('Товарищ ' + person.title() + ' награждается медалью ' + medal)

give_awards('"За отвагу"', 'Черкесов', 'Зубарев')
give_awards('"Жукова"', 'Чикулаев', 'Петров')