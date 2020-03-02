

describe('A FizzBuzz program', () => {
  it('has a smoke test', () => {
    expect(true).toBe(true)
  })

  describe('A fizz() function', () => {
    it('throws and error if there is no input', () => {
      expect(fizz()).toThrow()
    })
  })
})