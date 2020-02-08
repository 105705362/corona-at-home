import random

infect_threshold = 0.5
n_residents = 1000
n_couriers = 10
n_sim_days = 10
p_send = 1
p_receive = 1

class Civilian:
    '''resident who may be infected by other people'''
    def __init__(self, infected = False):
        self.infected = infected

    infected = False

    def contact(self, other_person):
        if(self.infected):
            possibility = random.random()
            if(possibility<infect_threshold):
                other_person.infected = True

    def send(self, couriers):
        self.contact(random.choice(couriers))

    def receive(self, couriers):
        random.choice(couriers).contact(self)

class Courier(Civilian):
    '''Courier who delivers parcels'''

class Parcel():
    '''packages, not used in this model'''
    def __init__(self, sender, receiver):
        self.infected = infected

residents = []
couriers = []

for i in range(n_residents):
    residents.append(Civilian())
residents[0].infected =  True
for i in range(n_couriers):
    couriers.append(Courier())

for day in range (n_sim_days):
    for resident in residents:
        if(random.random()<p_send):
            resident.send(couriers)
        if(random.random()<p_receive):
            resident.receive(couriers)
    day = day+1
    print("day: ", day)
    infected_residents = 0
    for resident in residents:
        if resident.infected:
            infected_residents = infected_residents + 1
    infected_couriers = 0
    for courier in couriers:
        if courier.infected:
            infected_couriers = infected_couriers + 1

    print("infected residents: ", infected_residents)
    print("infected couriers: ", infected_couriers)
