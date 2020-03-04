
const fizz = function (x) {
  // check to see if x is defined/exists
  if (typeof x !== 'undefined') {
    // yes, it exists, carry on
  } else {
    // no, it does not exist, throw an error
    throw new Error('there is no input')
  }

}

module.exports = {
  fizz
}