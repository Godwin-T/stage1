import requests



number = input("Enter a number: \n")
url = f"http://ec2-35-87-181-212.us-west-2.compute.amazonaws.com/api/classify-number?number={number}"

url2 = f"http://127.0.0.1:5000/api/classify-number?number={number}"
response = requests.get(url2)
print(response.text)