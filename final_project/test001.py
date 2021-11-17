import easyocr
import cv2
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


reader = easyocr.Reader(['ko','en'])
result = reader.readtext('receipt.png')
result2 = str(result)

print(result2)
# with open(result,"r") as f:
#     # print(f.read())
#     x = f.read()
#     y = x.decode(encoding='cp949')
    
#     print(y)