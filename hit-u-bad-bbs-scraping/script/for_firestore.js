const fs = require('fs')

const json = fs.readFileSync(__dirname + '/../tmp/bbs.json')
const _data = JSON.parse(json)

let tmp = ''
let data = []
_data.forEach((v) => {
  v.updatedAt = v.created_at
  v.createdAt = v.created_at
  v.password = '1111'
  delete v.created_at
  delete v.id_2
  delete v.thread
  if (tmp === v.id_1) {
    delete v.id_1
    data[data.length-1].comments.push(v)
  } else {
    v.comments = []
    tmp = v.id_1
    delete v.id_1
    data.push(v)
  }
})

fs.writeFileSync(__dirname + '/../tmp/bbs_for_firestore.json', JSON.stringify(data))