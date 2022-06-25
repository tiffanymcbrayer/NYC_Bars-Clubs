from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 10
# sales = [
#  {
#  "id": 1,
#  "salesperson": "James D. Halpert",
#  "client": "Shake Shack",
#  "reams": 1000
#  },
#  {
#  "id": 2,
#  "salesperson": "Stanley Hudson",
#  "client": "Toast",
#  "reams": 4000
#  },
#  {
#  "id": 3,
#  "salesperson": "Michael G. Scott",
#  "client": "Computer Science Department",
#  "reams": 10000
#  }
# ]

places = {
    
    "1": {
        "id": "1",
        "name": "The Happiest Hour",
        "hoursOperation": ["Monday: 5pm - 12am", "Tuesday: 5pm - 1am", "Wednesday: 5pm - 2am", "Thursday: 5pm - 2am", "Friday: 5pm - 3am", "Saturday: 2pm - 3am", "Sunday: 3pm - 12am"],
        "website": "https://www.happiesthournyc.com/reservations/",
        "picture":"https://d3emaq2p21aram.cloudfront.net/media/cache/venue_carousel/uploads/venues/edit/39137/Happiest%20Hour-85.jpg",
        "address": "121 W 10th St, New York, NY 10011",
        "closestSubway": "14th st",
        "walk": "0.5 mi",
        "neighborhood": "West Village",
        "phone": "(212) 243-2827",
        "type": "bar"
    },
    "2": {
        "id": "2",
        "name": "The Heights",
        "hoursOperation": ["Monday: 4pm - 12am", "Tuesday: 4pm - 12am", "Wednesday: 4pm - 12am", "Thursday: 4pm - 3am", "Friday: 4pm - 3am", "Saturday: 11amm - 3am", "Sunday: 11am - 12am"],
        "website": "https://theheightsnyc.com/",
        "picture":"	https://theheightsnyc.com/wp-content/uploads/2017/11/catering-bg.jpg",
        "address": "2867 Broadway, New York, NY 10025",
        "closestSubway": "110th st",
        "walk": "0.5 mi",
        "neighborhood": "Morningside",
        "phone": "(212) 866-7035",
        "type": "bar"
    },
    "3": {
        "id": "3",
        "name": "Mels",
        "hoursOperation": ["Monday: 11:30am - 11pm", "Tuesday: 11:30am - 11pm", "Wednesday: 11:30am - 11pm", "Thursday: 11:30am - 12am", "Friday: 11:30am - 12am", "Saturday: 10am - 12am", "Sunday: 10am - 12am"],
        "website": "https://www.melsburgerbar.com/",
        "picture": "https://www.melsburgerbar.com/img/gallery/gallery-11.jpg",
        "address": "2850 Broadway New York, NY 10025",
        "closestSubway": "110th st",
        "walk": "0.5 mi",
        "neighborhood": "Morningside",
        "phone": "(212) 452-1304",
        "type": "bar"
    },
    "4": {
        "id": "4",
        "name": "The Mean Fiddler",
        "hoursOperation": ["Monday: 4pm - 4am", "Tuesday: 3pm - 4am", "Wednesday: 3pm - 4am", "Thursday: 3pm - 4am", "Friday: 3pm - 4am", "Saturday: 12pm - 4am", "Sunday: 12pm - 4am"],
        "website": "https://themeanfiddlernyc.com/",
        "picture":"https://www.balldrop.com/images/venues/221-3-mean-fiddler-nyc.jpg",
        "address": "266 W 47th St, New York, NY 10036",
        "closestSubway": "50th st",
        "walk": "0.5 mi",
        "phone": "(212) 354-2950",
        "neighborhood": "Midtown",
        "type": "bar"
    },
    "5": {
        "id": "5",
        "name": "Nothing Really Matters",
        "hoursOperation": ["Monday: 4pm - 2am", "Tuesday: 4pm - 2am", "Wednesday: 4pm - 2am", "Thursday: 4pm - 2am", "Friday: 4pm - 2am", "Saturday: 4pm - 2am", "Sunday: closed"],
        "website": "https://www.instagram.com/nothingreallymattersbar/?hl=en",
        "picture":"https://media.timeout.com/images/105859118/image.jpg",
        "address": "50th St New York, NY",
        "closestSubway": "50th st",
        "walk": "0.5 mi",
        "neighborhood": "Midtown",
        "phone": "",
        "type": "bar"
    },
    "6": {
        "id": "6",
        "name": "Slate",
        "hoursOperation": ["Monday: 4pm - 12am", "Tuesday:  4pm - 12am", "Wednesday:  4pm - 12am", "Thursday:  4pm - 12am", "Friday: 4pm - 4am", "Saturday: 4pm - 4am", "Sunday:  4pm - 12am"],
        "website": "https://slate-ny.com/",
        "picture":"https://slate-ny.com/wp-content/uploads/2018/07/DMitchell_LureGroup_SlateNY_15-copy-min-1.jpg",
        "address": "54 W 21st St, New York, NY 10010",
        "closestSubway": "23th st",
        "walk": "0.5 mi",
        "neighborhood": "Flatiron District",
        "phone": "(212) 989-0096",
        "type": "club"
    },
    "7": {
        "id": "7",
        "name": "PHD Rooftop Lounge at Dream Downtown",
        "hoursOperation": ["Monday: closed", "Tuesday: closed", "Wednesday: closed", "Thursday: 9pm - 4am", "Friday: 9pm - 4am", "Saturday: 5pm - 4am", "Sunday: 5pm - 12am"],
        "website": "https://taogroup.com/venues/phd-lounge-new-york/",
        "picture":"https://taogroup.com/wp-content/uploads/2020/01/09_29_18.SunsetSaturdays-101.jpg",
        "address": "355 W 16th St, New York, NY 10011",
        "closestSubway": "18th st",
        "walk": "0.5 mi",
        "neighborhood": "Chelsea",
        "type": "club"
    },
    "8": {
        "id": "8",
        "name": "Fiddle Sticks",
        "hoursOperation": ["Monday: 5pm - 2am", "Tuesday: 5pm - 2am", "Wednesday: 5pm - 2am", "Thursday: 5pm - 2am", "Friday: 5pm - 4am", "Saturday: 2pm - 4am", "Sunday: 2pm - 4am"],
        "website": "https://www.fiddlesticksnyc.net/",
        "picture":"https://thenewyorknarrative.files.wordpress.com/2015/03/dsc03007.jpg",
        "address": "56 Greenwich Ave, New York, NY 10011",
        "closestSubway": "14th st",
        "walk": "0.5 mi",
        "neighborhood": "west village",
        "phone": "(212) 229-2511",
        "type": "bar"
    },
    "9": {
        "id": "9",
        "name": "Jakes Dilemma",
        "hoursOperation": ["Monday: 3pm - 2am", "Tuesday: 3pm - 2am", "Wednesday: 3pm - 2am", "Thursday: 3pm - 3am", "Friday: 3pm - 4am", "Saturday: 12pm - 4am", "Sunday: 12pm - 2am"],
        "website": "https://www.jakesdilemmanyc.com/location/",
        "picture":"https://assets3.thrillist.com/v1/image/1889114/1200x600/scale;",
        "address": "430 Amsterdam Ave, New York, NY 10024",
        "closestSubway": "79th st",
        "walk": "0.5 mi",
        "neighborhood": "Upper West Side",
        "phone": "(212) 580-0556",
        "type": "bar"
    },
    "10": {
        "id": "10",
        "name": "Tiki Chick",
        "hoursOperation": ["Monday: 5pm - 12am", "Tuesday: 5pm - 12am", "Wednesday: 5pm - 12am", "Thursday: 5pm - 12am", "Friday: 3pm - 12am", "Saturday: 12pm - 12am", "Sunday: 12pm - 12am"],
        "website": "https://www.tikichick.com/location/tiki-chick/",
        "picture":"https://media-cdn.tripadvisor.com/media/photo-s/1d/4b/2e/d0/caption.jpg",
        "address": "517 Amsterdam Ave, New York, NY 10024",
        "closestSubway": "86th st",
        "walk": "0.5 mi",
        "neighborhood": "Upper West Side",
        "phone": "",
        "type": "bar"
    },

}



@app.route('/')
def welcome():
    global places 
    place = places["1"]

    # choose these 
    favoritesList = ["1","2","3"]
    favPlaceList = []
    for i in favoritesList:
        favPlaceList.append(places[i])

    return render_template('welcome.html', favList = favPlaceList)   

@app.route('/edit/<id>')
def edit(id = None):
    global places
    place = places[id]
    hours = place["hoursOperation"]
    
    newHoursList = {}
    for day in hours:
        d, hr = day.split(": ")
        newHoursList[d] = hr

    
    return render_template('edit.html', place = place, current_id = id, newHoursList = newHoursList)

@app.route('/add')
def addPage():
    global places 
    return render_template('add.html', current_id = current_id)




@app.route('/view/<id>')
def view_name(id = None):
    global places

    place = places[id]
    

    return render_template('view.html', place = place)

@app.route('/search_results/<searchItem>')
def search_results(searchItem=None):

    searchItem = searchItem.lower()
    results = []
    for key, value in places.items():
        if not (value["name"].lower().find(searchItem) == -1):
            results.append(value)
        elif not (value["type"].lower().find(searchItem) == -1):
            results.append(value)
        elif not (value["closestSubway"].lower().find(searchItem) == -1):
            results.append(value)
        elif not (value["neighborhood"].lower().find(searchItem) == -1):
            results.append(value)
    num =len(results)


    return render_template('search_results.html', data=results, searchItem = searchItem, numResults = num)

@app.route('/add_place', methods=['GET', 'POST'])
def add_name():
    global places 
    global current_id

    json_data = request.get_json()   
    name = json_data["name"] 
    hoursOperation = json_data["hoursOperation"]
    wesbite = json_data["wesbite"]
    picture = json_data["picture"]
    address = json_data["address"] 
    subwayStop = json_data["closestSubway"]
    walk = json_data["walk"]
    neighborhood = json_data["neighborhood"]
    phone = json_data["phone"] 
    type = json_data["type"]
    

    current_id += 1
    currId = str(current_id)

    # add new entry to array with 
    # a new id and the name the user sent in JSON
    new_place_entry = {
        "id" : currId,
        "name": name,
        "hoursOperation":  hoursOperation,
        "wesbite": wesbite,
        "picture": picture,
        "address" : address,
        "closestSubway": subwayStop,
        "walk":  walk,
        "neighborhood": neighborhood,
        "phone": phone,
        "type": type
    }
    places[currId] = new_place_entry
    print(places[currId])

    return jsonify(current_id = current_id)

@app.route('/edit_place', methods=['GET', 'POST'])
def edit_place():
    global places 
    global current_id

    json_data = request.get_json()   
    currId = json_data['id']
    name = json_data["name"] 
    hoursOperation = json_data["hoursOperation"]
    wesbite = json_data["wesbite"]
    picture = json_data["picture"]
    address = json_data["address"] 
    subwayStop = json_data["closestSubway"]
    walk = json_data["walk"]
    neighborhood = json_data["neighborhood"]
    phone = json_data["phone"] 
    type = json_data["type"]
    

    

    # add new entry to array with 
    # a new id and the name the user sent in JSON
    new_place_entry = {
        "id" : currId,
        "name": name,
        "hoursOperation":  hoursOperation,
        "wesbite": wesbite,
        "picture": picture,
        "address" : address,
        "closestSubway": subwayStop,
        "walk":  walk,
        "neighborhood": neighborhood,
        "phone": phone,
        "type": type
    }
    print(currId)
    places[currId] = new_place_entry
    print(places[currId])

    return jsonify(current_id = current_id)


if __name__ == '__main__':
   app.run(debug = True)




