let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
input = input.map(n => parseInt(n))
T = input[0]


for(let tc=1; tc<T+1; tc++){
  let N = input[tc]
  const dp = Array.from({length: N+2}, (v, i) => [0, 0]);
  dp[0] = [1, 0]
  dp[1] = [0, 1]
  for(let i=2; i<=N; i++) {
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
  }
  console.log(...dp[N])
  
}