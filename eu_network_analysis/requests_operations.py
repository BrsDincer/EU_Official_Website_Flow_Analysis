from input_parameters import GET_LIST as GL
from operational_functions import GET_PARAMETERS as GP
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests,re
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class REQUESTS_OPS():
    def CONTENT_SCRAPING(self,target_site=str):
        head_payload = GP.OUT_OUTPUT().GET_HEADER_EXAMPLE()
        if "https://" in target_site or "http://" in target_site:
            r_s = requests.Session()
            g_r = r_s.get(target_site,
                          verify=False,
                          stream=True,
                          timeout=4,
                          headers=head_payload)
            status_c = g_r.status_code
            header_c = g_r.headers
            content_c = g_r.content
            text_c = g_r.text
            cookies_c = g_r.cookies.get_dict()
            link_c = g_r.links
            history_c = g_r.history
            elapsed_c = g_r.elapsed
            encoding_c = g_r.encoding
            permanent_c = g_r.is_permanent_redirect
            url_c = g_r.url
            r_s.close()
        else:
            r_s = requests.Session()
            g_r = r_s.get("http://"+target_site,
                          verify=False,
                          stream=True,
                          timeout=4,
                          headers=head_payload)
            status_c = g_r.status_code
            header_c = g_r.headers
            content_c = g_r.content
            text_c = g_r.text
            cookies_c = g_r.cookies.get_dict()
            link_c = g_r.links
            history_c = g_r.history
            elapsed_c = g_r.elapsed
            encoding_c = g_r.encoding
            permanent_c = g_r.is_permanent_redirect
            url_c = g_r.url
            r_s.close()
        return status_c,header_c,content_c,cookies_c,\
            text_c,link_c,history_c,\
            elapsed_c,encoding_c,permanent_c,url_c
    def GET_SECURITY_POLICY(self,target_site=str):
        try:
            _,header_c,_,_,_,\
                _,_,_,_=REQUESTS_OPS().CONTENT_SCRAPING(target_site)
            return header_c["Content-Security-Policy"]
        except Exception as err:
            print(str(err))
            print("THERE IS NO SECURITY POLICY")
            pass
        
    def FIND_EMBED(self,target_site=str):
        _,_,_,_,text_c,_,_,\
                _,_,_,_=REQUESTS_OPS().CONTENT_SCRAPING(target_site)
        src_p = re.findall(r"src.*",text_c)
        for x_p in src_p:
            try:
                print(x_p)
            except:
                pass
            
class REQ_OPS():
    def GET_REQ(target_site):
        r_q = type("REQUESTS OPERATIONS",
                   (REQUESTS_OPS,),
                   {})
        req_q = r_q()
        return req_q
    
# _,_,header_c,_,_,_,_,_,_=REQ_OPS().GET_REQ().CONTENT_SCRAPING("https://www.eiopa.europa.eu")
# header_c=REQ_OPS().GET_REQ().GET_SECURITY_POLICY("https://berec.europa.eu")

# REQ_OPS().GET_REQ().FIND_EMBED("https://www.europarl.europa.eu")


            
            
            
        
