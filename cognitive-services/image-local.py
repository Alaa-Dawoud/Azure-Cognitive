import http.client, urllib.request, urllib.parse, urllib.error, base64

# link to set parameters and get responsed data that you want
# https://eastus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f21b
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{your key for cognitive service resource in keys and endpoint}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories,Description',
    'details': 'Celebrities,Landmarks',
    'language': 'en',
    'model-version': 'latest',
})

with open("imgs/my-local-image.png", "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(type(b))
    image.close()
body = [b]

try:
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com') # depend on region eastus or other regions 
    conn.request("POST", "{put endpoint here also found in keys and endpoint of the service}/vision/v3.2/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
