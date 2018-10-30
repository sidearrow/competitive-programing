<?php

namespace Tests\Unit;

use Tests\TestCase;
//use Illuminate\Foundation\Testing\RefreshDatabase;

use App\Models\Channel;

class ModelsChannelTest extends TestCase
{
    public function testGetChannelListInfo()
    {
        $res = Channel::getChannelListInfo();
        $this->assertEquals($res[1], '');

        $res = Channel::getChannelListInfo(1);
        $this->assertEquals($res[1], 'ここは 1ちゃんねるです');
    }
}
