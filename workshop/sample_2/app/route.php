<?php
$urlPath = explode('/', $_SERVER['REQUEST_URI']);
array_shift($urlPath);

if ($urlPath[0] === 'api') {
    require_once(__DIR__ . '/api/index.php');
} else if ($urlPath[0] === 'static') {
    return false;
} else {
    require_once(__DIR__ . '/index.html');
}