<?php

require_once("../public/op_file.php");
class AES {

    var $key = "1234567812345678";
    var $str = "";

    public function __set($key, $value){
        $this->$key = $value;
    }

    public function __get($key) {
        return $this->$key;
    }

    public function encrypt($input) {
        $size = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_ECB);
        $input = $this->pkcs5_pad($input, $size);
        $td = mcrypt_module_open(MCRYPT_RIJNDAEL_128, '', MCRYPT_MODE_ECB, '');
        $iv = mcrypt_create_iv (mcrypt_enc_get_iv_size($td), MCRYPT_DEV_URANDOM);
        mcrypt_generic_init($td, $this->key, $iv);
        $data = mcrypt_generic($td, $input);
        mcrypt_generic_deinit($td);
        mcrypt_module_close($td);
        #$data = $this->base64url_encode($data);
		$data = base64_encode($data);		
        return $data;
    }

    private function pkcs5_pad ($text, $blocksize) {
        $pad = $blocksize - (strlen($text) % $blocksize);
        return $text . str_repeat(chr($pad), $pad);
    }

    function strToHex($string)   
    {   
        $hex="";   
        for   ($i=0;$i<strlen($string);$i++)   
        $hex.=dechex(ord($string[$i]));   
        $hex=strtoupper($hex);   
        return   $hex;   
    }   
    function hexToStr($hex)   
    {   
        $string="";   
        for   ($i=0;$i<strlen($hex)-1;$i+=2)   
        $string.=chr(hexdec($hex[$i].$hex[$i+1]));   
        return   $string;   
    }

    public function decrypt($sStr) {
        $decrypted= mcrypt_decrypt(
            MCRYPT_RIJNDAEL_128,
            //$sKey,
            $this->key,
            base64_decode($sStr),
            //$this->base64url_decode($sStr),
            //$sStr,
            MCRYPT_MODE_ECB,
				''
        );
        $dec_s = strlen($decrypted);
        $padding = ord($decrypted[$dec_s-1]);
        $decrypted = substr($decrypted, 0, -$padding);
        return $decrypted;
    }
    /**
     *url 安全的base64编码 sunlonglong
     */
    function base64url_encode($data) { 
      return rtrim(strtr(base64_encode($data), '+/', '-_'), '='); 
    } 
    /**
     *url 安全的base64解码 sunlonglong
     */
    function base64url_decode($data) { 
      return base64_decode(str_pad(strtr($data, '-_', '+/'), strlen($data) % 4, '=', STR_PAD_RIGHT)); 
    }   
}

$aes = new AES();

//设置密钥
$aes->__set("key", "AKxNB89D3Fcgenkc");
$str=<<<___XXX
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
___XXX;

//对文件内容加密
//1.获取文件列表

$fileArray[]=null;
$fileArray=getFile("../in_data");
print("\n************处理输入数据文件列表**********\n");
print_r($fileArray);
//2.对列表循环
$count=0;
foreach ($fileArray as $key => $value) { 
	print("\n************开始处理文件**********");
	print($value . "\n");
	$fp = fopen( "$value",'r');
	if(file_exists("$value")) {
		$str2="";
		while (!feof($fp)) {

             $line = fgets($fp);
			 //echo $line;
             $str2 .=$line;
        }

		echo $str2;
		//对字符串加密
		echo $aes->encrypt($str2); 
		$en_str=$aes->encrypt($str2);
		//写入文件
		$fp2 = fopen(substr_replace("$value","en_",11,0),'w+');
        fwrite($fp2,$en_str);
        fclose($fp2);
        $en_str="";
		$count++;
		print('************结束处理文件**********');
	}
    fclose($fp);

    //fwrite($fp,'在读模式下写入');
    //fclose($fp);
    //echo $value . "2" . "<br>";  
} 
//print("共计处理文件".$count."个");
echo "\n共计处理文件" . "$count" . "个";
print("\n*********全部加密文件处理完毕**************\n\n");
//echo $aes->encrypt($str);
echo  'Who am I' . '<br>';
echo "\r\n";
echo $aes->decrypt("RaMFiBl3Lp8wuywd6c1k6A");
?>