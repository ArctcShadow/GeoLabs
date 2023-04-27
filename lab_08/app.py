from flask import Flask, jsonify
import os
import json
import geopandas as gpd

app = Flask(__name__)
	
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_json/<string:filename>', methods=['GET'])
def get_json(filename):
    try:
        with open(filename + '.json', 'r') as file:
            json_data = file.read()
            return json_data
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})

@app.route('/get_field/<string:field_name>', methods=['GET'])
def get_field(field_name):
    try:
        file_path = os.path.join(os.getcwd(), 'field_data.geojson')
        field_data = gpd.read_file(file_path)
        result = field_data.loc[field_data['name'] == field_name]
        if not result.empty:
            json_result = json.loads(result.to_json())
            return jsonify(json_result)
        else:
            return jsonify({'error': 'Field not found'})
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})

if __name__ == '__main__':
    app.run(debug=True)