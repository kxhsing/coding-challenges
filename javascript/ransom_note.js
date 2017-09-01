function harmlessRansomNote (noteText, magazineText) {
  var words = {};
  var magWords = magazineText.split(" ");
  var noteWords = noteText.split(" ");
  
  for (var i=0; i < magWords.length; i++) {
    if (magWords[i] in words) {
      words[magWords[i]] ++;
    }
    else {
      words[magWords[i]] = 1;
    }
  }
  
  var notePossible = true;
  
  for (var j=0; j < noteWords.length; j++) {
    if (noteWords[j] in words) {
        words[noteWords[j]]--;
        if (words[noteWords[j]] < 0) {
          notePossible = false;
      }
    }
    else {
      notePossible = false;
    }
  }
  
  return notePossible;
  
  
  // console.log(words);
    
}

harmlessRansomNote('hello hey', 'hello there world hey');


