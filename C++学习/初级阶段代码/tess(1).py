import hashlib
import json as json_
import re
import time

import redis
import requests
import urllib
import urllib.parse


class DouYin():
    def __init__(self):
        self.rd_0 = redis.StrictRedis(host="127.0.0.1", port=6379, password='', db=0, decode_responses=True)
        res = requests.get('http://47.113.120.154:5001/device/fetch').json()
        d_id = res['data']
        resp = requests.get(
            f'http://47.113.120.154:5001/device/info?d_id={d_id}').json()
        self.did = resp['data']['device_id']
        self.ktoken = resp['data']['sdi_token_second']
        self.lanusk = self.rd_0.get(
            "lanusk"),  # 'bcef5501c2af168918ac26419aced5d837ff849cd0a343f35d66352781c5979284609486196db2930052c33d23c14e2f7ff21463cb983c77898fe100b34a3cd8'
        self.cookie = self.rd_0.get(
            "cookie"),  # 'passport_csrf_token=cdc0a654b33df1b3de2518fc28e42fe5;passport_csrf_token_default=cdc0a654b33df1b3de2518fc28e42fe5;d_ticket=e061642e38fe42f7adf5870a6c441b66f1f5f;multi_sids=3161788997173783%3Adb99998bc7daa1fb4c2ec52241ea6b58;odin_tt=e78057a139722294418bbaece552bbafc5d4f6f05377874d424703a164a616982a4935354b9522bb2137e7717adbfafa2653ffa8aa437fd4a4ddfb74f37b03f9af379c605e2108e224321c4266247b91;odin_tt=0e841ac6df6635ce2d9da10646dbc3ba2c169ca016e521be094c15291adfed4cfe20d75ce58aa65a12c2cf699c269bab20ba9a331e9a477e3245cf22ea7d2410fd409095562976f3859a0d7436b99a85;n_mh=nDRGnlPBLSwQKPkssRKOj346GEu6tJ5C51xUDnAMMPU;sid_guard=db99998bc7daa1fb4c2ec52241ea6b58%7C1648892788%7C5184000%7CWed%2C+01-Jun-2022+09%3A46%3A28+GMT;uid_tt=3bf853eca8c5d00c5f8dfafd93e1b0b2;uid_tt_ss=3bf853eca8c5d00c5f8dfafd93e1b0b2;sid_tt=db99998bc7daa1fb4c2ec52241ea6b58;sessionid=db99998bc7daa1fb4c2ec52241ea6b58;sessionid_ss=db99998bc7daa1fb4c2ec52241ea6b58;reg-store-region='
        self.x_tt_token = self.rd_0.get(
            "x_tt_token"),  # '00db99998bc7daa1fb4c2ec52241ea6b5802542165c26c8d5027ea6d35841ef594e7c53c1930bde6aed0fdb2c52d2e60950a94b8b3a94fe508c59c53c1462ce82dcd1916f1f77600411b97eedc77dce5513fdc5b3d6253e79f96427fb84323f2f34c8-1.0.1'
        self.x_tt_dt = resp['data']['device_token']
        self.iid = resp['data']['install_id']
        self.version_code = resp['data']['version_code']
        self.openudid = resp['data']['openudid']
        self.manifest_version_code = resp['data']['manifest_version_code']
        self.update_version_code = resp['data']['update_version_code']
        self.package = resp['data']['package']
        self.app_name = resp['data']['app_name']
        self.cdid = resp['data']['cdid']
        self.aid = resp['data']['aid']  # '1128'
        self.channel = resp['data']['channel']
        self.version_name = resp['data']['version_name']
        self.device_platform = resp['data']['device_platform']
        self.device_type = resp['data']['device_type'].replace(' ', '+')
        self.device_brand = resp['data']['device_brand']
        # self.language = resp['data']['language']
        self.language = resp['data']['app_language']
        self.os_api = resp['data']['os_api']
        self.os_version = resp['data']['os_version']
        self.resolution = resp['data']['resolution']
        self.dpi = resp['data']['dpi']
        self.mcc_mnc = resp['data']['mcc_mnc']
        self.ac = resp['data']['ac'].lower()
        self.uuid = resp['data']['uuid_str']
        self.user_agent = resp['data']['user_agent']
        self.proxies = {
            "http": "socks5://140.249.73.70:30005",
            "https": "socks5://140.249.73.70:30005"
        }

    def sign(self, did, stub, url_, ktoken, lanusk):
        url = "http://124.221.64.59:8000/testdy"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "header": {
                "deviceid": str(did),
                "X-SS-STUB": stub,
                "ktoken": ktoken,
                "lanusk": lanusk
            },
            "url": url_,
            "key": "gowinchain"

        }
        resp = requests.post(url=url, headers=headers, data=json_.dumps(data)).json()
        return resp

    def x_ss_stub(self, b):
        if not isinstance(b, bytes):
            b = bytes(b, 'utf-8')
        m = hashlib.md5()
        m.update(b)
        # print(m.hexdigest())
        return m.hexdigest().upper()

    def shop_search(self, query, ursor, sort_params):
        url = f'https://search100-search-quic-lf.amemv.com/aweme/v2/shop/search/aggregate/shopping/?iid=4033439842964023&device_id=738511244499373&ac={self.ac}&channel={self.channel}&aid={self.aid}&app_name={self.app_name}&version_code={self.version_code}&version_name={self.version_name}&device_platform={self.device_platform}&os=android&ssmix=a&device_type={self.device_type}&device_brand={self.device_brand}&language={self.language}&os_api={self.os_api}&os_version={self.os_version}&openudid={self.openudid}&manifest_version_code={self.manifest_version_code}&resolution={self.resolution}&dpi={self.dpi}&update_version_code={self.update_version_code}&_rticket={str(int(time.time() * 1000))}&package={self.package}&mcc_mnc={self.mcc_mnc}&cpu_support64=true&host_abi=armeabi-v7a&is_guest_mode=0&app_type=normal&minor_status=0&appTheme=light&need_personal_recommend=1&is_android_pad=0&ts={str(int(time.time()))}&cdid={self.cdid}&uuid={self.uuid}'
        data = {
            'query': query,  # '无人机',
            'cursor': ursor,  # '0',  # 页数
            'count': '20',  # 数量
            'request_type': '1',
            'search_filter': '1',
            'search_source': 'tab_search',
            'enter_from': 'homepage_hot',
            'query_correct_type': '1',
            'original_search_id': '2022041316334901021218714355B1C8C2',
            'sort_params': sort_params,
            'search_channel': 'homepage_hot',
            'ecom_theme': 'light',
            'extra': '{"recommend_word_id":"","recommend_word_session_id":""}',
            'shown_count': '0',
            'large_font_mode': '0',
            'search_scene': 'douyin_search',
            'address_book_access': '2',
            'location_access': '1'
        }
        data_ = urllib.parse.urlencode(data)
        stub = self.x_ss_stub(data_.encode())
        headers_ = self.sign(self.did, stub, url, self.ktoken, '')
        headers = {
            'x-tt-dt': self.x_tt_dt,
            # 'AAASN5WW4MSHNWBC3YPIAWRQSUHTYBDFV5SOJONCVP2XTHGQ3EIENVIFVB7UBY6EVTVPLSYSASJ367GIBTNFRQ5FJY3O2PFCFTIWECZHOZUHGU765T63FNEGX7WK4OPFVDFDCU7YY7HZIF5OEVYO2VQ',
            'activity_now_client': str(int(time.time() * 1000)),  # '1648798712855',
            'sdk-version': '2',
            'passport-sdk-version': '20356',
            'x-ss-req-ticket': str(int(time.time() * 1000)),  # '1648798711835',
            'x-bd-kmsv': '1',
            'x-vc-bdturing-sdk-version': '2.2.1.cn',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-ss-stub': stub,
            'x-tt-request-tag': 's=-1;p=0',
            'x-ss-dp': '1128',
            'user-agent': self.user_agent,
            # 'com.ss.android.ugc.aweme/190401 (Linux; U; Android 9; zh_CN_#Hans; Pixel 3 XL; Build/PQ3A.190801.002; Cronet/TTNetVersion:28eaf52b 2021-12-28 QuicVersion:68cae75d 2021-08-12)',
            # 'cookie': 'odin_tt=f2755584db9761001a3dcf299e6465c5c669e168e58a55b44a6d665134074c86bd28bfff5a0ec50ee62d88210e0d318e5a2850c0342414174c47aa29df23b4865d6325119259e24ce2d4f72496d020a9;uid_tt=3bf853eca8c5d00c5f8dfafd93e1b0b2;uid_tt_ss=3bf853eca8c5d00c5f8dfafd93e1b0b2;sid_guard=db99998bc7daa1fb4c2ec52241ea6b58%7C1649236979%7C4839809%7CWed%2C+01-Jun-2022+09%3A46%3A28+GMT;sid_tt=db99998bc7daa1fb4c2ec52241ea6b58;sessionid=db99998bc7daa1fb4c2ec52241ea6b58;sessionid_ss=db99998bc7daa1fb4c2ec52241ea6b58;install_id=4033439842964023;ttreq=1$c352b13dc6062285e3e61a2a9883c5a2cad9b404;passport_csrf_token=59222c7e8fbcb4b5794c2fe7f47f2e81;passport_csrf_token_default=59222c7e8fbcb4b5794c2fe7f47f2e81;msToken=Qdzythl1E2axCL0ExlIIbdlmqdmC51IWk51Lo3ZuIq4mdENsi59v34M4wbtxhL8MI1Mpd6hrTEA0yP9UAwdOtbOXbHup4cV-DcqyWeYXNVs='
        }
        try:
            resp = requests.post(url=url, headers=dict(headers, **headers_), data=data).json()
        except:
            return {}
        print(resp)
        return resp