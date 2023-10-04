import numpy as np
import pandas as pd
import matplotlib.image as mpimg
from PIL import Image as im
from PIL import Image

def cropimg(path):
    img = mpimg.imread(path)
    x = []
    y = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            a = img[i, j, 0]
            b = img[i, j, 1]
            c = img[i, j, 2]
            if (a >= 108 and a < 170) and (b >= 115 and b <= 155) and (c >= 183 and c <= 230):
                x.append(i)
                y.append(j)

    df = pd.DataFrame(list(zip(x, y)))

    # IQR
    Q1 = np.percentile(df[0], 25,
                       interpolation='midpoint')

    Q3 = np.percentile(df[0], 75,
                       interpolation='midpoint')
    IQR = Q3 - Q1
    upper = np.where(df[0] >= (Q3 + 1.5 * IQR))
    lower = np.where(df[0] <= (Q1 - 1.5 * IQR))
    df.drop(upper[0], inplace=True)
    df.drop(lower[0], inplace=True)
    df = df.reset_index(drop=True)

    Q1 = np.percentile(df[1], 25, interpolation='midpoint')
    Q3 = np.percentile(df[1], 75, interpolation='midpoint')
    IQR = Q3 - Q1
    upper = np.where(df[1] >= (Q3 + 1.5 * IQR))
    lower = np.where(df[1] <= (Q1 - 1.5 * IQR))
    df.drop(upper[0], inplace=True)
    df.drop(lower[0], inplace=True)
    df = df.reset_index(drop=True)

    xmin = min(df[0]) < 10 if min(df[0]) < 10 else min(df[0]) - 10
    xmax = max(df[0]) if max(df[0]) < 230 else max(df[0]) + 10
    ymin = min(df[1]) < 10 if min(df[1]) < 10 else min(df[1]) - 10
    ymax = max(df[1]) if max(df[1]) < 310 else max(df[1]) + 10
    i = im.fromarray(img[xmin:xmax, ymin:ymax])
    i = i.resize((80, 80), Image.ANTIALIAS)
    temp = path.split('.')
    i.save(temp[0]+"_crop.jpeg")
#     plt.savefig("F:/jupyter_files/lab_jupyter/newdataset/TEST/EOSINOPHIL/_0_2498.jpeg")
#     i = plt.imshow(img[min(df[0])-10:max(df[0])+10,min(df[1])-10:max(df[1])+10])


