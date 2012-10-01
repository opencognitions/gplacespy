import urllib2
import urllib
import simplejson

class gPlaces(object):
    """
    Implements methods to wrap google places api
    """
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.placesurl = 'https://maps.googleapis.com/maps/api/place/{0}/json?{1}'
        
    def find(self, latitude, longitude, types=[], name="", radius= 5*1600, rankby="", sensor="false"):
        paramdict = {}
        paramdict['key'] = self.apiKey
        paramdict['location'] = str(latitude) + ',' + str(longitude)
        
        if(len(rankby) > 0):
            paramdict['rankby'] = rankby
        else:
            paramdict['radius'] = radius
            
        if(len(types) > 0):
            paramdict["types"] ='|'.join(types)
        
        if(len(name) > 0):
            paramdict["name"] = name
        
        paramdict['sensor'] = sensor
        
        url = self.placesurl.format("search", urllib.urlencode(paramdict))
         
        return self._queryurl(url)
        
    def details(self, reference, sensor="false"):
        paramdict = {}
        paramdict['key'] = self.apiKey
        paramdict['reference'] = reference
        paramdict['sensor'] = sensor
        url = self.placesurl.format("details", urllib.urlencode(paramdict))
        return self._queryurl(url)
        
    def _queryurl(self, url):
        print "Querying: {0}".format(url)
        results = urllib2.urlopen(url).read();
        return simplejson.loads(results)    


