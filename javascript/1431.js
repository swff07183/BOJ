let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
N = input[0]
const arr = Array.from({length: N}, (v, i) => input[i+1])

const get_sum = (word) => {
  word = word.split('').map(n => parseInt(n))
  total = 0
  for (n of word) {
    if (!isNaN(n)){
      total += n
    }
  }
  return total
}
arr.sort(
  (a, b) => {
    if (a.length > b.length) {
      return 1;
    }
    else if (a.length < b.length) {
      return -1;
    }
    else {
      let a_total = get_sum(a)
      let b_total = get_sum(b)
      if (a_total > b_total) {
        return 1;
      }
      else if (a_total < b_total){
        return -1;
      }
      else {
        if (a > b){
          return 1;
        }
        else {
          return -1;
        }
      }
    }
  }
)

for (num of arr) {
  console.log(num)
}
