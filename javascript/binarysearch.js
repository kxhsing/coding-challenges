function binarySearch(numArray, key) {
  var midIdx = Math.floor(numArray.length/2);
  var midElem = numArray[midIdx];
  
  if (midElem === key) {
    return true;
  }
  
  else if (midElem < key && numArray.length > 1) {
    return binarySearch(numArray.splice(midIdx, numArray.length), key);
  }
  else if (midElem > key && numArray.length > 1) {
    return binarySearch(numArray.splice(0, midIdx), key);
  }
  else {
    return false;
  }
  
}


binarySearch([5, 7, 12, 16, 36, 39, 42, 56, 71], 56);