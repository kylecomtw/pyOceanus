import re
import pdb
import requests
from .oceanus_data import OceanusData

class Oceanus:
    def __init__(self, url = None):
        if not url:
            self.url = "http://127.0.0.1:8090/nlp/parse"        
        else:
            self.url = url

        if not self.test_url():
            raise Exception("%s not responding" % self.url)

        if url is not None:
            self.url = url
    
    def test_url(self):
        try:
            ret = requests.get(self.url)
            return True
        except Exception: 
            return False       

    def parse(self, text):
        text = text.replace("(", "（")\
                   .replace(")", "）")
        resp = requests.post(self.url, 
                {"intext":text})
        self.nlp = resp.json()
        oc_data = OceanusData(self.nlp)
        return oc_data
    

