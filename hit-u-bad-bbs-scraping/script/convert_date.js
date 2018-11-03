const fs = require('fs')

const json = fs.readFileSync(__dirname + '/../tmp/bbs_new.json')
const _data = JSON.parse(json)

const formatDate = (dateString) => {
  const date = new Date(dateString)
  date.setTime(date.getTime() + 1000 * 60 * 60 * 9);
  const z = (str) => {
    return ('0' + String(str)).slice(-2)
  }

  return date.getFullYear() + '/' +
         z((date.getMonth() + 1)) + '/' +
         z(date.getDate()) + ' ' +
         z(date.getHours()) + ':' +
         z(date.getMinutes()) + ':' +
         z(date.getSeconds())
}

let data = []
_data.forEach((v, i) => {
  v.created_at = formatDate(v.date)
  v.thread = i
  delete v.date
  delete v.password

  data.push(v)
})

fs.writeFileSync(__dirname + '/../tmp/bbs_new2.json', JSON.stringify(data))