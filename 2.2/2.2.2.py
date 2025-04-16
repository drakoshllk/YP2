class Train:
    def __init__(self, destination_name, train_number, departure_time):
        self.destination_name = destination_name
        self.number = train_number
        self.departure_time = departure_time

    def display_info(self):
        print(f'Train destination_name: {self.destination_name}\n'
              f'Train train_number: {self.number}\n'
              f'Train departure_time: {self.departure_time}\n')


trains = [
    Train("Tomsk", 70, "00:00"),
    Train("Novosibirsk", 54, "10:15"),
    Train("Moscow", 777, "06:50")
]

while True:
    try:
        user_input = int(input())
    except ValueError:
        print("Enter train number")
        continue

    found = False
    for train in trains:
        if user_input == train.number:
            train.display_info()
            found = True
    if not found:
        print(f'train number {user_input} not found')
    else:
        break