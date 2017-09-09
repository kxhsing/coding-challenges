function print_asterisks(n) {
    if (n===0) {
    return "";
    }

    var output = "*" + print_asterisks(n-1);
    console.log(output);

    return output;
}