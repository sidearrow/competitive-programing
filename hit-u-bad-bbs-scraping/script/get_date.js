const fs = require('fs')

const json = fs.readFileSync(__dirname + '/../tmp/bbs.json')
const _data = JSON.parse(json)
const datePattern = new RegExp(/\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d/)

let date
let data = []
_data.forEach((v) => {
  let tmp = v.content_all.match(datePattern)
  if (tmp === null) {
    date = null
  } else {
    date = tmp[0]
  }

  v.date = date
  delete v.content_all

  data.push(v)
})

fs.writeFileSync('bbs2.json', JSON.stringify(data))