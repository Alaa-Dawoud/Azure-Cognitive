mohamed_salah_id='returned id' # this id we get from the first img_url detected image in face.py file to compare other images to see if
# they look similar to it or not we detect them also and get their id and compare
# see face.py file
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'your subscription key here',
}

params = urllib.parse.urlencode({
    
})
# docs here
# https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395237
body ={
    "faceId": "returned id",
    "faceIds": ['returned id'], # our face ids list that we want to check other images if they look similar to them or not
    "maxNumOfCandidatesReturned": 10,
    "mode": "matchPerson"
}
body = json.dumps(body)
try:
    conn = http.client.HTTPSConnection('{model name}.cognitiveservices.azure.com')
    conn.request("POST", "https://{model name}.cognitiveservices.azure.com/face/v1.0/findsimilars?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
