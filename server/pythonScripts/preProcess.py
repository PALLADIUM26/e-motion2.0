#pre-process pic
import cv2

def convert(file_path):
    print("Processing image...")
    img = cv2.imread(file_path, cv2.IMREAD_ANYCOLOR)
    print("Converting RGB image to grayscale...")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Converted RGB image to grayscale...")
    print("Resizing image to 48x48 scale...")
    img = cv2.resize(gray,(48, 48))
    print("Resized...")
    cv2.imwrite(filename='D:/buffer_/uploads/saved_img.jpg', img=img)
    print("Image saved!")
    return "D:/buffer_/uploads/saved_img.jpg"