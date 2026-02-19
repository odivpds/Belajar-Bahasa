<?php
$umur = array("jorge"=>"29",
        "jenifer"=>"28");
$umur['Mangjorge'] = "29";
$umur['jenifer'] = "28";


foreach ($umur as $key => $value) {
    echo "umurnya $key adalah $value tahun";
}
?>