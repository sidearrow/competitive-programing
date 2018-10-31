<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RegisterController extends Controller
{
    public function get() {
        return view('register');
    }

    public function post(Request $request) {
        $name = $request->query('name');
        $password = $request->query('password');
        if (!$name || !$password) {
            return response('', 400);
        }
        return redirect()->route('index', [], 303);
    }
}
