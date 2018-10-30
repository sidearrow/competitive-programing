<?php
use Illuminate\Http\Request;

Route::get('/', function (Request $request) {
    if ($request->cookie('user_id')) {
        return redirect()->route('channel', ['channel_id' => '1'], 303);
    }
    return view('index');
});

Route::get('/channel/{channel_id}', function (Request $request, $channelId) {
    list($channels, $description) = App\Models\Channel::getChannelListInfo($channelId);
    return view('channel', [
        'channels' => $channels,
        'channel_id' => $channelId,
        'description' => $description
    ]);
})->name('channel');