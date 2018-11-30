<?php
$str = [
    'data' => 'hello PHP'
];

header('Content-Type: application/json; charset=utf-8');
echo json_encode($str);