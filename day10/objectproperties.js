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

const ellie = new Person("Ellie", 28, 60, 0.58, "silver", "green");

// Safe way of checking if a property exists.
const hasEyeColor = Object.hasOwn(ellie, "eyeColor");
console.log("Has eyeColor:", hasEyeColor);

// Altnerate ways of checking if a property exists.
console.log("WEIGHT:", ellie.weight);
if (ellie.weight === undefined) console.log("NO WEIGHT!");
if (!ellie.weight) console.log("AGAIN, NO WEIGHT!");  // Implicit casting to boolean. (undefined == false)

console.log("ALL PROPS:", Object.keys(ellie));
console.log("WEIGHT?", Object.keys(ellie).includes("weight"))

console.log("ALL VALUES:", Object.values(ellie));

console.log("ALL PROPS:VALS:", Object.entries(ellie));

// const bob = ["Robert", 33, "Electrician"];
// const [name, age] = bob;  // Array destructuring.
// console.log(`This is ${name}, who is ${age} years old.`);

const { name: firstName, age, eyeColor } = ellie;
// Above is same as:
// const firstName = ellie.name;
// const age = ellie.age;
// const eyeColor = ellie.eyeColor;

console.log(`This is ${firstName}, who is ${age} years old.`);
