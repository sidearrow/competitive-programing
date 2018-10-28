<?php
use Illuminate\Http\Request;

Route::get('/', function (Request $request) {
    Log::info('cookie', ['test' => $request]);

    if ($request->cookie('user_id')) {
        return response()->json(['aa'], 303);
    }
    return view('index');
});
