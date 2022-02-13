import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'your subscription key',
}
# docs here
# https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236
# switch between detection_01, detection_02, detection_03 to include face attributes you want
params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,emotion,facialhair,gender,glasses,hair,headpose,makeup,noise',
    'recognitionModel': 'recognition_04',
    'returnRecognitionModel': 'true',
    'detectionModel': 'detection_01',
    'faceIdTimeToLive': '86400', # time image is stored in face api service. It is 24 hours converted to seconds. see docs above
})
# mohamed salah image
# we take image id from it to find similar images like it see find-similar.py file
img_url="https://e0.365dm.com/22/01/1600x900/skysports-mohamed-salah-liverpool_5638215.jpg?20220111105345"

# we get id from this image of mohamed salah and use it to see if it is like the original one we detected above
img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsBIZNa09KmGBuQ_q-jxS0fmbSlHwcrw1I2Q&usqp=CAU"
#print(img_url)
body={"url":img_url}
# this part below if you want to test local images and change application/json to application/octet-stream
# with open("imgs/img.png", "rb") as image:
#     f = image.read()
#     b = bytearray(f)
#     print(type(b))
#     image.close()
# body = [b]
body = json.dumps(body)
try:
    conn = http.client.HTTPSConnection('{your model name}.cognitiveservices.azure.com') # or you can put eastus.api.cognitive.microsoft.com and change eastus to your service
    # region like westus.api.cognitive.microsoft.com
    # link below you can also remove https://{model name}.cognitiveservices.azure.com
    conn.request("POST", "https://{model name}.cognitiveservices.azure.com/face/v1.0/detect?%s" % params, body, headers) # /detect will be /findsimilars in find-similar.py file
    response = conn.getresponse()
    data = response.read()
    print(data)
    #print(json.loads(data)) # to convert from bytes to return it back to python dictionary
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
