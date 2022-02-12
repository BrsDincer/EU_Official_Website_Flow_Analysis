from scapy.all import *

# c_l = open("connection_listen.txt","a")
# load_layer('tls')
# TLS(data)

def PACKET_GENERAL(pckt_l):
    try:
        print(pckt_l.show())
        print("---"*7)
    except:
        pass
    
def FLOW_NETWORK(pckt_l):
    if pckt_l.haslayer(Raw):
        try:
            in_src = pckt_l.getlayer(IP).src
            print(f"SRC: {in_src}")
        except:
            pass
        try:
            out_dst = pckt_l.getlayer(IP).dst
            print(f"DST: {out_dst}")
        except:
            pass
    else:
        pass
        
def NETWORK_DETAILS(pckt_l):
    i_count = 0
    try:
        src_ip = pckt_l[IP].src
        print("IP SRC: ",str(src_ip))
        i_count += 1
    except:
        pass
    try:
        dst_ip = pckt_l[IP].dst
        print("IP DST: ",str(dst_ip))
        i_count += 1
    except:
        pass
    try:
        id_dns = pckt_l[DNS].id
        print("DNS ID: ",str(id_dns))
        i_count += 1
    except:
        pass
    try:
        rcode_dns = pckt_l[DNS].rcode
        print("DNS CODE: ",str(rcode_dns))
        i_count += 1
    except:
        pass
    try:
        opcode_dns = pckt_l[DNS].opcode
        print("DNS OPERATION CODE: ",str(opcode_dns))
        i_count += 1
    except:
        pass
    try:
        sport_udp = pckt_l[UDP].sport
        print("UDP SRC PORT: ",str(sport_udp))
        i_count += 1
    except:
        pass
    try:
        dport_udp = pckt_l[UDP].dport
        print("UDP DST PORT: ",str(dport_udp))
        i_count += 1
    except:
        pass
    try:
        len_udp = pckt_l[UDP].len
        print("UDP LEN: ",str(len_udp))
        i_count += 1
    except:
        pass
    try:
        sport_tcp = pckt_l[TCP].sport
        print("TCP SRC PORT: ",str(sport_tcp))
        i_count += 1
    except:
        pass
    try:
        dport_tcp = pckt_l[TCP].dport
        print("TCP DST PORT: ",str(dport_tcp))
        i_count += 1
    except:
        pass
    try:
        reserved_tcp = pckt_l[TCP].reserved
        print("TCP RESERVED: ",str(reserved_tcp))
        i_count += 1
    except:
        pass
    try:
        payload_tcp = pckt_l[TCP].payload
        print("TCP PAYLOAD:")
        hexdump(payload_tcp)
        i_count += 1
    except:
        pass
    try:
        name_dnsqr = pckt_l[DNSQR].qname
        print("DNS QNAME: ",name_dnsqr.decode())
        i_count += 1
    except:
        pass
    try:
        type_dnsqr = pckt_l[DNSQR].qtype
        print("DNS QTYPE: ",type_dnsqr.decode())
        i_count += 1
    except:
        pass
    try:
        class_dnsqr = pckt_l[DNSQR].qclass
        print("DNS QCLASS: ",class_dnsqr.decode())
        i_count += 1
    except:
        pass
    try:
        name_dnsrr = pckt_l[DNSRR].rrname
        print("NAME: ",name_dnsrr.decode())
        i_count += 1
    except:
        pass
    try:
        type_dnsrr = pckt_l[DNSRR].type
        print("TYPE: ",type_dnsrr.decode())
        i_count += 1
    except:
        pass
    try:
        data_dnsrr = pckt_l[DNSRR].rdata
        print("DATA: ",data_dnsrr.decode())
        i_count += 1
    except:
        pass
    try:
        ttl_dnsrr = pckt_l[DNSRR].ttl
        print("TTL: ",str(ttl_dnsrr))
        i_count += 1
    except:
        pass
    try:
        proto_dnsrrdnskey = pckt_l[DNSRRDNSKEY].protocol
        print("PROTOCOL: ",str(proto_dnsrrdnskey))
        i_count += 1
    except:
        pass
    try:
        alg_dnsrrdnskey = pckt_l[DNSRRDNSKEY].algorithm
        print("ALGORITHM: ",str(alg_dnsrrdnskey))
        i_count += 1
    except:
        pass
    try:
        pblc_dnsrrdnskey = pckt_l[DNSRRDNSKEY].publickey
        print("PUBLIC KEY: ",str(pblc_dnsrrdnskey))
        i_count += 1
    except:
        pass
    if i_count > 0:
        print("---"*7)
    else:
        pass
    
def EU_SESSION(pckt_l):
    try:
        name_dnsrr = pckt_l[DNSRR].rrname
        if "eu" in name_dnsrr.decode() or "europe" in name_dnsrr.decode():
            print("---"*7)
            NETWORK_DETAILS(pckt_l)
        else:
            pass
    except:
        pass
    
def GENERAL_SESSION(pckt_l):
    try:
        NETWORK_DETAILS(pckt_l)
    except:
        pass
    

# sniff(prn=GENERAL_SESSION,
#       store=0)