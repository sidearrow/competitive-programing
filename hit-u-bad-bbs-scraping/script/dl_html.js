const fs = require('fs')
const http = require('http')

const urlBase = 'http://bbs.mottoki.com/index?bbs=ikkyo_bad&page='

const maxPage = 23

let nowPage = 1
let tmp = ''

const dlHtml = () => {
  tmp = String(nowPage)
  http.get(urlBase + tmp, (res) => {
    res.pipe(fs.createWriteStream('html/old_' + tmp + '.html'))
    nowPage++
    if (nowPage <= maxPage) {
      dlHtml()
    } else {
      return
    }
  })
}

dlHtml()