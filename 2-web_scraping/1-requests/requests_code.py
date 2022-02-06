import requests

# GET
# .get(url, params ={key:value}, args)
# .get(url, headers ={key:value}, args)
# .get(url, auth =(user , pw), args)

x = requests.get('https://w3schools.com')
print("1st ", x.status_code)

# with Auth
x = requests.get('https://w3schools.com/python/demopage.php', auth=("user", "pass"))
print("2nd ", x.status_code)



# GET with params real API
url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart'

params = dict(
    id=1,
    range='1D'
)

resp = requests.get(url=url, params=params)
print("coinmarketcap response ", resp.status_code)
data = resp.json()
print(data)
