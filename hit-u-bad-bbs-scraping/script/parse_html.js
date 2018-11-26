const fs = require('fs')
const jsdom = require('jsdom')

const { JSDOM } = jsdom

const map = [
  [23, 3, 12],
  [22, 13, 22],
  [21, 23, 34],
  [20, 35, 44],
  [19, 45, 55],
  [18, 56, 64],
  [17, 65, 75],
  [16, 76, 83],
  [15, 84, 96],
  [14, 97, 105],
  [13, 106, 115],
  [12, 116, 126],
  [11, 127, 138],
  [10, 139, 147],
  [9, 148, 157],
  [8, 158, 167],
  [7, 168, 177],
  [6, 178, 187],
  [5, 188, 198],
  [4, 199, 208],
  [3, 209, 218],
  [2, 219, 228],
  [1, 229, 238],
]

let data = []

const getPageContent = (page, threadFrom, threadTo) => {
  
  const filePath = __dirname + '/../html/old_' + page + '.html'
  const document = (new JSDOM(fs.readFileSync(filePath))).window.document
  
  
  let thread = threadFrom
  let num = 1
  let tmp = {}
  const getContent = () => {
    console.log(thread + '_' + num)
    const root = document.querySelector('div[id="' + thread + '_' + num + '"]')
    if (root === null || thread === 33) {
      thread++
      if (thread > threadTo) {
        return
      }
      num = 1
    } else {
      tmp = {}
      tmp.thread = thread
      tmp.num = num
      tmp.title = document.querySelector('table[id="' + thread + '"]>tbody>tr>td>div>span>a').textContent
      tmp.content = root.querySelector('span').outerHTML
      tmp.content_all = root.innerHTML
      if (thread === 140 && num === 3) {
        tmp.author = ''
      } else {
        tmp.author = root.querySelector('b').textContent
      }
      data.push(tmp)
      num++
    }
  
    getContent()
  }
  
  getContent()
}

map.forEach((v) => {
  getPageContent(v[0], v[1], v[2])
})

fs.writeFileSync(__dirname + '/../tmp/bbs.json' , JSON.stringify(data))