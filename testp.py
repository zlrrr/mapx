# coding: utf-8
import json
import requests
import time
import threading

url = "http://ip.taobao.com/service/getIpInfo.php?ip=63.223.108.42"
#url = "/mapData/getHDMapData"

lock = threading.Lock()
last_query_result = None

def query_thread():
    global last_query_result 

    N = 1
    while True:
        time.sleep(1)
        # if last_gps is not None:
        #     fix_ok = last_gps.flags & 1
        #     if not fix_ok:
        #         continue
        try:    
            ####
            #gps = []
            #for each in gps_in_second:
            #gps.append((each.timestamp, str(each.lon), str(each.lat), str(each.imuDirect))
            #params = {}
            #params["equipment"] = equ_id
            #params["lane_num"] = lane_num
            #params["lane"] = lane
            #params["gps"] = gps
            #payload = {}
            #payload["verify"] = verify
            #payload["data"] = params
            #r = requests.post(url, data=json.dumps(payload))
            #r_text = r.text
            #r_dict = json.loads(r_text)

            r = requests.get(url)
            content = r.text
            j = json.loads(content)
            print('\nget {}th information!\n'.format(N))
            print(j)

            lock.acquire()
            #last_query_result = 
            last_query_result = j
            lock.release()

            N = N + 1
            if N >= 11:
                print('\nfinished!')
                break
            ####
        except Exception as e:
            print(e)
            lock.acquire()
            last_query_result = None
            lock.release()
        

def main(gctx=None):
    q_thread = threading.Thread(target=query_thread)
    q_thread.start()

    # while True:
    #     time.sleep(0.1)

if __name__ == "__main__":
    main()