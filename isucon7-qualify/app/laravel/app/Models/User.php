<?php

namespace App\Models;

use Illuminate\Support\Facades\DB;

class User
{
    private $table = 'user';

    private function randomString($length)
    {
        $str = "";
        while ($length--) {
            $str .= str_shuffle("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")[0];
        }
        return $str;
    }

    public function store($userName, $password)
    {
        $salt = $this->randomString(20);
        $passDigest = sha1(utf8_encode($salt . $password));

        try {
            $userId = DB::table($this->table)->insertGetId([
                'name'         => $userName,
                'salt'         => $salt,
                'password'     => $passDigest,
                'display_name' => $userName,
                'avatar_icon'  => 'default.png',
                'created_at'   => now(),
            ]);
        } catch (\PDOException $e) {
            $userId = null;
        }

        return $userId;
    }

    public function getUser($name)
    {
        return DB::table($this->table)->where('name', $name)->first();
    }
}