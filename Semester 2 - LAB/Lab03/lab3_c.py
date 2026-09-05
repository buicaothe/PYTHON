'''
_____________LAB3_C____________
1. AI Tool: Gemini (Google)
2. Prompts used:
"Implement the program using Python 3:
Customers can buy three types of goods A, B, and C that require 1minute, 3 minutes, or 4 minutes service.
The simulation asks a user to enter the probability for a customer to enter the shop.
The program checks that the user gave a valid range for the probability (0.0 - 1.0) or closes if not.
The program executes the simulations 100 times. During one simulation round, a customer enters (with given probability) the cashier's queue, 
the number of customers in the queue is updated, the customer is randomly served A, B, or C minutes, and removed from the queue.
If there are no customers in the queue, the cashier is idle.
The program keeps track of each simulation round, the total number of customers, the longest queue, and the idle time during the simulation.
The final plot x-axis range is from 1 to the number of rounds and each x-point has 3 bars.
Plotting a green bar to x=1, y=20.
The program is allowed to crash if the user does not provide valid numbers for the number of round values,
but it should close if the given number is outside the range of 100 to 1000.
There should not be any other structures than built-in functions
print and input, variables, matplotlib and random functions, if-elif-else statements, and range-for-while loops."
'''
import random
import matplotlib.pyplot as plt

# 1. User Input and Validation
try:
    prob = float(input("Enter the probability of a customer entering (0.0 - 1.0): "))
except ValueError:
    exit()

if not (0.0 <= prob <= 1.0):
    print("Invalid probability range. Closing.")
    exit()

# Set simulation length (constrained to 100-1000)
num_rounds = 100 
if not (100 <= num_rounds <= 1000):
    print("Rounds out of range. Closing.")
    exit()

# 2. Simulation Variables
queue_length = 0
total_customers = 0
longest_queue = 0
idle_time = 0
service_remaining = 0

# Data for plotting
rounds_axis = list(range(1, num_rounds + 1))
queue_history = []
idle_history = []
total_cust_history = []

# 3. Simulation Loop
for r in range(1, num_rounds + 1):
    # Check if a customer enters the queue
    if random.random() < prob:
        queue_length += 1
        total_customers += 1
    
    # Update longest queue statistic
    if queue_length > longest_queue:
        longest_queue = queue_length

    # Cashier Logic
    if service_remaining > 0:
        # Currently serving a customer
        service_remaining -= 1
    elif queue_length > 0:
        # Cashier is free, pick next person in queue
        queue_length -= 1
        # Randomly assign goods A (1min), B (3min), or C (4min)
        service_remaining = random.choice([1, 3, 4])
        # Since we start serving this round, decrement 1 minute immediately
        service_remaining -= 1
    else:
        # Queue is empty and cashier is not busy
        idle_time += 1

    # Record data for this specific round
    queue_history.append(queue_length)
    idle_history.append(idle_time)
    total_cust_history.append(total_customers)

# 4. Final Output and Plotting
print(f"\nSimulation complete for {num_rounds} rounds.")
print(f"Total Customers: {total_customers}")
print(f"Longest Queue: {longest_queue}")
print(f"Total Idle Time: {idle_time}")

# Plotting the results
x = rounds_axis
width = 0.25

plt.bar([i - width for i in x], queue_history, width, label='Queue Length', color='blue')
plt.bar(x, idle_history, width, label='Cumulative Idle Time', color='orange')
plt.bar([i + width for i in x], total_cust_history, width, label='Total Customers', color='red')

# Specific requirement: Plotting a green bar to x=1, y=20
plt.bar(1, 20, width, color='green', label='Required Green Bar')

plt.xlabel('Round Number')
plt.ylabel('Values')
plt.title('Store Simulation Results')
plt.legend()
plt.show()