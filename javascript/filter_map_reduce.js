//map, reduce, filter are higher order functions

var animals = [
  { name: 'Waffles', type: 'dog', age: 12 },
  { name: 'Pancake', type: 'cat', age: 14 },
  { name: 'Speculoos', type: 'dog', age: 4 },
  { name: 'Potato', type: 'dog', age: 11 },
];

function findOldDogs(pets){
    return pets.filter(function(pet){ 
        return pet.type=="dog" && pet.age > 10; 
    });
}

function findDogNames(pets) {
    return pets.filter(function(pet) {
        return pet.type=="dog";
    }).map(function(pet){
        return pet.name;
    });
}

function makeDogsSpeak(pets) {
    return pets.filter(function(pet){
        return pet.type=="dog";
    }).map(function(pet){
        return pet.name;
    }).reduce(function(greetings, name) {
        var greet = name + " says hi";
        greetings.push(greet);
        return greetings;
    }, []);

    // greetings = [];

    // for (var i=0; i < pet_names.length; i++){
    //     var greet = pet_names[i] + " says hi";
    //     greetings.push(greet);

    // }

    // return greetings;

}

