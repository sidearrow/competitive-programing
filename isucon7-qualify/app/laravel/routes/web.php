<?php
use Illuminate\Http\Request;

Route::get('/', 'IndexController')->name('index');

Route::get('/channel/{channel_id}', 'ChannelController@index')->name('channel');

Route::get('/register', 'RegisterController@get');
Route::post('/register', 'RegisterController@post');