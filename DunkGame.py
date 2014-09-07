
from flask import Flask
from flask import request

from twilio import twiml
import pymongo
import serial

ser=serial.Serial(port='COM4',timeout=3)
s = 0
while s != "\n":
  s=ser.read(1)

dbname = 'mhacks'
client = pymongo.MongoClient(host='localhost', port=27017)
db = client[dbname]
profiles = db['profiles']
queue = db['queue']


app = Flask(__name__, static_url_path='/static')


@app.route('/sms', methods=['POST'])
def sms():

    response = twiml.Response()
    user = request.form['From']
    name = request.form['Body']

    user_doc = profiles.find_one({'user':user})

    if user_doc is None:

      user_doc = {

        'user': user,
        'name': name,
        'score': 0
      }

      profiles.insert(user_doc)

    # Do queue logic
    queue = db.queue.find_and_modify({}, { '$push': {'queue': user_doc['user']} }, upsert=True, new=True)

    # response.message("Thank you %s for checking out our hack follow us @demianvelasaco" % user_doc['name'])
    response.message("you are %d in the queue" % len(queue['queue']))

    return str(response)

def Dunk_Begin():
  turn = 0
  score = 0
  pending = 0
  while turn<6: #will be while True:
    turn = turn + 1
    message=ser.read(9) #reading up to 100 bytes


    print message

    while message == '0,0,0,0,0': #loop that pauses the game when there is no input
      x=0

    print "point\n"


    button0,button1, button2, button3, button4 = message.split(",")

    if button0 == "1":

      score = score +1
      pending = 0
    elif button1 == "1" or button2 == "1" or button3 == "1" or button4 == "1":
      if pending == 0 or pending ==1:
        pending = pending + 1
      else:
        pending =0
        score = score + 1


  return score

  old_queue = queue.find_and_modify({}, {'$pop': {'queue': -1}})  # pop current off the queue
  player = old_queue['queue'][0] # use old queue to current player

  player_profile = profiles.find_and_modify({'user': player}, {'$inc': { 'score': score }}, new=True)

  #sms with score
  #response.message("you scored {0} points! your total score is {1}".format(score, player_profile['score']))


score = Dunk_Begin()
print "Your total score is %d" % (score)

if __name__ == "__main__":
    port = 5000
    app.debug = True
    app.run(host="0.0.0.0", port=port)
