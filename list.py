from collections import namedtuple
symbols='$¢£¥€¤'
codes=[ord(symbol) for symbol in symbols]
print(codes)
dummy=[x for x in [1,2,3]]
print(dummy)
city,year,area='changsha',1917,'yuelu'
print(year)

print('{:15} | {:^9} | {:^9}|'.format('213', 'lat.', 'long.'))

City=namedtuple('City1','name coordinates')
beijin=City('beijing',(0,0))
print(beijin)
print(type(beijin))
print(beijin.coordinates)
print(City._make())

