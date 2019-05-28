#!/usr/bin/env python        #
# -*- coding: utf-8 -*-      #
# @Time    : 2018-03-29 8:53 #
# @author  : xuejf           #
# @email   :171521952@qq.com #
# -------------------------- #
###字符串测试

from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex

# 补全字符
def align(str, isKey=False):
    # 如果接受的字符串是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果接受的字符串是明文或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str


r_str ={"result":"z9urmHmqRA8YAwaHfFvRU24LfIsRA535qNd6bATWZizkKcwUaZlSlmvYRAxzE0MeLaCgs4CMvlqFdxoND0UuYjVwHc1XSjE9YhukWCHrPoDekRUJRxecpVkYA7F7VciAy88yMQuO1bJ7pSBWmzc3O4gF4VxIxksT5uK4TrE0WDqNZtjd2qcwS7AyaRzMNvWQ\/cY\/IBoYrV7GjOYAc3nOw\/BuFNzoaq6926GHelSaxQmnQdVlRXjGAZzlAKdOsGkvNpuLjFDVsUPOk4RAZQU7SEw22jToyQVHEHVgcxIN6vn7\/41VCGKV+W9JSpbBpb84b+H7xm6WBIeY68WPuH0HkmBPePGzpvIYyKE\/uN7EToHngOv42L1h5hvyT\/kebJZLIrvBRjeR5bD7tUQdYYsgQsH8RaOhB+NEntNaNVNUOQ5JNZ6TlYtK4cu\/4MkC5lZM+vB6Oq6N3jM2bc88dXBAQD2joWGzCxPh\/yMm+X9S3BOWgopTMDgRf56JbY+t\/tBNiCUF+4lICUs\/UGvGbR+qmYS8c75HZbnO6qkpDksYZyUo6f+pcTIAHW6U8t9N7XXA0QVL4w2bvDWWFEerwjbERQRGGXECvwwW8jWVBT2uTauRJQ\/ZU4cQeroFUXbSRfk1GTBIRybKczKz2qNbG4RwlxODuOPwAm\/PEI+ClJZoxfAb7X8q5Y2sOFp7HeS5hCVDHdawJjTi7JionQiA30HE4WsEh0oFE9D6WLseCv4FPkggaOJWlEljSe2BAuvWzRQ4EGtw6r5WjfZqIraxKjxtsoQ4yBEfldCRi5cdfihc\/dBhqIFjqp+3BMXxdhSemt6Y7zHxf9\/FYOxwH2e9b7oaJ3EQi8aUc1BXO0j\/Icq2UPzpt\/N+Rc+kjZsD96\/sFbkUZHemIHZO2u4cERWSTp84desd00Fif2FixXqymYETssnRtt6sBj52yRX8s+E+YvlucPRgLyzOmZRIg2xh+vjQWXDIvYWMSgGxJh6gm+bbtVxSMDBSBXRaPBWlNm39zkRZa9AdqY7bBC5cnmhgNU\/GJPVX73zmto85QYyfhq434I48+rQx2CmYQVXX6hjHRDqbY2Ra9LHG16AqMlN03H3To8ewYlppfbSdkEbYAHmpCN4QjJr7ezmyEmm8nI1H3vFh0qJKJuf8SetR1+c2gpBJ\/mrg3Nr9pnZKksvu3X\/zNbRnewGOPXvRuiE1aOZSySL7p+raGngLeOUU\/P5w\/wMVhzPcuBVLGbzGIMV2BePpTd2IBEslfTjZb0v4YPAMmYtS0o5Lo\/d4TVEA0nkPZi\/5R4EdJjU3xNHpmfqTlQAzEQyBxgXbIRhaXaaLTsbWhDhLDYy0CniYJJ4uVTZHSIcuOOrTtLqsi61Re0HKqbIg0mPfqkCBsaMJ1fCgeCMZZRH4zKruDmvbBK8b7OUkmwJgDM4ZYZ2zi6bcloqwiyUekRDyoVB1CoLqWllcTKnVaJRaJV83hlFHaPZv0HBqj2rc5eWBD7ojA2MGseo9lCoGVZVC9xZtiL0M7W\/BC9lYKaQkbltVRox66I27R3iH1yGT3YtfYzwtajHuPLMD+f30Dbo2IkgUmEbxiX36Vm3UyxTtO8XakGm3cX2+kNfTZPI0SXrzk57rjA2lD+jyKtyCGRuIWdcocjMeetpztcljVaGUHXlQkYmCx\/LsmBm6tFLn336Ocg065rBHuSK4vj+2OPZYs\/rWOAgDDngq7ZXxmN9ov5OJwNwphSy+aPmQQiPmV+CdosbXP+npOoAIf8dZjt5no1qlAgyNguBCtT1LcbP5LbD+REndrlW\/LbJinIG8Q29KVFl9PWgTH4zWrHBwjUh6ZQk6SA23TnyRLulAEhXwIMYq6\/HDWZZMIEolpnNdLLxPOv\/lJxu5tHtSpFLvn6k="}
print(type(r_str))

print(r_str["result"])





