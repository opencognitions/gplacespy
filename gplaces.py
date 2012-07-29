import urllib2
import urllib
import simplejson

class gPlaces(object):
    """
    Implements methods to interact with the google places api
    """
    #AIzaSyBwX8lyMQntv4B_Mag-o7Cmn7-FXqXU_QU
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.placesurl = 'https://maps.googleapis.com/maps/api/place/search/json?{0}'
        
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
        
        return self._queryurl(paramdict)
        
    def details(self, reference, sensor="false"):
        paramdict = {}
        paramdict['key'] = self.apiKey
        paramdict['reference'] = reference
        paramdict['sensor'] = sensor
        
        return self._queryurl(paramdict)
        
        
    def _queryurl(self, paramdict):
        url = targeturl = self.placesurl.format(urllib.urlencode(paramdict))
        print "Querying: {0}".format(url)
        results = urllib2.urlopen(url).read();
        return simplejson.loads(results)    


