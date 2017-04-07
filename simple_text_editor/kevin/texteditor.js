'use strict'

const Pair = require('./pair')

class TextEditor {
  constructor () {
    this.input_stack = []
    this.string = ''
  }
  createOperation (op, word) {
    return new Pair(op, word)
  }
  append (input) {
    console.log(`appending ${input}`)
    if (typeof input === 'string' || input instanceof String) {
      this.input_stack.push(this.create_operation(1, input))
      this.string += input
    } else {
      console.log(`Invalid input type. Type of ${input} is not of type string...`)
      process.exit(1)
    }
  }

  delete (k) {
    console.log(`deleting ${k}`)
    if (Number.isInteger(k)) {
      const suffix = this.string.slice(-k)
      this.string = this.string.substr(0, this.string.length - k)
      this.input_stack.push(this.create_operation(2, suffix))
    } else {
      console.log(`Tried to delete a non integer value: ${k}`)
      process.exit(1)
    }
  }

  print (k) {
    if (Number.isInteger(k)) {
      console.log(this.string.slice(0, k))
    } else {
      console.log(`Tried to print a non integer amount of chars: ${k}`)
      process.exit(1)
    }
  }

  undo () {
    if (this.input_stack.length === 0) {
      console.log('nothing to undo')
      return
    }
    const pair = this.input_stack.pop()
    if (pair.operation === 1) {
      const wordLen = pair.text.length
      this.delete(wordLen)
    } else if (pair.operation === 2) {
      this.append(pair.text)
    }
  }
}

module.exports = TextEditor
