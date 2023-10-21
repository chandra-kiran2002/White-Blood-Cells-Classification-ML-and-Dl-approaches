from flask import Flask,request,jsonify
from base64 import encodebytes
from PIL import Image
import io
from flask_cors import CORS
import crop_img
import predict
import os

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
import random
# UPLOAD_FOLDER = './upload'
UPLOAD_FOLDER = os.path.join('static')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        # return path
        crop_img.cropimg(path)
    #     return '''
    # <h1>cropped image</h1>
    # <img src="'''+path+'">'+"<h5>'"+predict.predict_img(path)[0]+"'</h5>"
        temp = path.split('.')
        result = [path,temp[0]+"_crop.jpeg"]
        encoded_imges = []
        for image_path in result:
            encoded_imges.append(get_response_image(image_path))
        prob = predict.predict_img(temp[0]+"_crop.jpeg")[1][0]
        return jsonify({'result': encoded_imges,
                        'class':predict.predict_img(temp[0]+"_crop.jpeg")[0][0],
                        'prob0':int(prob[0]*100),
                        'prob1':int(prob[1]*100),
                        'prob2':int(prob[2]*100),
                        'prob3':int(prob[3]*100)})

if __name__=="__main__":
    app.run(debug=True)