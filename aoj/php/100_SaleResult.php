<?php
$inputs = getInputs();

$data = array();
$data_set_num = 0;
foreach ($inputs as $val) {
    if (strpos($val, ' ') === false) {
        $data_set_num++;
        $data[$data_set_num] = array();
        continue;
    }
    $tmp = explode(' ', $val);
    $sum = (int)$tmp[1] * (int)$tmp[2];
    if (array_key_exists($tmp[0], $data[$data_set_num])) {
        $data[$data_set_num][$tmp[0]] += $sum;
    } else {
        $data[$data_set_num][$tmp[0]] = $sum;
    }
}

foreach ($data as $val_a) {
    $na_flag = true;
    foreach ($val_a as $key_b => $val_b) {
        if ($val_b >= 1000000) {
            $na_flag = false;
            echo $key_b;
            echo "\n";
        }
    }
    if ($na_flag) {
        echo 'NA';
        echo "\n";
    }
}

function getInputs() {
    $inputs = array();
    while(true) {
        $input = trim(fgets(STDIN));
        if ($input === '0') {
           break;
        }
        $inputs[] = $input;
    }
    return $inputs;
}
