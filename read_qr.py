import cv2
import numpy as np

inputImage = cv2.imread("qr.png")

def display(im, bbox):
    n = len(bbox)
    print(bbox)
    for j in range(n):
        x1y1 = bbox[j][0]
        x2y2 = bbox[j][2]
        x1 = x1y1[0]
        y1 = x1y1[1]
        x2 = x2y2[0]
        y2 = x2y2[1]        
        cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 1)
        cv2.imshow("sonuc", im)

qrDecoder = cv2.QRCodeDetector()

data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)

if len(data) > 0:
    print(f"decoded data: {data}")
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage)
    cv2.imshow("Rectified QRCode", rectifiedImage)
    cv2.imwrite("qr.png", rectifiedImage)
    print(f"link: {data}")
else:
    print("QR Code not detected")
    cv2.imshow("sonuc", inputImage)

cv2.waitKey(0)
cv2.destroyAllWindows()