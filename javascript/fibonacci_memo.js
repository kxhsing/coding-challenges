function fibMemo(position, memo) {
  memo = memo || {};
  
  if (memo[position]) {
    return memo[position];
  }
  else {
    if (position <= 1) {
      return 1;
    }
    else {
      memo[position] = fibMemo(position-1, memo) + fibMemo(position-2, memo)
    }
  }
  return memo[position];  
}

fibMemo(0);