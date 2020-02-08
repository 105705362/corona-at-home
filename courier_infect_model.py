import random

infect_threshold = 0.01 #传染可能性
#n_residents = 1000 #小区住户
#n_couriers = 10 #负责该小区的快递员数量
#n_sim_days = 10 #模拟天数
p_send = 0.01 #每人每天发快递的可能性，没有考虑发多个
p_receive = 0.1 #没人每天收快递的可能性，没有考虑收多个
#f2fcontact = True #是否当面寄/送快递。如当面，则寄/送均为双向传染，否则为单项传染。
#未考虑小区内人传人可能性，建议增加家庭对象;
#未考虑快递集中管理造成的污染

#结论揭示，避免当面寄送可以大幅度避免感染

class Civilian:
    '''resident who may be infected by other people'''
    def __init__(self, infected = False):
        self.infected = infected

    infected = False

    def contact(self, other_person, bidirectional = False):
        if(bidirectional):
            self.infected = self.infected | other_person.infected
            other_person.infected = self.infected | other_person.infected
        else:
            if(self.infected):
                possibility = random.random()
                if(possibility<infect_threshold):
                    other_person.infected = True

    def send(self, couriers, f2fcontact):
        self.contact(random.choice(couriers), f2fcontact)

    def receive(self, couriers, f2fcontact):
        random.choice(couriers).contact(self, f2fcontact)

class Courier(Civilian):
    '''Courier who delivers parcels'''

class Parcel():
    '''packages, not used in this model'''
    def __init__(self, sender, receiver):
        self.infected = infected

class Block():

    def __init__(self, n_residents, n_couriers, init_infected_residents, init_infected_couriers, f2fcontact = False ):
        self.residents = []
        self.couriers = []
        self.n_residents = n_residents
        self.n_couriers = n_couriers
        self.f2fcontact = f2fcontact
        self.init_infected_residents = init_infected_residents
        self.init_infected_couriers = init_infected_couriers
    residents = []
    couriers = []
    #couriers[0].infected =  True

    def simulate(self, n_sim_days):
        print("----------------", self.n_residents, self.n_couriers, self.f2fcontact, self.init_infected_residents, self.init_infected_couriers)
        for i in range(self.n_residents):
            self.residents.append(Civilian(i<self.init_infected_residents))

        for i in range(self.n_couriers):
            self.couriers.append(Courier(i<self.init_infected_couriers))

        for day in range (n_sim_days):
            for resident in self.residents:
                if(random.random()<p_send):
                    resident.send(self.couriers, self.f2fcontact)
                if(random.random()<p_receive):
                    resident.receive(self.couriers, self.f2fcontact)
            day = day+1
            print("day: ", day)
            infected_residents = 0
            for resident in self.residents:
                if resident.infected:
                    infected_residents = infected_residents + 1
            infected_couriers = 0
            for courier in self.couriers:
                if courier.infected:
                    infected_couriers = infected_couriers + 1
            print("infected residents: ", infected_residents)
            print("infected couriers: ", infected_couriers)

blocks = []
blocks.append(Block(2000, 10, 1, 0, False))
blocks.append(Block(2000, 10, 0, 1, False))
blocks.append(Block(2000, 10, 1, 0, True))
blocks.append(Block(2000, 10, 0, 1, True))
for block in blocks:
    block.simulate(10)
