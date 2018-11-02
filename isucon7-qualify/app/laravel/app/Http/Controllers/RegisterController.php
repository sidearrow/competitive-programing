<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Model\User;

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
        $modelUser = new User();
        $userId = $modelUser->store($name, $password);
        if ($userId === null) {
            return response('', 409);
        }
        response()->cookie('user_id', $userId);
        return redirect()->route('index', [], 303);
    }
}
