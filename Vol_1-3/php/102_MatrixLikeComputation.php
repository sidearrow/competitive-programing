<?php
$inputs = getInputs();

$sum_all = 0;
foreach ($inputs as $val_a) {
    $sum_tate = array();
    foreach ($val_a as $val_b) {
        $output = '';
        $index = 0;
        $sum_yoko = 0;
        $sum_tate[$index] = (empty($sum_tate[$index])) ? 0 : $sum_tate[$index];
        foreach ($val_b as $val_c) {
            $sum_yoko += (int)$val_c;
            $sum_tate[$index] += (int)$val_c;
            $output .= putSpace((int)$val_c);
            $index++;
        }
        $output .= putSpace((int)$sum_yoko);
        $sum_all += (int)$sum_yoko;
        echo $output;
        echo "\n";
    }
    $output = '';
    foreach ($sum_tate as $val) {
        $output .= putSpace($val);
    }
    echo $output . putSpace($sum_all);
}

function getInputs() {
    $inputs = array();
    while (true) {
        $data_set_num = trim(fgets(STDIN));
        if ($data_set_num === '0') {
            break;
        }
        $index = 0;
        for ($i = 0; $i < $data_set_num; $i++) {
            $inputs[$index][] = explode(' ', trim(fgets(STDIN)));
        }
        $index++;
    }
    return $inputs;
}

function putSpace ($num) {
    $space = '';
    if ($num < 10) {
        $space = '    ';
    } elseif ($num < 100) {
        $space = '   ';
    } else {
        $space = '  ';
    }
    return $space . $num;
}
