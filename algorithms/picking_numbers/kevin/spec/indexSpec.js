'use strict'
// https://www.hackerrank.com/challenges/picking-numbers
var numPicker = require('../index.js')
var test = require('tape')

test('HackerRank Sample 0', function (assert) {
  const input = [4, 6, 5, 3, 3, 1]
  const nums = numPicker(input)
  const expected = 3
  assert.equal(nums, expected, `If ${input}: Then ${nums} should equal ${expected}`)
  assert.end()
})

test('HackerRank Sample 1', function (assert) {
  const input = [1, 2, 2, 3, 1, 2]
  const nums = numPicker(input)
  const expected = 5
  assert.equal(nums, expected, `If ${input}: Then ${nums} should equal ${expected}`)
  assert.end()
})

test('HackerRank Sample 2', function (assert) {
  const input = [1, 2, 2, 3, 1, 2, 1, 2]
  const nums = numPicker(input)
  const expected = 7
  assert.equal(nums, expected, `If ${input}: Then ${nums} should equal ${expected}`)
  assert.end()
})
