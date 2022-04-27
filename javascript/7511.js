let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const find_ = (x, p) => {
  if (x === p[x]){
    return x
  }
  else {
    p[x] = find_(p[x], p)
    return p[x]
  }
}

const union_ = (x, y, p) => {
  x = find_(x, p)
  y = find_(y, p)
  if (x === y) return;
  else if (x > y) p[x] = y
  else p[y] = x
}


idx = 0
T = parseInt(input[idx++])
result = ""
for (let tc = 1; tc <= T; tc++) {
  result += `Scenario ${tc}:\n`
  const arr = new Array()
  n = parseInt(input[idx++])
  const p = Array.from({length: n}, (v, i) => i)
  
  k = parseInt(input[idx++])
  for (let i = 0; i < k; i++) {
    tmp = input[idx++].split(' ').map(n => parseInt(n))
    union_(...tmp, p)
  }
  m = parseInt(input[idx++])
  for (let i = 0; i < m; i++){
    tmp = input[idx++].split(' ').map(n => parseInt(n))
    result += (find_(tmp[0], p)===find_(tmp[1], p)) ? '1\n' : '0\n'
  }
  if (tc != T) result += '\n'
}
console.log(result)