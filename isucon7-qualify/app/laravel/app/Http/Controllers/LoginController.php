<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Model\User;

class LoginController extends Controller
{
    public function get()
    {
        return view('login');
    }

    public function post(Request $request, $name, $password)
    {
        $modelUser = new User();
        $user = $modelUser->getUser();
        if (!$user || $user['password'] !== sha1(utf8_encode($user['salt'] . $password))) {
            return response('', 403);
        }
        response()->cookie('user_id', $user['id']);
        return redirect('/', 303);
    }
}
