fetch('http://localhost:8080/api')
  .then(function (res) {
    return res.json()
  })
  .then(function (res) {
    const main = document.getElementById('main')
    main.innerHTML = res.data
  })