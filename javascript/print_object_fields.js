
var people = {
  "jesse": {"name": "jesse", "email": "jesse@domain.com"},
  "karen": {"name": "karen", "email": "karen@domain.com"}
  
}

function print_field_values(people) {

var people_ids = Object.keys(people);
var fields = Object.keys(people[people_ids[0]]);


output = {}

for (i=0; i < fields.length; i++) {
  results = [];
  var field = fields[i];
  
  for (j=0; j < people_ids.length; j++){
    var person_id = people_ids[j];
    var person = people[person_id]; 
    
    results.push(person[field]);
  }
  output[fields[i]] = results;
}



console.log(output);

}





