<?php
/****
{
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
}
****/


  /**
   * Formats a JSON string for pretty printing
   *
   * @param string $json The JSON to make pretty
   * @param bool $html Insert nonbreaking spaces and <br />s for tabs and linebreaks
   * @return string The prettified output
   */


function unicode_decode($name){
 
  $json = '{"str":"'.$name.'"}';
  $arr = json_decode($json,true);
  if(empty($arr)) return '';
  return $arr['str'];
}

function decodeUnicode($str)
{
    return preg_replace_callback('/\\\\u([0-9a-f]{4})/i',
        create_function(
            '$matches',
            'return mb_convert_encoding(pack("H*", $matches[1]), "UTF-8", "UCS-2BE");'
        ),
        $str);
}

function _format_json_e($json, $html = false) {
    $tabcount = 0;
    $result = '';
    $inquote = false;
    $ignorenext = false;
    if ($html) {
      $tab = "   ";
      $newline = "<br/>";
    } else {
      $tab = "\t";
      $newline = "\n";
    }
    for($i = 0; $i < strlen($json); $i++) {
      $char = $json[$i];
      if ($ignorenext) {
        $result .= $char;
        $ignorenext = false;
      } else {
        switch($char) {
          case '{':
            $tabcount++;
            $result .= $char . $newline . str_repeat($tab, $tabcount);
            break;
          case '}':
            $tabcount--;
            $result = trim($result) . $newline . str_repeat($tab, $tabcount) . $char;
            break;
          case ',':
            $result .= $char . $newline . str_repeat($tab, $tabcount);
            break;
          case '"':
            $inquote = !$inquote;
            $result .= $char;
            break;
          case '\\':
            if ($inquote) $ignorenext = true;
            $result .= $char;
            break;
          default:
            $result .= $char;
        }
      }
    }
    return $result;
}

function _format_str($json, $html = false) {
    $tabcount = 0;
    $result = '';
    $inquote = false;
    $ignorenext = false;
    if ($html) {
      $tab = "    ";
      $newline = "<br/>";
    } else {
      $tab = "    ";
      $newline = "\n";
    }
    for($i = 0; $i < strlen($json); $i++) {
      $char = $json[$i];
      if ($ignorenext) {
        $result .= $char;
        $ignorenext = false;
      } else {
        switch($char) {
          case '{':
            $tabcount++;
            $result .= $char . $newline . str_repeat($tab, $tabcount);
            break;
          case '}':
            $tabcount--;
            $result = trim($result) . $newline . str_repeat($tab, $tabcount) . $char;
            break;
          case ',':
            $result .= $char . $newline . str_repeat($tab, $tabcount);
            break;
          case '"':
            //$inquote = !$inquote;
            $result .= $char;
            break;
          case '\\':
            //if ($inquote) $ignorenext = true;
            $result .= $char;
            break;
          default:
            $result .= $char;
        }
      }
    }
    return $result;
}

//$arr = array("ret"=>0,"data"=>array('a' => 1, 'b' => "脚本之家", 'c' => 3, 'd' => 4, 'e' => 5));
/******
解密前
$str='z9urmHmqRA8YAwaHfFvRU24LfIsRA535qNd6bATWZizkKcwUaZlSlmvYRAxzE0MeLaCgs4CMvlqFdxoND0UuYjVwHc1XSjE9YhukWCHrPoDekRUJRxecpVkYA7F7VciAy88yMQuO1bJ7pSBWmzc3O4gF4VxIxksT5uK4TrE0WDqNZtjd2qcwS7AyaRzMNvWQ/cY/IBoYrV7GjOYAc3nOw/BuFNzoaq6926GHelSaxQmnQdVlRXjGAZzlAKdOsGkvNpuLjFDVsUPOk4RAZQU7SEw22jToyQVHEHVgcxIN6vn7/41VCGKV+W9JSpbBpb84b+H7xm6WBIeY68WPuH0HkmBPePGzpvIYyKE/uN7EToHngOv42L1h5hvyT/kebJZLIrvBRjeR5bD7tUQdYYsgQsH8RaOhB+NEntNaNVNUOQ5JNZ6TlYtK4cu/4MkC5lZM+vB6Oq6N3jM2bc88dXBAQD2joWGzCxPh/yMm+X9S3BOWgopTMDgRf56JbY+t/tBNiCUF+4lICUs/UGvGbR+qmYS8c75HZbnO6qkpDksYZyUo6f+pcTIAHW6U8t9N7XXA0QVL4w2bvDWWFEerwjbERQRGGXECvwwW8jWVBT2uTauRJQ/ZU4cQeroFUXbSRfk1GTBIRybKczKz2qNbG4RwlxODuOPwAm/PEI+ClJZoxfAb7X8q5Y2sOFp7HeS5hCVDHdawJjTi7JionQiA30HE4WsEh0oFE9D6WLseCv4FPkggaOJWlEljSe2BAuvWzRQ4EGtw6r5WjfZqIraxKjxtsoQ4yBEfldCRi5cdfihc/dBhqIFjqp+3BMXxdhSemt6Y7zHxf9/FYOxwH2e9b7oaJ3EQi8aUc1BXO0j/Icq2UPzpt/N+Rc+kjZsD96/sFbkUZHemIHZO2u4cERWSTp84desd00Fif2FixXqymYETssnRtt6sBj52yRX8s+E+YvlucPRgLyzOmZRIg2xh+vjQWXDIvYWMSgGxJh6gm+bbtVxSMDBSBXRaPBWlNm39zkRZa9AdqY7bBC5cnmhgNU/GJGuIBhO+NuOKySnOtqzBfUDJ6yNCR3BEQwfSMrcvBnx1adyxGggFwwuTzms4GYBeVtoVzYNZVs4aTaFZe7fq5k2o+83poDcvQjryFNdXUEp12Mlwd6hsk1mYBhLUJ475ztTn1KT5M2+RxaQQFzJtP1CW2Q3wXSGMvkS3hYPw4irF+n7/+eBPiVj/mNSXCv2Ej4Tjjy2xGBiH4SqfUq+FgIDhunwSIK1MU3TobAgPImN6zHD65nnJAQXaJGH7cVfqanoAicWi0B82XUHnsl8tIQ19fdUfaORdDnw0w1d+Y/jkRW5yDgzjuo3RbYM7c5ADDUjfsNa6/Waeg9IiVYu57wYKyxVpy5DPs6MaLnIVkwwYTsR99jz3Z2+ov589EuPlBgHRJGDXzsM8VNeHOI6E1PcceT//ZmN+GwghgJwTE7t4n1gUCbSNYvaDGlg+rPKNyocZnpeQVrqhr8hP+mmFv7bUrYi6OXruR7FYfSQKEyqDuyWXh3vPorwOB+V2fX7bM+BRiFavsTY8ni1Zc9EbxDxHQC1usUa3Fbv7mQ+ZWicvCZBgWZjx0Q12Zis67/OScg1M9LhREQ95VYmAUtL7NMh5dc7NRZQWkiFV6HhKdRqkQ+h+5UFYP3x7xhpJL8vdjYNWMdJ13xrykFJrFgY1z30HAIKEra9pwM0dTq4DulD3qNK167sepPdGORS2MJHz3liFsvYAlkzyzFaE25FoTiUzwjp8Xtt3a88eyneU2Pqah3hYPRCa/p7v39gruH/Ki1twbfv7CQUNDZlUR4OxIwmvy93HGZ4Gd1kT+bfmY+NSe9TTfYlHszL6bYc412iuNz8fpOuvBhSc2Oe7Ths/UPQ=';
****/
/***
$de_str=
'{"result_code":1,"result_data":{"id":"5825487","username":"N96qAsCIDnNB0KJWT","mobile":"13305710129","is_edit":"1","udid":"","rand_str":"8893591e33","password":"ddb0bc7cb00118c22dca00e49b61f147","nick":"\u73a9\u5bb65825487","head_image_url":"http:\/\/api.nhbia.cn\/uploads\/images\/20180314\/small_thumb\/15210191944541_thumb.png","nature":"0","sex":"1","birthday":"0","signature":"\u8fd9\u4e2a\u5bb6\u4f19\u5f88\u61d2\uff0c\u4ec0\u4e48\u90fd\u6ca1\u7559\u4e0b...","status":"1","wb_user_id":0,"invitation_code":"6TC1MK","uid":"5825487","need_update_info":0,"anchor_id":0,"token":"f3f74f4b12bcc5be43c54eac6d4d3360","income_yb":"0.00","anchor":0,"experience":0,"watermark":null,"nick_edit_count":0,"user_level":"1","max_experience":101,"user_group":"11","style":"","name_color":"","xd":0,"yb":1003261,"certification":0,"lrs_win_rate":0,"lrs_win_num":0,"lrs_fail_num":0,"lrs_group_name":"","lrs_level_name":"LV.1","lrs_level":1,"lrs_experience":0,"lrs_max_experience":99,"dan_info":{"dan_value":40,"dan_level":0,"dan_max_value":60,"dan_show":0},"ranking":{"live_ranking":0,"rich_ranking":0},"checkin_flag_display":0,"xmpp":{"xmpp_domain":"kwc.im","xmpp_server":"60.205.163.42","xmpp_port":"35222","xmpp_room_domain":"muc.kwc.im","xmpp_c_key":"ADGOKMIODGVTFMRDX","xmpp_s_key":"QAZOPSUNAGBYHNUJM","xmpp_username":"1000185825487","xmpp_nick":"1000185825487","xmpp_password":"a4d0c2391a"},"corporation_id":"100018"}}';
print("\n\n**********格式化字符串*********");
print("\n\n");

echo decodeUnicode($de_str);
$de_str=decodeUnicode($de_str);
echo _format_str($de_str);
$f_de_str=_format_str($de_str);
print("\n\n");
$a_str = explode("\n", $f_de_str);
		//写入文件

print("\n**********写入文件*********\n");
$table_change = array('\\/'=>'\\');
		
foreach($a_str as $val){

     $val2=strtr($val,$table_change) . "\n";

	 echo $val2;  
	#fwrite($fp2,$val."\n");
}
****/
?> 