window.onload = function () {
  document.getElementById('button').addEventListener('click', function () {
    const counter = document.querySelector('#counter');
    const nowNum = Number(counter.innerHTML);
    counter.innerHTML = String(nowNum + 1);
  });
}