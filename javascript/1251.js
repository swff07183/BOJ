let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input = input[0].split(' ')
word = input[0].split('')
let tmp, m1, m2
let result = '~'
for (let i=0; i<word.length-2; i++){
  for (let j=i+1; j<word.length-1; j++){
    tmp = ''
    tmp += word.slice(0, i+1).reverse().join('')
    tmp += word.slice(i+1, j+1).reverse().join('')
    tmp += word.slice(j+1, word.length+1).reverse().join('')
    if (tmp < result) {
      result = tmp
    }
  }
}
console.log(result)