const fetchData = function (params) {
  const baseUrl = 'http://localhost:8080/api/'
  fetch(baseUrl + params)
    .then(function (res) {
      return res.json()
    })
    .then(function (res) {
      const main = document.getElementById('main')
      main.innerHTML = res.data
    })
}

const parseUrl = function () {
  return location.hash.split('/')
}

let hash
hash = parseUrl()
fetchData(hash[1])

window.addEventListener('hashchange', function () {
  hash = parseUrl()
  fetchData(hash[1])
})