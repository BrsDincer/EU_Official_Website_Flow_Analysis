from scapy.all import *
import re
import pandas as pd

class LISTEN_OPS():
    def GET_MAC_PROCESS(target_ip):
        try:
            arp_rq = ARP(pdst=target_ip)
            broad_pck = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_rq_broad = broad_pck/arp_rq
            ans_list = srp(arp_rq_broad,timeout=2,verbose=False)[0]
            return ans_list[0][1].hwsrc
        except:
            pass
    def NETWORK_REQUESTS(pkt_incoming):
        # new_list = open("general_listen.txt","a")
        if pkt_incoming.haslayer(Raw):
            in_payload = pkt_incoming.getlayer(Raw).load
            if b"GET" in in_payload:
                in_src = pkt_incoming.getlayer(IP).src
                out_dst = pkt_incoming.getlayer(IP).dst
                dst_port = pkt_incoming.getlayer(IP).dport
                src_port = pkt_incoming.getlayer(IP).sport
                tt_ttl = pkt_incoming.getlayer(IP).ttl
                print("---"*7)
                # new_list.write(f"[GET TRAFFIC: TTL {tt_ttl}] SRC {in_src} --> DST {out_dst}")
                print(f"[GET: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                print("---"*7)
            elif b"POST" in in_payload:
                in_src = pkt_incoming.getlayer(IP).src
                out_dst = pkt_incoming.getlayer(IP).dst
                dst_port = pkt_incoming.getlayer(IP).dport
                src_port = pkt_incoming.getlayer(IP).sport
                tt_ttl = pkt_incoming.getlayer(IP).ttl
                print("---"*7)
                # new_list.write(f"[POST TRAFFIC: TTL {tt_ttl}] SRC {in_src} --> DST {out_dst}")
                print(f"[POST: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                print("---"*7)
            else:
                in_src = pkt_incoming.getlayer(IP).src
                out_dst = pkt_incoming.getlayer(IP).dst
                dst_port = pkt_incoming.getlayer(IP).dport
                src_port = pkt_incoming.getlayer(IP).sport
                tt_ttl = pkt_incoming.getlayer(IP).ttl
                # new_list.write(f"[ADDITIONAL TRAFFIC: TTL {tt_ttl}] SRC {in_src} --> DST {out_dst}")
                print(f"[ADDITIONAL TRAFFIC: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
    def NETWORK_BLACKLIST(pkt_incoming):
        bl_list = pd.read_csv("tracket_all_ip_host.csv")
        # new_list = open("network_listen.txt","a")
        if pkt_incoming.haslayer(Raw):
            in_payload = pkt_incoming.getlayer(Raw).load
            if b"GET" in in_payload:
                try:
                    in_src = pkt_incoming.getlayer(IP).src
                except:
                    pass
                try:
                    out_dst = pkt_incoming.getlayer(IP).dst
                except:
                    pass
                try:
                    dst_port = pkt_incoming.getlayer(IP).dport
                except:
                    pass
                try:
                    src_port = pkt_incoming.getlayer(IP).sport
                except:
                    pass
                try:
                    tt_ttl = pkt_incoming.getlayer(IP).ttl
                except:
                    pass
                try:
                    if in_src in bl_list["IP"].values:
                        detect_host = bl_list[bl_list["IP"] == in_src]
                        detect_host.reset_index(inplace=True)
                        print("---"*7)
                        print("[TRAFFIC HOST]")
                        print(str(detect_host['HOST']))
                        # new_list.write(str(detect_host['HOST']))
                        # new_list.write("---"*7)
                        # new_list.write(f"[GET: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        # new_list.write("---"*7)
                        print(f"[GET: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        print("---"*7)
                    else:
                        pass
                except:
                    pass
            elif b"POST" in in_payload:
                try:
                    in_src = pkt_incoming.getlayer(IP).src
                except:
                    pass
                try:
                    out_dst = pkt_incoming.getlayer(IP).dst
                except:
                    pass
                try:
                    dst_port = pkt_incoming.getlayer(IP).dport
                except:
                    pass
                try:
                    src_port = pkt_incoming.getlayer(IP).sport
                except:
                    pass
                try:
                    tt_ttl = pkt_incoming.getlayer(IP).ttl
                except:
                    pass
                try:
                    if in_src in bl_list["IP"].values:
                        detect_host = bl_list[bl_list["IP"] == in_src]
                        detect_host.reset_index(inplace=True)
                        print("---"*7)
                        print("[TRAFFIC HOST]")
                        print(detect_host['HOST'])
                        # new_list.write(str(detect_host['HOST']))
                        # new_list.write("---"*7)
                        # new_list.write(f"[POST: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        # new_list.write("---"*7)
                        print(f"[POST: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        print("---"*7)
                    else:
                        pass
                except:
                    pass
            else:
                try:
                    in_src = pkt_incoming.getlayer(IP).src
                except:
                    pass
                try:
                    out_dst = pkt_incoming.getlayer(IP).dst
                except:
                    pass
                try:
                    dst_port = pkt_incoming.getlayer(IP).dport
                except:
                    pass
                try:
                    src_port = pkt_incoming.getlayer(IP).sport
                except:
                    pass
                try:
                    tt_ttl = pkt_incoming.getlayer(IP).ttl
                except:
                    pass
                try:
                    if in_src in bl_list["IP"].values:
                        detect_host = bl_list[bl_list["IP"] == in_src]
                        detect_host.reset_index(inplace=True)
                        print("---"*7)
                        print("[TRAFFIC HOST]")
                        print(detect_host['HOST'])
                        # new_list.write(str(detect_host['HOST']))
                        # new_list.write("---"*7)
                        # new_list.write(f"[ADDITIONAL: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        # new_list.write("---"*7)
                        print(f"[ADDITIONAL: TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                        print("---"*7)
                    else:
                        pass
                except:
                    pass
    def EU_SITE_TRACKING(pkt_incoming):
        eu_list = pd.read_csv("eu_all_ip_host.csv")
        if pkt_incoming.haslayer(Raw):
            try:
                in_src = pkt_incoming.getlayer(IP).src
            except:
                pass
            try:
                out_dst = pkt_incoming.getlayer(IP).dst
            except:
                pass
            try:
                dst_port = pkt_incoming.getlayer(IP).dport
            except:
                pass
            try:
                src_port = pkt_incoming.getlayer(IP).sport
            except:
                pass
            try:
                tt_ttl = pkt_incoming.getlayer(IP).ttl
            except:
                pass
            try:
                if in_src in eu_list["IP"].values:
                    try:
                        get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                        print(f"[MAC FOR {in_src}] --> {get_mac}")
                    except:
                        pass
                    print("---"*7)
                    print("[EU SITE]-->")
                    print(f"[TTL {tt_ttl}] SRC {in_src} --> DST {out_dst}")
                    print("---"*7)
                else:
                    try:
                        print(f"[TTL {tt_ttl}] SRC {in_src}:{src_port} --> DST {out_dst}:{dst_port}")
                    except:
                        pass
            except:
                pass
    def EU_SITE_BLACK_LIST_TRACKER(pkt_incoming):
        eu_list = pd.read_csv("eu_all_ip_host.csv")
        bl_list = pd.read_csv("tracket_all_ip_host.csv")
        if pkt_incoming.haslayer(Raw):
            try:
                in_src = pkt_incoming.getlayer(IP).src
            except:
                pass
            try:
                out_dst = pkt_incoming.getlayer(IP).dst
            except:
                pass
            try:
                dst_port = pkt_incoming.getlayer(IP).dport
            except:
                pass
            try:
                src_port = pkt_incoming.getlayer(IP).sport
            except:
                pass
            try:
                tt_ttl = pkt_incoming.getlayer(IP).ttl
            except:
                pass
            try:
                if in_src in eu_list["IP"].values:
                    try:
                        get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                        print(f"[MAC FOR {in_src}] --> {get_mac}")
                    except:
                        pass
                    print("---"*7)
                    print("[EU SITE]-->")
                    print(f"[TTL {tt_ttl}] SRC {in_src}")
                    print("---"*7)
                    if in_src in bl_list["IP"].values:
                        try:
                            get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                            print(f"[MAC FOR {in_src}] --> {get_mac}")
                        except:
                            pass
                        print("---"*7)
                        print("---"*7)
                        print("[IN THE BLACK LIST]-->")
                        print(f"[TTL {tt_ttl}] SRC {in_src}")
                        print("---"*7)
                        print("---"*7)
                    else:
                        print(f"[TTL {tt_ttl}] SRC {in_src}")
                else:
                    pass
            except:
                pass
    def GENERAL_NETWORK_TRACKER(pkt_incoming):
        bl_list = pd.read_csv("tracket_all_ip_host.csv")
        if pkt_incoming.haslayer(Raw):
            try:
                in_src = pkt_incoming.getlayer(IP).src
            except:
                pass
            try:
                out_dst = pkt_incoming.getlayer(IP).dst
            except:
                pass
            try:
                dst_port = pkt_incoming.getlayer(IP).dport
            except:
                pass
            try:
                src_port = pkt_incoming.getlayer(IP).sport
            except:
                pass
            try:
                tt_ttl = pkt_incoming.getlayer(IP).ttl
            except:
                pass
            try:
                if in_src in bl_list["IP"].values:
                    try:
                        get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                        print(f"[MAC FOR {in_src}] --> {get_mac}")
                    except:
                        pass
                    detect_host = bl_list[bl_list["IP"] == in_src]
                    detect_host.reset_index(inplace=True)
                    print("---"*7)
                    print("---"*7)
                    print("[IN THE BLACK LIST]-->")
                    try:
                        print(f"[TTL {tt_ttl}] SRC {in_src}")
                    except:
                        pass
                    try:
                        print(str(detect_host["HOST"]))
                    except:
                        pass
                else:
                    pass
            except:
                pass
    def GENERAL_NETWORK_SUSPECT(pkt_incoming):
        ss_list = pd.read_csv("SUSPECTS_IP.csv")
        # new_list = open("suspect_listen.txt","a")
        if pkt_incoming.haslayer(Raw):
            try:
                in_src = pkt_incoming.getlayer(IP).src
            except:
                pass
            try:
                out_dst = pkt_incoming.getlayer(IP).dst
            except:
                pass
            try:
                dst_port = pkt_incoming.getlayer(IP).dport
            except:
                pass
            try:
                src_port = pkt_incoming.getlayer(IP).sport
            except:
                pass
            try:
                tt_ttl = pkt_incoming.getlayer(IP).ttl
            except:
                pass
            try:
                if in_src in ss_list["IP"].values or out_dst in ss_list["IP"].values:
                    try:
                        get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                        print(f"[MAC FOR {in_src}] --> {get_mac}")
                    except:
                        pass
                    try:
                        get_mac_out = LISTEN_OPS.GET_MAC_PROCESS(out_dst)
                        print(f"[MAC FOR {out_dst}] --> {get_mac_out}")
                    except:
                        pass
                    try:
                        detect_host = ss_list[ss_list["IP"] == in_src]
                        detect_host.reset_index(inplace=True)
                        print("---"*7)
                        print("---"*7)
                        print("[IN THE BLACK LIST]-->")
                    except:
                        pass
                    try:
                        print(f"[TTL {tt_ttl}] SRC {in_src}")
                        # new_list.write(f"[TTL {tt_ttl}] SRC {in_src}")
                    except:
                        pass
                    try:
                        print(str(detect_host["SRC"]))
                    except:
                        pass
                    try:
                        detect_host = ss_list[ss_list["IP"] == out_dst]
                        detect_host.reset_index(inplace=True)
                        print("---"*7)
                        print("---"*7)
                        print("[IN THE BLACK LIST]-->")
                        print(f"[TTL {tt_ttl}] DST {out_dst}")
                        # new_list.write(f"[TTL {tt_ttl}] SRC {out_dst}")
                    except:
                        pass
                    try:
                        print(str(detect_host["SRC"]))
                    except:
                        pass
                else:
                    pass
            except:
                pass
    def PASSIVE_EU_NETWORK_TRACKER(pkt_incoming):
        bl_list = pd.read_csv("tracket_all_ip_host.csv")
        if pkt_incoming.haslayer(Raw):
            try:
                in_src = pkt_incoming.getlayer(IP).src
            except:
                pass
            try:
                out_dst = pkt_incoming.getlayer(IP).dst
            except:
                pass
            try:
                dst_port = pkt_incoming.getlayer(IP).dport
            except:
                pass
            try:
                src_port = pkt_incoming.getlayer(IP).sport
            except:
                pass
            try:
                tt_ttl = pkt_incoming.getlayer(IP).ttl
            except:
                pass
            try:
                if in_src:
                    try:
                        get_mac = LISTEN_OPS.GET_MAC_PROCESS(in_src)
                        print(f"[MAC FOR {in_src}] --> {get_mac}")
                    except:
                        pass
                    detect_host = bl_list[bl_list["IP"] == in_src]
                    detect_host.reset_index(inplace=True)
                    print("---"*7)
                    print("[LIST]-->")
                    try:
                        print(f"[TTL {tt_ttl}] SRC {in_src}")
                        print("---"*7)
                    except:
                        pass
                else:
                    pass
            except:
                pass
    def PASSIVE_EU_TCP(self):
        sniff(session=TCPSession,
              prn=LISTEN_OPS.PASSIVE_EU_NETWORK_TRACKER,
              store=0)
    def LISTEN_EU_TCP(self):
        sniff(session=TCPSession,
              prn=LISTEN_OPS.EU_SITE_TRACKING,
              store=0)
    def LISTEN_EU_IP(self):
        sniff(session=IPSession,
              prn=LISTEN_OPS.EU_SITE_TRACKING,
              store=0)
    def LISTEN_EU_TRACKER_TCP(self):
        sniff(session=TCPSession,
              prn=LISTEN_OPS.EU_SITE_BLACK_LIST_TRACKER,
              store=0)
    def LISTEN_EU_TRACKER_IP(self):
        sniff(session=IPSession,
              prn=LISTEN_OPS.EU_SITE_BLACK_LIST_TRACKER,
              store=0)
    def LISTEN_GENERAL_TRACKER(self):
        sniff(session=TCPSession,
              prn=LISTEN_OPS.GENERAL_NETWORK_TRACKER,
              store=0)
    def LISTEN_GENERAL(self):
        sniff(prn=LISTEN_OPS.NETWORK_REQUESTS,
              store=0)
    def LISTEN_GENERAL_IP(self):
        sniff(session=IPSession,
              prn=LISTEN_OPS.NETWORK_REQUESTS,
              store=0)
    def LISTEN_443_TCP(self):
        sniff(session=TCPSession,
              filter="tcp port 443",
              prn=LISTEN_OPS.NETWORK_REQUESTS,
              store=0)
    def LISTEN_80_TCP(self):
        sniff(session=TCPSession,
              filter="tcp port 80",
              prn=LISTEN_OPS.NETWORK_REQUESTS,
              store=0)
    def LISTEN_BLACKLIST(self):
        sniff(prn=LISTEN_OPS.NETWORK_BLACKLIST,
              store=0)
    def LISTEN_SUSPECT(self):
        sniff(prn=LISTEN_OPS.GENERAL_NETWORK_SUSPECT,
              store=0)
        

class GET_LISTEN():
    def RUN_OPS():
        g_l = type("LISTEN OPERATIONS",
                   (LISTEN_OPS,),
                   {})
        l_i = g_l()
        return l_i
    
# GET_LISTEN.RUN_OPS().LISTEN_GENERAL()