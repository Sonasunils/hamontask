#importing argv
from sys import argv
#module is used to pass command-line arguments to a script
script,file = argv
#open file
txt = open(file)
#read the content
content = txt.read()



chars = len(content) - content.count(' ')
words = len(content.split())
sentences = content.count('.') + content.count('!') + content.count('?')
        
print(chars)
print(words)
print(sentences)

ARI=4.71 * (chars/words) + 0.5 * (words/sentences) - 21.43
print(ARI)
#rounding the ari value
Rounded_value = round(ARI)

#function find grade.
def get(score):
    if score == 1 and score > 1:
        return {"age": "5-6", "grade": "Kindergarten"}
    elif score == 2:
        return {"age": "6-7", "grade": "First Grade"}
    elif score == 3:
        return {"age": "7-8", "grade": "Second Grade"}
    elif score == 4:
        return {"age": "8-9", "grade": "Third Grade"}
    elif score == 5:
        return {"age": "9-10", "grade": "Fourth Grade"}
    elif score == 6:
        return {"age": "10-11", "grade": "Fifth Grade"}
    elif score == 7:
        return {"age": "11-12", "grade": "Sixth Grade"}
    elif score == 8:
        return {"age": "12-13", "grade": "Seventh Grade"}
    elif score == 9:
        return {"age": "13-14", "grade": "Eighth Grade"}
    elif score == 10:
        return {"age": "14-15", "grade": "Ninth Grade"}
    elif score == 11:
        return {"age": "15-16", "grade": "Tenth Grade"}
    elif score == 12:
        return {"age": "16-17", "grade": "Eleventh Grade"}
    elif score == 13:
        return {"age": "17-18", "grade": "Twelfth Grade"}
    elif score == 14:
        return {"age": "18-22", "grade": "College student"}
    else:
        return {"age": "Unknown", "grade": "Unknown"}

Grade_value = get(Rounded_value) 
print(Grade_value)