<?php

use Illuminate\Http\Request;

Route::get('/articles', 'ArticleController@index');
Route::post('/articles', 'ArticleController@create');
