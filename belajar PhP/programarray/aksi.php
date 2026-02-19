<?php
    #var_dump($_POST);\
    #echo $_GET['nim'];
    echo $_GET ['fav_language'];
    foreach ($_GET['vehicle'] as $key => $value) {
        echo "$value <br>";
    }

?>