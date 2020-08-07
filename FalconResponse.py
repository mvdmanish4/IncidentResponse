from flask import Flask, request
from flask import send_file
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return "Home"

@app.route("/read_request/myassetname")
def myAssetName():
	return jsonify(
        pid=3021,
        op="kill"
    )

@app.route('/write_result', methods=['POST']) 
def writeResult():
	req_data = request.get_json()
	assetname = req_data['assetname']
	return jsonify(
		res=0
	)

if __name__ == "__main__":
	app.debug = True
	app.run()