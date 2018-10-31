<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class IndexController extends Controller
{
    public function __invoke(Request $request)
    {
        if ($request->cookie('user_id')) {
            return redirect()->route('channel', ['channel_id' => '1'], 303);
        }
        return view('index');
    }
}
