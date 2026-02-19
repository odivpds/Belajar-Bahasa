<?php
$kegiatanhari='jumat';

switch($kegiatanhari){
    case'senin';
    case'selasa';
    case'rabu';
    case'kamis';
        echo 'kuliah';
        break;
case'jumat':
    echo'ketemu bu rara<br>';
    break;
case'sabtu':
    echo'ketemu bu gio<br>';
    break;
default:
    echo'pacaran ma ayang';
}

?>