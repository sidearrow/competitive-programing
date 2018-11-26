<?php

namespace Tests\Feature;

use Tests\TestCase;

class IndexTest extends TestCase
{
    /*
    public function testIndexNotSetCookie()
    {
        $response = $this->get('/');
        $response->assertStatus(200);
    }

    public function testIndexSetCookie()
    {
        $response = $this->call('GET', '/', [], ['user_id' => 'test']);
        $response->assertStatus(303);
    }
    */

    public function _testRegister()
    {
        $response = $this->call('GET', '/register');
        $response->assertStatus(200);

        $response = $this->call('POST', '/register');
        $response->assertStatus(400);

        $response = $this->call('POST', '/register?name=name&password=password');
        $response->assertStatus(303);
    }

    public function testLogout()
    {
        $response = $this->get('/logout');
        $response
            ->assertStatus(303)
            ->assertRedirect('/')
            ->assertCookie('user_id', '0');
    }
}
