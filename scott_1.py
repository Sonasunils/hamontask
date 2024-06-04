import json
import math
from sys import argv
def load_journal(content):
    # print(content)
    with open(content, 'r') as file:
        data = json.load(file)
        # print(data)
    return data

def compute_phi(journal, event):
    n11 = n00 = n10 = n01 = 0
  
    for entry in journal:
        x = event in entry["events"]
        y = entry["squirrel"]
        
        if x and y:
            n11 += 1
        if not x and not y:
            n00 += 1
        if x and not y:
            n10 += 1
        if not x and y:
            n01 += 1
        n1_plus =n11+n10
      
        n0_plus =n00+n01
      
        n_plus_1 =n11+n01
        
        n_plus_0 =n00+n10
        
        
         
    ntr = (n11 * n00) - (n10 * n01)
    dtr = math.sqrt(n1_plus * n0_plus * n_plus_1 * n_plus_0)
     
       
    value = ntr/dtr
    return value
       

def compute_correlations(content):
    journal = load_journal(content)
   
    events = set() 
    for entry in journal:
        for event in entry["events"]:
            events.add(event)
   
  
    correlations = {}
    for event in events:
        correlations[event] = compute_phi(journal, event)
    print(correlations)

    return correlations
def diagnose(content):
   
    correlations = compute_correlations(content)
    max_event = max(correlations, key=correlations.get)
    min_event = min(correlations, key=correlations.get)
    return max_event, min_event
  
   

if __name__ == "__main__":
    script,content = argv
    diagnose(content)
    most_pos, most_neg = diagnose(content)
    print(f"Most positively correlated event: {most_pos}")
    print(f"Most negatively correlated event: {most_neg}")
  
   