<?php
$domain = 'bdfajsdflajdflug';//get_domain();
$post_data = array(
	'query' => $domain,
	'suffix' => array('.com')
);
$ch = curl_init();
$option = array(
	CURLOPT_URL => "http://iisp.com/domain/mcheck.php",
	CURLOPT_HEADER => false,
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_POST => true,
    CURLOPT_TIMEOUT => 30,
	CURLOPT_POSTFIELDS => http_build_query($post_data)
);
curl_setopt_array($ch, $option);
$ret = curl_exec($ch);
if (strpos($ret, '#009900') > 0) {
    echo 'aaa';
}
curl_close($ch);

function get_domains()
{
	$domains = array();
	$num = array(0,1,2,3,4,5,6,7,8,9);
	$char = explode('', 'abcdefghijklmnopqrstuvwxyz');
	foreach ($num as $a) {
		foreach ($num as $b) {
			foreach ($num as $c) {
				$domains[] = $a . $b . $c;
			}
		}
	}
	foreach ($char as $a) {
		foreach ($char as $b) {
			foreach ($char as $c) {
				$domains[] = $a . $b . $c;
			}
		}
	}

	return $domains;
}
