const fs = require('fs')

const json = fs.readFileSync(__dirname + '/../tmp/bbs2.json')
const _data = JSON.parse(json)

let data = []
_data.forEach((v) => {
  v.content = v.content.replace(new RegExp(/<br>/g), '\n')
  v.content = v.content.replace(new RegExp(/<span style="color:black;">/), '')
  v.content = v.content.replace(new RegExp(/<\/span>/), '')
  v.content = v.content.replace(new RegExp(/&lt;/g), '<')
  v.content = v.content.replace(new RegExp(/&gt;/g), '>')
  v.content = v.content.replace(new RegExp(/<img src="emoji\/img\/i\/63879\.gif" alt="" border="0" width="12" height="12">/g), '[1]')
  v.content = v.content.replace(new RegExp(/<img src="emoji\/img\/i\/63880\.gif" alt="" border="0" width="12" height="12">/g), '[2]')
  v.content = v.content.replace(new RegExp(/<img src="emoji\/img\/i\/63881\.gif" alt="" border="0" width="12" height="12">/g), '[3]')
  v.content = v.content.replace(new RegExp(/<img src="emoji\/img\/i\/63882\.gif" alt="" border="0" width="12" height="12">/g), '[4]')
  v.content = v.content.replace(new RegExp(/<img src="emoji\/img\/i\/63883\.gif" alt="" border="0" width="12" height="12">/g), '[5]')
  data.push(v)
})

fs.writeFileSync(__dirname + '/../tmp/bbs3.json', JSON.stringify(data))