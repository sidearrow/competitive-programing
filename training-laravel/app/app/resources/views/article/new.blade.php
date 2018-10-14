@extends('layouts.app')

@section('content')
<form action="/article/post" method="POST">
  <div>
    <label>Title<input type="text"></label>
  </div>
  <div>
    <label>Content<textarea></textarea></label>
  </div>
  <input type="submit">
</form>
@endsection