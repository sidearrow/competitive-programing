<?php

$host = getenv('ISUBATA_DB_HOST') ?: 'localhost';
$port = getenv('ISUBATA_DB_PORT') ?: '3306';
$user = getenv('ISUBATA_DB_USER') ?: 'root';
$password = getenv('ISUBATA_DB_PASSWORD') ?: '';
$dsn = "mysql:host={$host};port={$port};dbname=isubata;charset=utf8mb4";

echo $dsn;

$pdo = new PDO(
    $dsn,
    $user,
    $password
);