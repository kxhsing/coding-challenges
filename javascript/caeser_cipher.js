function caesarCipher (str, num) {
  num = num % 26;
  
  var lowerCaseStr = str.toLowerCase();
  var alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
  var newStr = '';
  
  for (var i=0; i < lowerCaseStr.length; i++) {
    var currLetter = lowerCaseStr[i];
    if (currLetter === ' ') {
      newStr += currLetter;
      continue;
    }
    var currIndex = alphabet.indexOf(currLetter);
    var newIndex = currIndex + num;
    if (newIndex > 25) { newIndex = newIndex - 26; }
    if (newIndex < 0 ) {newIndex = 26 + newIndex;}
    if (str[i] === str[i].toUpperCase()) {
      newStr += alphabet[newIndex].toUpperCase();
    }
    else {
      newStr += alphabet[newIndex];
    }
    
  }
  return newStr;
  
}

caesarCipher('Zoo Keeper', 2);
caesarCipher('Big Car', -16);
caesarCipher('Javascript', -900);