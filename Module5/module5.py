from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Trees In NY</h1>
<p>A prototype API for trees in NY</p>'''




@app.route('/trees/all')
def api_all():
    r = requests.get('https://data.cityofnewyork.us/resource/nwxe-4ae8.json')
    trees = r.json()
    return jsonify(trees)



# for example: Try the url: http://localhost:5000/trees?boroname=Queens, 
# it will show all of information of trees in Queens
@app.route('/trees', methods=['GET'])
def api_id():
    r = requests.get('https://data.cityofnewyork.us/resource/nwxe-4ae8.json')
    trees = r.json()
    if 'boroname' in request.args:
      boroname = str(request.args['boroname'])
    else:
        return "Error."
    
    results = []
    
    for tree in trees:
        if tree['boroname']== boroname:
            results.append(tree)

    

    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)