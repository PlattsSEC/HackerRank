'use strict'
const kevin = () => {
  console.log('HackerRank Javascript Attempt By Kevin Boyette')
}
kevin()
const equalStacks = () => {
  const h1 = [3, 2, 1, 1, 1]
  const h2 = [4, 3, 2]
  const h3 = [1, 1, 4, 1]

  let equalHeight = false
  const sum = (total, x) => { return total + x }
  const firstParamIsBiggest = (x, y, z) => { return x > y || x > z }
  const allAreEqual = (x, y, z) => { return x === y && y === z }

  let h1Total = h1.reduce(sum)
  let h2Total = h2.reduce(sum)
  let h3Total = h3.reduce(sum)

  while (!equalHeight) {
    if (firstParamIsBiggest(h1Total, h2Total, h3Total)) { h1Total -= h1.shift() }
    if (firstParamIsBiggest(h2Total, h1Total, h3Total)) { h2Total -= h2.shift() }
    if (firstParamIsBiggest(h3Total, h1Total, h2Total)) { h3Total -= h3.shift() }
    if (allAreEqual(h1Total, h2Total, h3Total)) { equalHeight = true }
  }
  console.log(h1Total)
}
equalStacks()
