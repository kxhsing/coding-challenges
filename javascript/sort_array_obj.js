var dogs = [
    {type: "husky", age: 10},
    {type: "corgi", age: 2},
    {type: "sheltie", age: 5},
    {type: "poodle", age: 14}
]

function sortDogsAge(dogs) {
    dogs.sort(function(a, b) { 
        return a.age - b.age; 
    });
}

function sortDogTypes(dogs) {
    dogs.sort(function(a, b) { 
        var x = a.type.toLowerCase();
        var y = b.type.toLowerCase();
        if (x < y) { return -1;}
        if (x > y) { return 1;}
        return 0;
    });
}