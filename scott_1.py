#import modules
import json
import math
from sys import argv
#load_journal function read json file
def load_journal(content):
  
    with open(content, 'r') as file:
        data = json.load(file)
    #return parsed data. 
    return data
#find correlation between squirrel transformation.
def compute_phi(journal, event):
    #initilizing values
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
    #return correlation value
    return value
       

def compute_correlations(content):
    #load jornal data
    journal = load_journal(content)
    #find uniq entries.
    events = set() 
    for entry in journal:
        for event in entry["events"]:
            events.add(event)
    #declear empty dic, store event as key and correlation value as value
    correlations = {}
    for event in events:
        correlations[event] = compute_phi(journal, event)
    print(correlations)
    #return dictionary
    return correlations
def diagnose(content):
   
    correlations = compute_correlations(content)
    #find maximum and minimum value from dictionary
    max_event = max(correlations, key=correlations.get)
    min_event = min(correlations, key=correlations.get)
    #return values
    return max_event, min_event
  
   

if __name__ == "__main__":
    #unpacking argv
    script,content = argv
    #function call
    most_pos, most_neg = diagnose(content)
    #printing values.
    print(f"Most positively correlated event: {most_pos}")
    print(f"Most negatively correlated event: {most_neg}")
  
   