from input_parameters import GET_LIST as GL
import socket,json,random
import pandas as pd

class USER_OPS():
    def CLEAN_DUBLICATES(target_list=list):
        try:
            c_l = list(dict.fromkeys(target_list))
            return c_l
        except:
            pass
    def READING_FILE(target_document=str):
        try:
            with open(target_document,
                      "r",
                      errors="replace") as t_d:
                n_f = []
                for x_l in t_d:
                    try:
                        n_f.append(x_l.strip())
                    except:
                        pass
            c_l = USER_OPS.CLEAN_DUBLICATES(n_f)
            return c_l
        except:
            pass
    def USER_AGENT_LIST():
        try:
            f_op = open(GL.IN_INPUT().user_agent_all)
            j_op = json.loads(f_op.read())
            list_agent = []
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_agent.append(ixlp_values)
            return list_agent
        except:
            pass
    def GET_TRACKERS(self):
        try:
            tracker_list = USER_OPS.READING_FILE(GL.IN_INPUT().all_trackers)
            return tracker_list
        except:
            pass
    def GET_GOOGLE(self):
        try:
            google_llc = USER_OPS.READING_FILE(GL.IN_INPUT().google_llc)
            return google_llc
        except:
            pass
    def GET_AMAZON(self):
        try:
            amazon_tech = USER_OPS.READING_FILE(GL.IN_INPUT().amazon_tech)
            return amazon_tech
        except:
            pass
    def GET_AKAMAI(self):
        try:
            akamai_tech = USER_OPS.READING_FILE(GL.IN_INPUT().akamai_tech)
            return akamai_tech
        except:
            pass
    def GET_ALIBABA(self):
        try:
            alibaba_group = USER_OPS.READING_FILE(GL.IN_INPUT().alibaba_group)
            return alibaba_group
        except:
            pass
    def GET_ADOBE(self):
        try:
            adobe_inc = USER_OPS.READING_FILE(GL.IN_INPUT().adobe_inc)
            return adobe_inc
        except:
            pass
    def GET_APPLE(self):
        try:
            apple_inc = USER_OPS.READING_FILE(GL.IN_INPUT().apple_inc)
            return apple_inc
        except:
            pass
    def GET_FACEBOOK(self):
        try:
            facebook_inc = USER_OPS.READING_FILE(GL.IN_INPUT().facebook_inc)
            return facebook_inc
        except:
            pass
    def GET_CLOUDFLARE(self):
        try:
            cloudflare_inc = USER_OPS.READING_FILE(GL.IN_INPUT().cloudflare_inc)
            return cloudflare_inc
        except:
            pass
    def GET_EBAY(self):
        try:
            ebay_inc = USER_OPS.READING_FILE(GL.IN_INPUT().ebay_inc)
            return ebay_inc
        except:
            pass
    def GET_LINKEDIN(self):
        try:
            linkedin_cor = USER_OPS.READING_FILE(GL.IN_INPUT().linkedin_cor)
            return linkedin_cor
        except:
            pass
    def GET_LIQUID(self):
        try:
            liquid_llc = USER_OPS.READING_FILE(GL.IN_INPUT().liquid_llc)
            return liquid_llc
        except:
            pass
    def GET_PAYPAL(self):
        try:
            paypal_inc = USER_OPS.READING_FILE(GL.IN_INPUT().paypal_inc)
            return paypal_inc
        except:
            pass
    def GET_RAKUTEN(self):
        try:
            rakuten_inc = USER_OPS.READING_FILE(GL.IN_INPUT().rakuten_inc)
            return rakuten_inc
        except:
            pass
    def GET_TWITTER(self):
        try:
            twitter_inc = USER_OPS.READING_FILE(GL.IN_INPUT().twitter_inc)
            return twitter_inc
        except:
            pass
    def GET_AD_SPY(self):
        try:
            ad_spy_sites = USER_OPS.READING_FILE(GL.IN_INPUT().ad_spy_sites)
            return ad_spy_sites
        except:
            pass
    def GET_EU(self):
        try:
            eu_site = USER_OPS.READING_FILE(GL.IN_INPUT().eu_site)
            return eu_site
        except:
            pass
        
class IP_HOST_OPS():
    def GET_IP_INFO(target_site=str):
        n_s = target_site.replace("https://","").replace("http://","").replace("www.","")
        return socket.gethostbyname(n_s)
    def GET_TRACKET_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_TRACKERS(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("tracket_all_ip_host.csv")
        return concat_d
    def GET_EU_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_EU(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        concat_d.to_csv("eu_all_ip_host.csv")
        return concat_d
    def GET_GOOGLE_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_GOOGLE(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("google_all_ip_host.csv")
        return concat_d
    def GET_AMAZON_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_AMAZON(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("amazon_all_ip_host.csv")
        return concat_d
    def GET_AKAMAI_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_AKAMAI(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("akamai_all_ip_host.csv")
        return concat_d
    def GET_ALIBABA_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_ALIBABA(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("alibaba_all_ip_host.csv")
        return concat_d
    def GET_ADOBE_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_ADOBE(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("adobe_all_ip_host.csv")
        return concat_d
    def GET_APPLE_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_APPLE(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("apple_all_ip_host.csv")
        return concat_d
    def GET_FACEBOOK_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_FACEBOOK(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("facebook_all_ip_host.csv")
        return concat_d
    def GET_CLOUDFLARE_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_CLOUDFLARE(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("cloudflare_all_ip_host.csv")
        return concat_d
    def GET_EBAY_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_EBAY(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("ebay_all_ip_host.csv")
        return concat_d
    def GET_LINKEDIN_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_LINKEDIN(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("linkedin_all_ip_host.csv")
        return concat_d
    def GET_LIQUID_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_LIQUID(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("liquid_all_ip_host.csv")
        return concat_d
    def GET_PAYPAL_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_PAYPAL(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("paypal_all_ip_host.csv")
        return concat_d
    def GET_RAKUTEN_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_RAKUTEN(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("rakuten_all_ip_host.csv")
        return concat_d
    def GET_TWTITER_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_TWITTER(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("twitter_all_ip_host.csv")
        return concat_d
    def GET_AD_SPY_IP(self):
        t_l_i = []
        t_l = []
        for x_t in USER_OPS.GET_AD_SPY(self):
            try:
                # print(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l_i.append(IP_HOST_OPS.GET_IP_INFO(x_t))
                t_l.append(x_t)
            except:
                pass
        series_t_l_i = pd.Series(t_l_i,name="IP")
        series_t_l = pd.Series(t_l,name="HOST")
        concat_d = pd.concat([series_t_l,series_t_l_i],axis=1)
        # concat_d.to_csv("ad_spy_all_ip_host.csv")
        return concat_d
    def GET_HEADER_EXAMPLE(self):
        try:
            user_agent_all=random.choice(USER_OPS.USER_AGENT_LIST())
            ref_ex_list=USER_OPS.READING_FILE(GL.IN_INPUT().ref_list)
            ref_all=random.choice(ref_ex_list)
            date_day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month=["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number=random.randint(1,30)
            date_year=random.randint(2000,2021)
            date_time_x=random.randint(10,23)
            date_time_y=random.randint(10,50)
            date_time_z=random.randint(10,55)
            main_header={"User-Agent":str(user_agent_all),
                         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                         "Connection":"Keep-Alive",
                         "Keep-Alive":"155",
                         "Content-Type":"text/html",
                         "Accept-Encoding":"gzip,deflate",
                         "Accept-Language":"en-us,en;q=0.5",
                         "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                         "Referer":str(ref_all),
                         "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
            return main_header
        except:
            pass

class GET_PARAMETERS():
    def OUT_OUTPUT():
        o_o = type("OUTPUTS",
                   (USER_OPS,
                    IP_HOST_OPS,),
                   {})
        g_o = o_o()
        return g_o

# GET_PARAMETERS.OUT_OUTPUT().GET_EU_IP()