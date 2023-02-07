import geo

testip = '216.239.32.0'

countries = {
    'ID' : '',
    'Country' : '',
    'Continent' : ''
}

regions = {
    'Name' : '',
    'FKCountry' : ''
}

timezones = {
    'Name' : ''
}

hosts = {
    'FKCountry' : '',
    'FKRegion' : '',
    'FKTimezone' : '',
    'Latitude' : 0,
    'Longitude' : 0
}

geodata = geo.getGeoData(testip)

countries['ID'] = geodata['country_code']
countries['Country'] = geodata['country']
countries['Continent'] = geodata['continent_code']
regions['Name'] = geodata['region']
regions['FKCountry'] = countries['ID']
timezones['Name'] = geodata['timezone']
hosts['FKCountry'] = countries['ID']
hosts['FKRegion']= regions['Name']
hosts['FKTimezone'] = timezones['Name']
hosts['Latitude'] = geodata['latitude']
hosts['Longitude'] = geodata['longitude']

print(countries)
print(regions)
print(timezones)
print(hosts)