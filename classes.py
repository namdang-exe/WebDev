class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    
    def add_passenger(self, name):
        if self.open_seats() > 0:
            self.passengers.append(name)
            return True
        elif not self.open_seats():
            return False
        else:
            return False
            

    def open_seats(self):
        return max(0,self.capacity - len(self.passengers))
    
    
f = Flight(3) # Enter capacity
people = ["Nam", "Jon", "John", "Ken", "Tom", "Thomas"]
for person in people:
    success = f.add_passenger(person)
    if success:
        print(f"The client {person} has been added to the flight.")
    else:
        print(f"The client {person} was not added to the flight. The flight is full.")