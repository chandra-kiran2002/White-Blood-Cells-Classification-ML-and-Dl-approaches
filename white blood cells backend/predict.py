from joblib import Parallel, delayed
import joblib
import numpy as np
from skimage.io import imread,imshow

# Save the model as a pickle in a file
# joblib.dump(knn, 'filename.pkl')

# Load the model from the file
model = joblib.load('./models/svm1.pkl')


def flat_img(path):
    img = imread(path,as_gray=True)
    img = img[0::4,0::4]
    img=img.flatten()
    return img

# Use the loaded model to make predictions
def predict_img(path):
    x=model.predict(np.array([flat_img(path)]))
    print(x)
    y = model.predict_proba(np.array([flat_img(path)]))
    print(y)
    return [x,y]
# predict_img("F:\\jupyter_files\\lab_jupyter\\newdataset\\TEST\\EOSINOPHIL\\_0_2107.jpeg")