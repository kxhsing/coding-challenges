function compressString(my_str) {
    var dict = {}; //create object of lists
    var order = [];

    for (var i=0; i < my_str.length; i++) {
        if (my_str[i] in dict) {

            if (my_str[i]!= order.slice(-1)) {
                dict[my_str[i]].push(1);
            }
            else {
                counts = dict[my_str[i]];
                counts[counts.length-1] += 1;
            } 
        }
        else {
            dict[my_str[i]]=[1];
            } 

        if (my_str[i]!= order.slice(-1)[0]) {
            order.push(my_str[i]);
        }
    }
    // console.log(order);
    // console.log(dict);

    var output = "";

    for (var j=0; j < order.length; j++) {
        var currCount = dict[order[j]].slice(0,1)[0];
        var checkCounts = dict[order[j]];
        var nextOutput = order[j] += currCount.toString();
        output += nextOutput;
        checkCounts.splice(0,1);

    }

    return my_str.length < output.length ? my_str : output
}