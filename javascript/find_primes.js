function sieveofEratosthenes(num) {
  var primes = [];
  for (var i=0; i <= num; i++) {
    primes[i] = true;
  }
  primes[0] = false;
  primes[1] = false;
  
  for (var i=2; i <= Math.sqrt(num); i++) {
    for (var j=2; j * i <= num; j++) {
      primes[i*j] = false;
    }
  }
  
  var results = [];
  for (var i=0; i < primes.length ; i++) {
    if (primes[i]) {
      results.push(i);
    }
  }
  return results;

}

sieveofEratosthenes(20);