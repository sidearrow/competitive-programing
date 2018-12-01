<?php
$data = 'hello PHP !!';
if (isset($urlPath[1])) {
    $data = $urlPath[1];
}

$str = [
    'data' => $data
];

header('Content-Type: application/json; charset=utf-8');
echo json_encode($str);