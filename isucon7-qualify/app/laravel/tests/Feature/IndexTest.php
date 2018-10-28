<?php

namespace Tests\Feature;

use Tests\TestCase;

class IndexTest extends TestCase
{
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
}
