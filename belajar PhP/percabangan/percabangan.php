<?php
$bangundatar='persegi';

switch($bangundatar){

case'segitiga':
    echo'jumlah sisinya 3<br>';
    echo'besar setiap sudut 60 derajat<br>';
    echo'memiliki alas dan tinggi';
    break;

case'persegi':
    echo'<p> jumlah sisinya 8 </p>';
    echo'besar sudutnya 90 derajat<br>';
    echo'memiliki sisi yang sama panjang';
    break;

default:
    echo'bangun ruang';
}

?>
