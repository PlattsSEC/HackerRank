'use strict'

const Pair = require('./pair')

class TextEditor {
  constructor () {
    this.inputStack = []
    this.string = ''
  }
  createOperation (op, word) {
    return new Pair(op, word)
  }
  append (input) {
    if (typeof input === 'string' || input instanceof String) {
      this.inputStack.push(this.createOperation(1, input))
      this.string += input
    } else {
      console.log(`Invalid input type. Type of ${input} is not of type string...`)
      process.exit(1)
    }
  }

  delete (k) {
    if (Number.isInteger(k)) {
      const suffix = this.string.slice(-k)
      this.string = this.string.substr(0, this.string.length - k)
      this.inputStack.push(this.createOperation(2, suffix))
    } else {
      console.log(`Tried to delete a non integer value: ${k}`)
      process.exit(1)
    }
  }

  print (k) {
    if (Number.isInteger(k)) {
      const output = this.string.slice(0, k)
      console.log(output)
      return output
    } else {
      console.log(`Tried to print a non integer amount of chars: ${k}`)
      process.exit(1)
    }
  }

  undo () {
    if (this.inputStack.length === 0) {
      return ''
    }
    const pair = this.inputStack.pop()
    if (pair.operation === 1) {
      const wordLen = pair.text.length
      return this.delete(wordLen)
    } else if (pair.operation === 2) {
      return this.append(pair.text)
    }
  }
}

module.exports = TextEditor
