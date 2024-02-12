// SPREAD
let fruit = ["apple", "orange", "lime"];
fruit.push("pomegranate");

let newFruit = fruit.concat(["watermelon"]);
console.log("NEW FRUIT:", newFruit);

newFruit = [...newFruit, "kiwi"]; // newFruit = ["apple", "orange", "lime", "kiwi"]
console.log("NEW FRUIT:", newFruit);


function somethingHappens(inArray) {
    // blah blah
}

let currArray = [1, 5, 3, 6];

// currArray.push(9);
// somethingHappens(currArray);

// somethingHappens([...currArray, 9])
somethingHappens([2, ...currArray, 9])


// DESTRUCTURING
const personArr = ["George", 23];

// const name = personArr[0];
// const age = personArr[1];

const [name, age] = personArr;  // Same as above.

const { lotsOfPeople } = require("./people.js");  // This line is not needed using html.
// lotsOfPeople.sort((a, b) => a[1] - b[1]);
lotsOfPeople.sort(([aName, aAge], [bName, bAge]) => aAge - bAge);
console.log("SORTED:", lotsOfPeople.slice(0, 10));
