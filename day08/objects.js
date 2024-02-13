// let one = ["Peter", 23, 34, 0.45, "brown", "brown", 70, "student"];
// let two = ["Betty", 25, 32, 0.23, "red", "green", 62, "lawyer"];
// let three = ["Reta", 32, 31, 0.5, "blond", "blue", 67, "doctor"];

const one = {
    "firstName": "Peter",  // Object properties can be enclosed in quotes. 
    age: 23,  // Or assumed.
    applicationId: 34,
    score: 0.45,
    hairColor: "brown",
    eyeColor: "brown",
    height: 70,
    occupation: "student",
    favoriteNumbers: [3, 6, 9],
    23: true,  // While not an error, it is discouraged to have numeric properties.
};  // Curly braces here are to encompass an object. Semi-colons are welcome.

if (true) {
    console.log();
}  // Curly braces here are at the end of a block. Semi-colons are not needed.

console.log("NAME:", one.firstName);  // Using a dot -- quick, convenient if you know the property while coding
console.log("AGE:", one["age"]);  // Using brackets - versatile, any string can be provided as a possible property

console.log();  // Blank line.

// const keys = [hairColor, eyeColor, height];  // Error -- you'll have to DEFINE variables hairColor, eyeColor, etc.
const keys = ["hairColor", "eyeColor", "height"];
for (const currKey of keys) {
    console.log(currKey, "-", one[currKey]);
}

console.log("KEYS:", Object.keys(one));  // While these print in "order", there is no actual order in an object.
console.log("VALS:", Object.values(one));  // While these print in "order", there is no actual order in an object.

let two = {
    type: "bird",
    // call: function randomNoise() { console.log("KAKAW!") },  // Objects can also have functions.
    call: function () { console.log("KAKAW!") },  // Function doesn't need a declared name. (Unless you want to use recursion.)
}
console.log("TWO:", two);
two.call();  // Calling a function of an object.

console.log("TWO:", Object.values(two));

one.sing = () => console.log("lalalalala");  // For brevity. Can use standard anonymous functions.
one.improveScore = () => one.score += 0.1;
console.log("ONE:", one);

let anotherOne = {
    firstName: "Paul",
    age: 28,
    applicationId: 67,
    score: 0.59,
    hairColor: "brown",
    eyeColor: "brown",
    height: 70,
    occupation: "student",
}
anotherOne.sing = () => console.log("lalalalala");  // For brevity. Can use standard anonymous functions.
anotherOne.improveScore = () => anotherOne.score += 0.1;
console.log("ANOTHER ONE:", anotherOne);

let yetAnotherOne = {
    firstName: "Mary",
    age: 26,
    applicationId: 41,
    score: 0.92,
    hairColor: "red",
    eyeColor: "green",
    height: 67,
    occupation: "student",
}
yetAnotherOne.sing = () => console.log("lalalalala");  // For brevity. Can use standard anonymous functions.
yetAnotherOne.improveScore = () => yetAnotherOne.score += 0.1;
console.log("YET ANOTHER ONE:", yetAnotherOne);

let copyOfOne = one;  // copyOfOne points at the same object as one, not a copy
copyOfOne.age = 200;
one.applicationId = 300;
console.log("COPYOFONE:", copyOfOne);
console.log("ONE:", one);


let createCopyOfOne = Object.create(one);  // Not a true copy, but a "child" or facade in front of one.
createCopyOfOne.age = 2;
console.log("CREATECOPYOFONE:", createCopyOfOne.age);
console.log("ONE:", one.age);
console.log("CREATECOPYOFONE:", createCopyOfOne);
console.log("ONE:", one);
console.log("CREATECOPYOFONE:", createCopyOfOne.applicationId);
console.log("ONE:", one.applicationId);


let assignCopyOfOne = Object.assign({}, one);  // A better copy! But a shallow copy.
assignCopyOfOne.age = 2;
console.log("ASSIGNCOPYOFONE:", assignCopyOfOne.age);
console.log("ONE:", one.age);
console.log("ASSIGNCOPYOFONE:", assignCopyOfOne);
console.log("ONE:", one);

assignCopyOfOne.favoriteNumbers.push(12);
console.log("ASSIGNCOPYOFONE:", assignCopyOfOne.favoriteNumbers);
console.log("ONE:", one.favoriteNumbers);  // one also gets changed


let spreadCopyOfOne = { ...one };  // Also a shallow copy.
spreadCopyOfOne.age = 2;
console.log("SPREADCOPYOFONE:", spreadCopyOfOne.age);
console.log("ONE:", one.age);
console.log("SPREADCOPYOFONE:", spreadCopyOfOne);
console.log("ONE:", one);

spreadCopyOfOne.favoriteNumbers.push(15);
console.log("SPREADCOPYOFONE:", spreadCopyOfOne.favoriteNumbers);
console.log("ONE:", one.favoriteNumbers);  // one also gets changed


// constructor function to make it easier to create many similar objects
function Person(inName, inAge, inAppId, inScore, newHairColor, eyeColor, height = 60, newFunc = null) {
    // Properties
    this.name = inName;
    this.age = inAge;
    this.applicationId = inAppId;
    this.score = inScore;
    this.hairColor = newHairColor;
    this.eyeColor = eyeColor;
    this.height = height;
    this.occupation = "student";

    // Methods/functions
    this.sing = () => console.log("lalalalala");  // For brevity. Can use standard anonymous functions.
    this.improveScore = () => this.score += 0.1;
    this.extraFunction = newFunc;
    this.showAppearance = function () {
        console.log(`I have ${this.hairColor} hair and ${this.eyeColor} eyes and I'm ${this.height}cm tall.`);
    }
}
let three = new Person("Charlie", 31, 89, 0.63, "black", "brown", 71);
let four = new Person("Danielle", 29, 68, 0.32, "purple", "brown");
let five = new Person("Ellie", 28, 60, 0.58, "silver", "green");

console.log("THREE:", three);
console.log("FOUR:", four);
console.log("FIVE:", five);

console.log("BEFORE THREE:", three.score);
console.log("BEFORE FOUR:", four.score);
three.improveScore();
console.log(" AFTER THREE:", three.score);
console.log(" AFTER THREE:", four.score);

three.showAppearance();
four.showAppearance();
five.showAppearance();


// Class version of above. Same thing.
class Person {
    constructor(inName, inAge, inAppId, inScore, newHairColor, eyeColor, height = 60, newFunc = null) {
        // Properties
        this.name = inName;
        this.age = inAge;
        this.applicationId = inAppId;
        this.score = inScore;
        this.hairColor = newHairColor;
        this.eyeColor = eyeColor;
        this.height = height;
        this.occupation = "student";

        this.extraFunction = newFunc;
    }

    // Methods/functions - Moved outside the constructor so that all objects would share the functions,
    // instead of having mutliple copies of the functions per object.

    sing = () => console.log("lalalalala"); // For brevity. Can use standard anonymous functions.

    improveScore = () => this.score += 0.1;

    showAppearance = function () {
        console.log(`I have ${this.hairColor} hair and ${this.eyeColor} eyes and I'm ${this.height}cm tall.`);
    };
}