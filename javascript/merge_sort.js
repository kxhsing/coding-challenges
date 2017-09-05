function mergeSort(arr) {
  if (arr.length < 2) return arr; //base case
  
  var mid = Math.floor(arr.length/2);
  var left = arr.slice(0,mid);
  var right = arr.slice(mid);
  
  return merge(mergeSort(left), mergeSort(right));
}


function merge(arr1, arr2) {
  var result = [];
  while (arr1.length && arr2.length) {
    var minElem;
    if (arr1[0] < arr2[0]) {
      minElem = arr1.shift(); //shift pulls first element in array
    }
    else {
      minElem = arr2.shift();
    }
    result.push(minElem);
  }
  //if we run out of elements in one array:
  if (arr1.length) {
    result = result.concat(arr1);
  }
  else {
    result = result.concat(arr2);
  }
  return result;
}


mergeSort([5,6,71,29,43,21,36]);