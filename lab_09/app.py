from flask import Flask, jsonify, request
import numpy as np
import rasterio
import geopandas as gpd

app = Flask(__name__)

with rasterio.open('soil_moisture.tif') as src:
  bbox = src.bounds

@app.route('/get_image_bbox')
def get_image_bbox():
    with rasterio.open('soil_moisture.tif') as src:
        bounds = src.bounds
        return jsonify({
            'xmin': bounds.left,
            'ymin': bounds.bottom,
            'xmax': bounds.right,
            'ymax': bounds.top,
        })

@app.route('/get_moisture_value', methods=['GET'])
def get_moisture_value():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    with rasterio.open('soil_moisture.tif') as src:
        try:
            row, col = src.index(lon, lat)
            moisture = src.read(1)[row, col]
        except (IndexError, ValueError):
            return jsonify({'moisture': 'no data'})

    moisture = int(moisture)  
    return jsonify({'moisture': moisture})

if __name__ == '__main__':
  app.run(debug=True)