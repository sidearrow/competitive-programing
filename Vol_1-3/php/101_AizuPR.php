<?php
$inputs = getInputs();

$first_flag = true;
foreach ($inputs as $val) {
    echo str_replace('Hoshino', 'Hoshina', $val);
}

function getInputs() {
    $inputs = array();
    $data_set_num = trim(fgets(STDIN));
    for ($i = 0; $i < $data_set_num; $i++) {
        $inputs[] = fgets(STDIN);
    }
    return $inputs;
}
