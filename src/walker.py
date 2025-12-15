import random

class Walker:

    def __init__(self, data):
        events = []
        probability = []

        if not data:
            raise ValueError
        
        for i in range(len(data)):
            events.append(data[i][0])

            prob = data[i][1]
            if prob < 0:
                raise ValueError
            
            probability.append(data[i][1])

        n = len(events)

        total = sum(probability)

        if total < 1:
            raise ValueError

        self.n = n
        self.events = events

        if n == 1:
            self.donors = [events[0]]
            self.recepients = [events[0]]
            self.barriers = [1.0]
            
        donor = [i for i in range(n) if probability[i] < 1 / n]
        recepient = [i for i in range(n) if probability[i] > 1 / n]

       
        donors = [None] * n
        recepients = [None] * n
        barriers = [0.0] * n

        distin = [1 / n] * n

        while donor and recepient:

            donor = donor.pop()
            recepient = recepient.pop()

            over = 1 / n - probability[donor]

            to_give = min(over, probability[recepient] - 1 / n)

            donors[donor] = events[donor]
            recepients[donor] = events[recepient]
            barriers[donor] = probability[donor]

            distin[donor] = probability[donor]
            distin[recepient] += to_give

            if distin[recepient] < probability[recepient]:
                recepients.append(recepient)

            elif distin[recepient] > probability[recepient]:
                donors.append(recepient)

            else:
                break

            for i in range(n):
                if donors[i] is None:
                    donors[i] = events[i]
                    recepients[i] = recepient[i]
                    barriers[i] = 1

            self.donors = donors
            self.recepients = recepients
            self.barriers = barriers

    def get_random(self):

        temp = random.random()

        row = int(temp * self.n)

        position = (temp * self.n) - row

        if position < self.barriers[row]:
            return self.donors[row]
        
        else:
            return self.recepients[row]
        


    
        


