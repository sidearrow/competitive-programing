<?php

namespace Tests\Unit;

use Tests\TestCase;
//use Illuminate\Foundation\Testing\RefreshDatabase;

use App\Models\User;

class ModelsUserTest extends TestCase
{
    public function testStore()
    {
        $user = new User();
        $res = $user->store('name', 'password');
        var_dump($res);
        $this->assertTrue(true);
    }
}