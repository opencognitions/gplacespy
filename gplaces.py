import urllib2
import simplejson

class gPlaces(object):
    """
    Implements methods to interact with the google places api
    """
    #AIzaSyBwX8lyMQntv4B_Mag-o7Cmn7-FXqXU_QU
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseurlbyradius = 'https://maps.googleapis.com/maps/api/place/search/{0}?key={1}&location={2},{3}&radius={4}&sensor={5}'
        self.baseurlbyrank = 'https://maps.googleapis.com/maps/api/place/search/{0}?key={1}&location={2},{3}&rankby={4}&sensor={5}'
        
        
    def getPlaces(self, latitude, longitude, types=[], radius= 5*1600, rankby="", sensor="false", outputformat="json"):
        if(len(rankby) > 0):
            targeturl = self.baseurlbyradius.format(outputformat, self.apiKey, latitude, longitude, rankby, sensor)
        else:
            targeturl = self.baseurlbyradius.format(outputformat, self.apiKey, latitude, longitude, radius, sensor)
        
        if(len(types) > 0):
            targeturl = targeturl + '&types='  + '|'.join(types)
        print targeturl
        return self._queryurl(targeturl)
    
    def _queryurl(self, url):
        print "Querying: {0}".format(url)
        results = urllib2.urlopen(url).read();
        return simplejson.loads(results)
        
        


