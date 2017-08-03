'use strict'

// Brute Force
function numPicker (nums) {
  nums.sort()
  let max = 0
  let counter = 1
  for (var i = 0; i < nums.length; i++) {
    for (var j = i + 1; j < nums.length; j++) {
      if ((Math.abs(nums[i] - nums[j]) <= 1)) {
        counter++
      } else {
        break
      }
    }
    if (counter > max) {
      max = counter
    }
    counter = 1
  }
  return max
}

module.exports = numPicker
