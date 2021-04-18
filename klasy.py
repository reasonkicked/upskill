from pprint import pprint as pp


class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):

        """Args:
                seat: A seat designator such as '12C' or '21F'.
                passenger: The passenger name.

            Raises:
                ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        row, letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")
        
        self._seating[row][letter] = passenger
    
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")
        
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """
        Relocate a passenger to a different seat.

        Args:
            from_seat: This existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
    
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

class AirbusA319:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boeing777:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration
    
    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), 
        "ABCDEFGHJK"[:self._num_seats_per_row])

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
            f" Flight: {flight_number}" \
            f" Seat: {seat}"    \
            f" Aircraft: {aircraft}"    \
            " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()
    

def make_flight():
    g = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    g.allocate_seat("12A", "Józek Gosztyła")
    g.allocate_seat("15F", "Staszek Górczany")
    g.allocate_seat("15E", "Mietek Lubas")
    g.allocate_seat("1C", "Kazek Stawarz")

    return g

def make_flights():
    r = Flight("BA758", AirbusA319("G-EUPT"))
    r.allocate_seat("12A", "Józek Gosztyła")
    r.allocate_seat("15F", "Staszek Górczany")
    r.allocate_seat("15E", "Mietek Lubas")
    r.allocate_seat("1C", "Kazek Stawarz")

    n = Flight("BA758", Boeing777("G-EUPT"))
    n.allocate_seat("12A", "Józek Gosztyła")
    n.allocate_seat("15G", "Staszek Górczany")
    n.allocate_seat("15E", "Mietek Lubas")
    n.allocate_seat("1C", "Kazek Stawarz")
    

    return r, n

r, n = make_flights()
print(r.aircraft_model())
print(n.num_available_seats())
n.relocate_passenger("12A", "13G")

g = make_flight()
#print(g)
#pp(g._seating)

g.relocate_passenger("12A", "15D")
#f = Flight("0s600")

#g.make_boarding_cards(console_card_printer)
a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)

#print(g.num_available_seats())

f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
f.allocate_seat("12A", "Józek Gosztyła")
#f.allocate_seat("DA", "Kazek Górczany")
#print(f.aircraft_model())
#print(f._seating)
#pp(g._seating)
#print(f.model())
#print(f.seating_plan())


class Participant:
    def __init__(self, number, first_name):
        self._number = number
        self._first_name = first_name

    def number(self):
        return self._number
    
    def przedstawSie(self, powitanie = "Cześć"):
        print(powitanie + ", mam na imię " + self._first_name)

    @classmethod
    def nowy_czlowiek(cls, number, first_name):
        return cls(number, first_name)
    
    @staticmethod
    def przywitaj(arg):
        print("Cześć " + arg) 



class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("nazywam się " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)

class KontoBankowe:
    __stan = 0

    @property
    def stan_konta(self):
        return self.__stan
    
    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta: " + str(self.__stan) + "zł"

    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value

konto = KontoBankowe()
#print(konto.stan_konta)

konto.stan_konta = 50
#print(konto.stan_konta)


#cz1 = Czlowiek.nowy_czlowiek("Mietek")
#cz1.przedstaw()
#cz2 = Participant.nowy_czlowiek(2, "Zenek")
#cz2.przedstawSie()
#cz3 = cz2.nowy_czlowiek(5, "Tadek")
#cz3.przedstawSie()
#Participant.przywitaj("ziomuś!")
#cz3.przywitaj("gościu")

#f = Participant(3, "Edek")
#print(f.number())
#print(f.przedstawSie())

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __del__(self):
        pass
        #print("Bye class")

class Dog(Animal):
    def voice(self):
        print("Hał Hał")

felek = Dog("felek", 10)
#felek.voice()

class Wolf(Dog):
    def getVoice(self):
        print("Jestę wilkię,")
        super().voice()

wolf = Wolf("Gierek", 55)
#wolf.getVoice()


class Cat(Animal):
    def getVoice(self):
        print("Miał miał")

cat = Cat("Bury", 8)
#cat.getVoice()

class Test:
    _lista = []
    def dodaj(self, arg):
        self._lista.append(arg)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) -1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj._lista.append("XX")
obj.dodaj("B")
obj.dodaj("C")
#print(obj._lista)
#print(obj.zdejmij())
#print(obj._lista)
