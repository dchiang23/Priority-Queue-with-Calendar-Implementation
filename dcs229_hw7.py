from PriorityQueue import *
import names
import random
import sys

def main():
    max_sim_time = int(sys.argv[1]) #argument 2 from terminal
    inital_seed = int(sys.argv[2]) #arguemnt 3 from terminal 
    Q = PriorityQueue()  #initalize the priority q

    random.seed(inital_seed) #set the seed from terminal
    i = 0
    while i<10: #inserting names into the q with times
        Q.insert(random.random()*10, names.get_full_name())
        print(Q)
        print("\n")
        i+=1
    
    t = 0
    while t<max_sim_time: #last part of the question
        time_name = Q.removeMin()
        t = time_name.key
        print(f"Meet with {time_name.value} @ {t:.2f}")
        new_time = t + random.expovariate(0.5)
        Q.insert(new_time,names.get_full_name())

        
if __name__ == "__main__":
    main()