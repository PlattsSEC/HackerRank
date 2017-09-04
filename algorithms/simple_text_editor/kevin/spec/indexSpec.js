/* es-lint jasmine */
'use strict'
// https://www.hackerrank.com/challenges/picking-numbers

// TODO make better undo tests
const Pair = require('../pair')
const TextEditor = require('../texteditor')
require('jasmine')

describe('Pair Tests:', () => {
  it('Pair Instantiation 1', () => {
    const pair = new Pair(1, 'hello world')
    expect(pair.operation).toBe(1)
    expect(pair.text).toBe('hello world')
  })

  it('Pair Instantiation 2', () => {
    const pair = new Pair(2, 'hello')
    expect(pair.operation).toBe(2)
    expect(pair.text).toBe('hello')
  })
})

describe('TextEditor createOperation Tests:', () => {
  const textEditor = new TextEditor()
  const expected = new Pair(1, 'hello')

  beforeEach(() => {
    spyOn(textEditor, 'createOperation').and.callThrough()
  })

  it('TextEditor createOperation', function () {
    const createOperation = textEditor.createOperation(1, 'hello')
    expect(textEditor.createOperation).toHaveBeenCalledWith(1, 'hello')
    expect(createOperation.operation).toEqual(expected.operation)
    expect(createOperation.word).toEqual(expected.word)
  })
})

describe('TextEditor Append Tests:', () => {
  const textEditor = new TextEditor()
  const expectedAfterFirstAppend = 'hello'
  const expectedAfterSecondAppend = 'hello world'
  beforeEach(() => {
    spyOn(textEditor, 'append').and.callThrough()
  })
  it('TextEditor Append ', () => {
    textEditor.append('hello')
    expect(textEditor.append).toHaveBeenCalledWith('hello')
    expect(textEditor.string)
      .toEqual(expectedAfterFirstAppend)

    textEditor.append(' world')
    expect(textEditor.append).toHaveBeenCalledWith(' world')
    expect(textEditor.string)
      .toEqual(expectedAfterSecondAppend)
  })
})

describe('Text Editor Delete Tests', () => {
  const textEditor = new TextEditor()
  const input = 'hello'
  textEditor.append(input)
  beforeEach(() => {
    spyOn(textEditor, 'delete').and.callThrough()
    textEditor.delete(2)
  })

  it('delete 2 was called', () => {
    expect(textEditor.delete).toHaveBeenCalledWith(2)
    const deleted = textEditor.string
    expect(deleted).toEqual('hel')
  })

  it('TextEditor Delete 4 ', () => {
    expect(textEditor.delete).toHaveBeenCalledWith(2)
    const deleted = textEditor.string
    expect(deleted).toEqual('h')
  })

  it('TextEditor Delete 6 ', () => {
    expect(textEditor.delete).toHaveBeenCalledWith(2)
    const deleted = textEditor.string
    expect(deleted).toEqual('')
  })
  it('TextEditor Delete On Empty string ', () => {
    expect(textEditor.delete).toHaveBeenCalledWith(2)
    const deleted = textEditor.string
    expect(deleted).toEqual('')
  })
})

describe('Text Editor Print Tests', () => {
  const textEditor = new TextEditor()
  const input = 'hello'
  textEditor.append(input)
  beforeEach(() => {
    spyOn(textEditor, 'print').and.callThrough()
    spyOn(console, 'log').and.callThrough()
  })

  it('print(3) was called', () => {
    const expected = 'hel'
    const actual = textEditor.print(3)
    expect(textEditor.print).toHaveBeenCalledWith(3)
    expect(console.log).toHaveBeenCalled()
    expect(actual).toEqual(expected)
  })

  it('printing with integer greater than string length', () => {
    const expected = 'hello'
    const actual = textEditor.print(10)
    expect(textEditor.print).toHaveBeenCalledWith(10)
    expect(console.log).toHaveBeenCalled()
    expect(actual).toEqual(expected)
  })
})

describe('Text Editor Undo Tests', () => {
  const textEditor = new TextEditor()
  beforeEach(() => {
    spyOn(textEditor, 'undo').and.callThrough()
  })

  afterEach(() => {
    textEditor.inputStack.length = 0
    textEditor.string = ''
  })

  it('Undo Empty', () => {
    const expected = ''
    const actual = textEditor.undo()
    expect(textEditor.undo).toHaveBeenCalled()
    expect(textEditor.inputStack.length).toEqual(0)
    expect(actual).toEqual(expected)
  })

  it('Undo Append', () => {
    const expected = ''
    textEditor.append('hello')
    expect(textEditor.inputStack.length).toEqual(1)
    expect(textEditor.string).toEqual('hello')
    textEditor.undo()
    expect(textEditor.undo).toHaveBeenCalled()
    expect(textEditor.inputStack.length).toEqual(1)
    expect(textEditor.inputStack[0].operation).toEqual(2)
    expect(textEditor.inputStack[0].text).toEqual('hello')
    expect(textEditor.string).toEqual(expected)
  })
  it('Undo Delete', () => {
    textEditor.append('hello')
    expect(textEditor.inputStack.length).toEqual(1)
    expect(textEditor.string).toEqual('hello')
    textEditor.delete(2)
    expect(textEditor.inputStack.length).toEqual(2)
    expect(textEditor.string).toEqual('hel')
    textEditor.undo()

    expect(textEditor.undo).toHaveBeenCalled()
    expect(textEditor.inputStack.length).toEqual(2)
    expect(textEditor.inputStack[1].operation).toEqual(1)
    expect(textEditor.inputStack[1].text).toEqual('lo')
    expect(textEditor.string).toEqual('hello')
  })
})
