@extends('layouts.app')

@section('content')
<form action="/article/post" method="POST">
  {{ csrf_field() }}
  <div>
    <label>Title<input type="text" name="title"></label>
  </div>
  <div>
    <label>Content<textarea name="content"></textarea></label>
  </div>
  <input type="submit">
</form>
@endsection