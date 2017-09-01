function isPalindrome(string) {
  string = string.toLowerCase();
  var charArr = string.split('');
  var validChar = 'abcdegfhijklmnopqrstuvwxyz'.split('');
  
  var letterArr = [];
  charArr.forEach(char => {
    if (validChar.indexOf(char) > -1) letterArr.push(char); // JS will return -1 if index not found for char
  });
  
  if (letterArr.join('') === letterArr.reverse().join('')) return true;
  else return false;
  
}