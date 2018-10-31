<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ChannelController extends Controller
{
    public function index(Request $request, $channelId) {
        list($channels, $description) = App\Models\Channel::getChannelListInfo($channelId);
        return view('channel', [
            'channels' => $channels,
            'channel_id' => $channelId,
            'description' => $description
        ]);
    }
}
