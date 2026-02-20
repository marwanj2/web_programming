class Flight:
    
    counter = 1

    def __init__(self, origin, destination, duration):
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration} min")

        print()
        print("Passengers: ")
        for passenger in self.passengers:
            print(f"{passenger.name}")
    
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id



class Passenger:
    def __init__(self, name):
        self.name = name


def main():
    #create a flight
    f1 = Flight(origin="Tunis", destination="Gafsa", duration=30)
    marwan = Passenger(name="Marwan")
    ilyes = Passenger(name="Ilyes")

    f1.add_passenger(marwan)
    f1.add_passenger(ilyes)

    f1.print_info()

if __name__ == "__main__":
    main()
