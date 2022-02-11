import http.client, urllib.request, urllib.parse, urllib.error, base64
import os
import json

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Prediction-Key': 'your prediction key',
}


try:
    conn = http.client.HTTPSConnection('{modelname}.cognitiveservices.azure.com')#custom vision service endpoint without https://
    for filename in os.listdir("Images/test"):

        with open(os.path.join("Images/test/",filename), "rb") as image:
            body = image.read()
            image.close()
        conn.request("POST", "{this url you find in customvision.ai when you publish the iteration and get url for local images}", body, headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        # # Display the results.   
        data = json.loads(data) 
        for prediction in data["predictions"]:
            print("\t" + prediction["tagName"] + ": {0:.2f}% ".format(prediction["probability"] * 100))

    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

