<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Channel extends Model
{
    protected $table = 'channel';

    public static function getChannelListInfo($focusedChannelId = null)
    {
        $channels = Channel::orderBy('id')->get();
        $description = '';

        foreach ($channels as $channel) {
            if ((int)$channel['id'] === (int)$focusedChannelId) {
                $description = $channel['description'];
                break;
            }
        }

        return [$channels, $description];
    }
}
