// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew(array, elem){
  array.push(elem);
  return array;
}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

function remove(array, elem){
// check if the item is in the array or not
  for (item of array) {
    if(item === elem) {
      array.splice(array.indexOf(elem), 1);
      return array;
    }
  }

}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(array){
  array.forEach(function(item){//anonymous functon
    console.log(item);
  });
}

// Start by asking if they want to use the web app

var start = prompt('Do you want to use the class roster app? y/n');

if (start === 'y') {
  do {
    var command = prompt('Enter a command. (add, remove, display, quit)');

    if (command === 'add'){
      roster = addNew(roster, prompt('Enter a name to add to the roster:'));
    } else if (command === 'remove'){
      roster = remove(roster, prompt('Enter a name to remove from the roster:'));
    } else if (command === 'display'){
      display(roster);
    }
  } while (command !== 'quit');
}

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
