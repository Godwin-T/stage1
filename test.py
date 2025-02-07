import requests



number = int(input("Enter a number: \n"))
url = f"http://ec2-35-87-181-212.us-west-2.compute.amazonaws.com/api/classify-number?number={number}"
response = requests.get(url)
print(response.text)