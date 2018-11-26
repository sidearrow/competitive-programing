<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LogoutController extends Controller
{
    public function get()
    {
        return redirect('/', 303)->cookie('user_id', 0);
    }
}
