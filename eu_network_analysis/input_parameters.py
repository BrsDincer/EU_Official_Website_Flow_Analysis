def OPERATIONAL_LIST(self):
    self.eu_site = "list_eu.txt"
    self.google_llc = "google_llc.txt"
    self.amazon_tech = "amazon_tech.txt"
    self.akamai_tech = "akamai_tech.txt"
    self.alibaba_group = "alibaba_group.txt"
    self.adobe_inc = "adobe_inc.txt"
    self.apple_inc = "apple_inc.txt"
    self.facebook_inc = "facebook_inc.txt"
    self.cloudflare_inc = "cloudflare_inc.txt"
    self.ebay_inc = "ebay_inc.txt"
    self.linkedin_cor = "linkedin_cor.txt"
    self.liquid_llc = "liquid_llc.txt"
    self.paypal_inc = "paypal_inc.txt"
    self.rakuten_inc = "rakuten_inc.txt"
    self.twitter_inc = "twitter_inc.txt"
    self.verizon_media = "verizon_media.txt"
    self.ad_spy_sites = "ad_spy_sites.txt"
    self.all_trackers = "total_trackers_list.txt"
    self.user_agent_all = "user_agent_all.json"
    self.ref_list = "ref_list.txt"
    
class GET_LIST():
    def IN_INPUT():
        g_i = type("PARAMETERS",
                   (),
                   {"get_parameters":OPERATIONAL_LIST})
        f_i = g_i()
        f_i.get_parameters()
        return f_i
    

