import random
import time
import matplotlib.pyplot as plt

probability_input = float(input("Enter the probability for a customer to enter (0.0 - 1.0): "))
rounds = 100
if 0.0 < probability_input < 1.0:
    for round in range (rounds):

        #  create  cashier to handle random number of customers 
        cashier = 0
        customer = 0
        ticks = 360  # Simulate 6 hours, 3600 seconds / 10 = 360 "minutes"
        #  statistics of how cashier operated during simulation
        idletime = 0
        max_cashier = 0
        numofserved = 0 
        max_idletime = 0

        service_ready = random.choice((1,3,4))

        while ticks > 0:
            if random.random() <= probability_input:
                customer += 1
                cashier += 1
                if cashier > max_cashier:
                    max_cashier = cashier  # update maximum
            if cashier > 0:
                idletime = 0  # Cashier has customers, reset idle time
                if service_ready > 0:
                    service_ready = service_ready-1
                elif service_ready == 0:
                    service_ready = random.choice((1,3,4))
                    cashier -= 1  # remove one customer from the queue
                    numofserved += 1
            elif cashier == 0:
                idletime += 1  # No customers in queue, increase idle time
                if idletime > max_idletime:
                    max_idletime = idletime  # Update maximum idle time  
            ticks -= 1 # remove one "minute" from simulation
        # Plotting
        plt.bar(round, numofserved, color='blue')
        plt.bar(round+0.1, max_cashier, color='red')
        plt.bar(round+0.2, max_idletime, color='green')
        
    # Plotting a green bar to x=1, y=20
    plt.bar(1, 20, width=0.2, color='green', label='Required Green Bar')

    print(f"Simulation ended with {cashier} customers in queue.")
    print(f"Simulation served: {numofserved} customers.")
    print(f"Simulation's maximum number of customers in queue: {max_cashier}")
    print(f"Simulation's maximum idle time: {max_idletime} minutes.")
    
    plt.xlabel('Simulation Rounds')
    plt.ylabel('Values')
    plt.title('Simulation Results - 100 Rounds')
    plt.legend()
    plt.show()
else:
    print('Programme closes - Probability should be between 0.0 and 1.0!!!')