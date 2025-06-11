#use model2.h5
from pythonScripts import preProcess
from keras.models import load_model
import cv2
from matplotlib import pyplot as plt

def giveResult(file_path):
    saved_path = preProcess.convert(file_path)
    mymodel = load_model('server//model2.h5') #91% accuracy

    # mymodel.summary()
    test_img = cv2.imread(saved_path)
    # plt.imshow(test_img)
    # plt.show()

    test_img = cv2.resize(test_img,(48,48))
    # plt.imshow(test_img)

    test_input = test_img.reshape((1, 48, 48, 3))

    mymodel.predict(test_input)

    var = (mymodel.predict(test_input) > 0.5).astype("int32")

    res = "Prediction of img by Model:"
    if var[0][0]==1:
        res += 'Angry'
    elif var[0][1] == 1:
        res += 'Disgust'
    elif var[0][2] == 1:
        res += 'Fear'
    elif var[0][3] == 1:
        res += 'Happy'
    elif var[0][4] == 1:
        res += 'Neutral'
    elif var[0][5] == 1:
        res += 'Sad'
    else:
        res += 'Surprise'
    
    return res

