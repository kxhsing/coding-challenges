function meanMedianMode(array) {
  return {
    mean: getMean(array),
    median: getMedian(array),
    mode: getMode(array)
  }
}

function getMean(array) {
  var sum = 0;
  array.forEach(num => {sum +=num});
  
  var mean = sum/(array.length);
  
  return mean
}

function getMedian(array) {
  array.sort(function(a,b) {
    return a-b;
  });
  
  var median;
  if (array.length%2!==0) {
    median = array[Math.floor(array.length/2)]; 
  }
  else {
    var mid1 = array[(array.length/2)-1];
    var mid2 = array[(array.length/2)];
    median = (mid1 + mid2) / 2;
  }
  return median;
}


function getMode(array) {
  var counts = {};
  array.forEach(num => {
    if (!counts[num]) {
      counts[num] = 0;
    }
      counts[num] ++;
  });
  
  var maxFreq = 0;
  var modes = [];
  for (var num in counts) {
    if (counts[num] > maxFreq) {
      modes = [num];
      maxFreq = counts[num];
    }
    else if (counts[num] === maxFreq) {
      modes.push(num);
    }
    
  }
  if (modes.length === Object.keys(counts).length) {
    modes = [];
    
  }
  return modes;
  
}

// meanMedianMode([9,10,23,10,23,9]);
meanMedianMode([1,2,3,4,5,6,7,8,9,1]);






