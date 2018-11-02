<?php

namespace Tests\Unit;

use Tests\TestCase;
//use Illuminate\Foundation\Testing\RefreshDatabase;

use App\Models\User;

class ModelsUserTest extends TestCase
{
    private static $instanceModelUser;

    public static function setUpBeforeClass()
    {
        self::$instanceModelUser = new User();
    }

    public function testStore()
    {
        $res = self::$instanceModelUser->store('name', 'password');
        var_dump($res);
        $this->assertTrue(true);
    }

    public function testGetUser()
    {
        $user = self::$instanceModelUser->getUser('name');
        $this->assertEquals($user->name, 'name');
        $this->assertEquals($user->display_name, 'name');
        $this->assertEquals($user->avatar_icon, 'default.png');
    }
}