# Headers, variables, iterate through headers using enumerate()
f = open("data/raw/european_commission/ted-sample.csv", "r")
headers = f.readline().strip().split(",")
f.close()

for idx, head in enumerate(headers):
  print(idx, head)

#Find "WIN_COUNTRY_CODE" in headers:

for idx, value in enumerate(headers):
  if value == "WIN_COUNTRY_CODE":
    print(idx)

#Checking how many times an item occurs:

a = [1, 2, 4, 1, 2, 1]

d = {}
for num in a:
  if not num in d:
    d[num] = 0
  d[num] += 1

print(d)
print(d[1])

data = []

with open("data/raw/european_commission/ted-sample.csv") as file:
  for line in file:
    data.append(list(line.strip().split(",")))

data = data[1:] #Get rid of headers; don't need them
#or data.pop(0)

#Counting the number of wins by country:
d = {}

for row in data:
  country = row[61] # Careful: some tenders are won by more than one country
  countries = country.split('---') #Returns a list of winning countries
  for country in countries:
    if not country in d:
      d[country] = 0
    d[country] += 1

print(d)



