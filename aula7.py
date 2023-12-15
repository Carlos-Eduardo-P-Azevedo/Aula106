import cv2

# img = cv2.imread("butterfly.jpg")
# #cv2.imshow("Borboleta",img)
# grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2LAB)
# cv2.imshow("Cinza",grayimg)
# cv2.waitKey(0)
# #print(grayimg)

# img = cv2.imread("poster.jpg")
# rocket = img[120:360,400:500]
# img[0:240,500:600] = rocket
# text = "Banana"
# cv2.putText(img,text,(250,200),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,196,31))
# cv2.imshow("Foguete",img)
# cv2.waitKey(0)

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sol",(100,100),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img,"Mercurio",(130,170),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(230,170),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Terra",(330,260),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Lua",(340,160),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Marte",(410,170),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupter",(650,100),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturno",(830,160),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Urano",(1050,170),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Netuno",(1170,170),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,255,255))
cv2.imshow("planeta",img)
cv2.waitKey(0)