<?php
$nilai = 60;

if($nilai >= 90){
   echo "A"; 
}
elseif($nilai >= 80 and $nilai < 90){
   echo "B"; 
}
elseif($nilai >= 70 and $nilai < 80){
   echo "C"; 
}
elseif($nilai >= 60 and $nilai < 70){
   echo "D"; 
}
else{
    echo "E";
}
?>