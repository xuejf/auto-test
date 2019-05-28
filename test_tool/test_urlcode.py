#----------------------------#
#!/usr/bin/env python        #
# -*- coding: utf-8 -*-      #
# @Time    : 2018-03-29 8:53 #
# @author  : xuejf           #
# @email   :171521952@qq.com #
# @tool   解决字符串转换
# -------------------------- #
import requests
import unittest
import json
import urllib.parse

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        print("******************start test******************")
        pass

    def test_1(self):

        s = '''jlextIAg2Fne3OdJ0uqm572moQRNB01iJJ5jIHCwydABvElgGqZvAR/isV8mqSoEC9AYWgwmHTHE
fIA2PYNPrEIZnT5V1vESyPVmeKoM0BnG7a7CWicKJkZg3sWW7jXsLi4b16RIWTYJEh6D1k6LJsgi
8k7Ic/Nk4qT1FYGP7Tsvak7tz/UGEjfqZjzx5gI9dByE7Ny7lkBDYqZXIBsRZF0Mk10IgIetDY27
uF+YUpxHvzaGGUsIHbMkHwAraHosY4dwgUo9P+hjItsEBwB0coXiYdxtVyTFt/TzxTKdVFmFEtRx
Hl7zrBBouHZGTwczd8DzG5vdIcHtlXRAKEDcKntlz1jPxBuAsGPuSUHZIUkHvue637jrCvWD5xXp
pH5hOvd8qqrqSICgW2YQFPzSVGYN+9R0D5ElfIRS6h6AKe7Aqve2XWvAxnB3/z7BIhdrEe0nc8I9
E2Zv4aM0Fs7C4bDSsv/hJ0KY+X7jiuEIc726CWYBKDwiWW4yE5ncfw0gBouIAIwMw1h1rDVyS156
bzsxv3g2q9oalZxrsdCP+8Wy0MBORusUfk7inf7daFZw0fuCWtwyn2q4/9agFE4hfS4Gi28DZwpB
uooSk3ZoV0s/y5wJfFuk8IwDF3iNiofG7iQEQf6KEN74fd/BE6JdO15LQKFILBqKrUJvao3/GS0R
FPHNDsGhuxrMNW6XPpnqnquvHN1IHQeexi78/wqd2crhmUrPtcKjMJQilmUX2QzaWYyxvPI85SGR
WuvBTWFr9OtMhKGBnrWH7LPZxLOqovB50VG2W+0VHWcKmLve3sjryxH9RolT48uZoIdvZ2pmBtYG
jAhvUXimvNS8zPmJZA=='''
        s = urllib.parse.quote(s,safe='')
        print(s)
        pass

    def tearDown(self):
        print("****************** end test******************")
        pass


if __name__ == '__main__':
    unittest.main()

##加密串，加密后形成s，s是经过 ulrdecode转换后得到结果 encrypt 加密串
## urllib.parse — Parse URLs into components
'''{
  "ysx_appid": "yxs14615737845553",
  "ysx_ua": "nubia-NX511J_V3",
  "mobile": "13305710129",
  "user_avatars": "http://api.nhbia.cn/uploads/images/20180314/small_thumb/15210191944541_thumb.png",
  "ysx_appkey": "Y3AxNDMxNDg5ODQyNTUzMg==",
  "userpwd": "123321",
  "ysx_build": "18020801",
  "request_time": "1522329772729",
  "oid": "5825487",
  "secret": "d8ac1d26cff8cb856f403a3d6344858f",
  "umeng_channel_key": "lezhi",
  "channel_key": "def5a36fe65e6933ec9e285ee161b9fe",
  "name": "N96qAsCIDnNB0KJWT",
  "channel_id": "20141208",
  "ysx_os": "1",
  "ysx_version": "V1.0.0",
  "sex": "1",
  "ysx_version_code": "18020801"
}'''



# Ran 1 test in 0.002s
#
# OK
# ******************start test******************
# jlextIAg2Fne3OdJ0uqm572moQRNB01iJJ5jIHCwydABvElgGqZvAR%2FisV8mqSoEC9AYWgwmHTHE%0AfIA2PYNPrEIZnT5V1vESyPVmeKoM0BnG7a7CWicKJkZg3sWW7jXsLi4b16RIWTYJEh6D1k6LJsgi%0A8k7Ic%2FNk4qT1FYGP7Tsvak7tz%2FUGEjfqZjzx5gI9dByE7Ny7lkBDYqZXIBsRZF0Mk10IgIetDY27%0AuF%2BYUpxHvzaGGUsIHbMkHwAraHosY4dwgUo9P%2BhjItsEBwB0coXiYdxtVyTFt%2FTzxTKdVFmFEtRx%0AHl7zrBBouHZGTwczd8DzG5vdIcHtlXRAKEDcKntlz1jPxBuAsGPuSUHZIUkHvue637jrCvWD5xXp%0ApH5hOvd8qqrqSICgW2YQFPzSVGYN%2B9R0D5ElfIRS6h6AKe7Aqve2XWvAxnB3%2Fz7BIhdrEe0nc8I9%0AE2Zv4aM0Fs7C4bDSsv%2FhJ0KY%2BX7jiuEIc726CWYBKDwiWW4yE5ncfw0gBouIAIwMw1h1rDVyS156%0Abzsxv3g2q9oalZxrsdCP%2B8Wy0MBORusUfk7inf7daFZw0fuCWtwyn2q4%2F9agFE4hfS4Gi28DZwpB%0AuooSk3ZoV0s%2Fy5wJfFuk8IwDF3iNiofG7iQEQf6KEN74fd%2FBE6JdO15LQKFILBqKrUJvao3%2FGS0R%0AFPHNDsGhuxrMNW6XPpnqnquvHN1IHQeexi78%2Fwqd2crhmUrPtcKjMJQilmUX2QzaWYyxvPI85SGR%0AWuvBTWFr9OtMhKGBnrWH7LPZxLOqovB50VG2W%2B0VHWcKmLve3sjryxH9RolT48uZoIdvZ2pmBtYG%0AjAhvUXimvNS8zPmJZA%3D%3D
# ****************** end test******************