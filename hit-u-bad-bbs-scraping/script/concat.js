const fs = require('fs')

const oldData = JSON.parse(fs.readFileSync(__dirname + '/../tmp/bbs_old.json'))
const newData = JSON.parse(fs.readFileSync(__dirname + '/../tmp/bbs_new.json'))

let data = []
let id = 0
let tmp = 0
oldData.forEach((v) => {
  if (v.thread >= 161) {
    return
  }
  if (tmp !== v.thread) {
    id++
    tmp = v.thread
  }
  v.created_at = v.date
  v.id_1 = id
  v.id_2 = v.num
  delete v.date
  delete v.thread
  delete v.num
  data.push(v)
})
newData.forEach((v) => {
  id++
  v.id_1 = id
  v.id_2 = 1
  data.push(v)
})

fs.writeFileSync(__dirname + '/../tmp/bbs.json', JSON.stringify(data))