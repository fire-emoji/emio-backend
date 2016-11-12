from urllib2 import Request, urlopen, URLError



"""
apikey str
origin str
destination str
departure_date str
one-way bool
duration 1-15
direct bool
max_price int
aggregation_mode

http://api.sandbox.amadeus.com/v1.2/flights/
inspiration-search?origin=BOS
&departure_date=2015-09-06--2015-09-26&duration=7--9&max_price=500&apikey=<your API key>
"""
class amadeus:
    def __init__(self, _origin, _max_price):
        self.apikey = "RvgLqBzb1H67WTUb4WQbKKQPgmk9SAlK"
        self.origin = _origin
        self.max_price = _max_price
        packageForPing()

    def packageForPing(self):
        self.req = "http://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?origin={0}&max_price={1}&apikey={2}".format(self.origin,self.max_price,self.apikey)

    def makeRequest(self):
        try:
            response = urlopen(self.req)
            reqrep = response.read()
            return reqrep
        except URLError, e:
            print e
