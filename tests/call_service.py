import requests, random, time, json

random_sentences = (
'I like cake',
'I have seen many cats in my time',
'My apartment is the biggest in the building',
'I might go for a walk',
'Eating cake can be difficult with windows open',
'I am going for holiday in a month',
'I just got a new car',
'I hate when people take my parking-spot',
'No i really hate this crap'
)

print('Starting the simulation...')

for each_try in (10, 100, 500, 1000, 2000, 5000, 10000,20000,30000,40000, 50000, 100000):
    print('Try to predict {0} sentences'.format(str(each_try)))
    d = []
    for x in xrange(each_try):
        d.append(random_sentences[random.randint(0,len(random_sentences)-1)])
    start = time.time()
    
    request_payload = json.dumps(dict(data=d))
    response = requests.post('http://54.76.109.46/api/classify', data=request_payload)
    # Calculate time it took
    elapsed_time = time.time() - start
    print('Call took {0}. Responded with HTTP Code: {1}'.format(str(elapsed_time), str(response.status_code)))
    no_items_returned = len(response.json()['data'])
    print('Returned {0} items'.format(str(no_items_returned)))
