
import requests

parameters = {
        'amount' : 10,
        'type' : 'boolean'
        }

response = requests.get("https://opentdb.com/api.php",params= parameters)
response.raise_for_status()

data = response.json()

'''
for i in range(len(data['results'])):
    print(data['results'][i]['question'])
    print(data['results'][i]['correct_answer'])
    print("\n")
'''  
    
question_data = data['results']