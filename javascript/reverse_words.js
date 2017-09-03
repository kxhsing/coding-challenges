function reverseWords(str) {
  var wordArr = str.split(" ");
  var output = [];

  wordArr.forEach(word => {
    var reversedWord = '';
    for (var j = word.length-1; j >= 0; j--) { 
      reversedWord += word[j];
    }

    output.push(reversedWord);
    
  });
  
  
  return output.join(' ');
}

reverseWords("hello There world");




  // for (var i=0; i < wordArr.length; i++) {
  //   var currWordLetters = wordArr[i].split('');
  //   var reversedWord = "";
    
  //   for (var j = currWordLetters.length-1; j >= 0; j--) {
  //     reversedWord += currWordLetters[j];
  //   }
  //   output.push(reversedWord);
  // }