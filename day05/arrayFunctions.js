// let one = new Array(4);
// one.fill("");

let rememberStr = "Remember";
let rememberArr = rememberStr.split("");
rememberArr = Array.from(rememberStr);

console.log("Array.isArray:", Array.isArray(rememberArr));

rememberArr[1];
rememberArr.at(1);
rememberArr.at(-1);  // "r"
rememberArr.at(-2);  // "e"

// Is there a z, and at what position is it at?
let stuff = "olsndovn90aw8enfoinavoweifoqa29i3fokanwelfna032hbo1non32ogihw0r8vqn92i3f;lkaw'rgkhap9uo24nfqj3nfoiaj0werhfaojwjenf;lqj2a380rhfoa;wnef08ahq23oijkna;lwkndf;kabdafgklab;ldfkjqo3iru[oq;rhg;lakkwberfqjef";
// let pos = -1;  // Gonna track the index, if the letter is found.
// for (let i = 0; i < stuff.length; i++) {
//     let currLetter = stuff[i];
//     if (currLetter === 'z') {
//         pos = i;
//         break;
//     }
// }
// console.log("FOUND AT: ", pos);

// console.log("F:", stuff.indexOf("f"));
// console.log("Z:", stuff.indexOf("z"));
if (stuff.indexOf("f") !== -1) console.log("There is an f in stuff!");
if (stuff.indexOf("z") === -1) console.log("There is no z in stuff!");

// let one = [];
// one[0] = "red";
// one[1] = "blue";
// one[3] = "pink";

// console.log("ONE:", one);

// for (let i = 0; i < one.length; i++) {
//     console.log("ONE:", one[i]);
// }

let fruit = ["apple", "banana", "cherry", "durian"];
console.log("Original fruit basket:", fruit);

// Only at the end.
fruit.push("eggplant");  // Returns new length of the array, remember to assign if that's useful to you.
let lastItem = fruit.pop();  // Remember to assign to a variable, if you want to use the element that was removed.

// Only at the beginning.
fruit.unshift("zucchini");  // Adds to the beginning of an array. Returns new length of the array.
let firstItem = fruit.shift();  // Removes the first item of the array. Remember to assign, if it's important to you.

// Remove an item from an arbitrary position in the array.
fruit.splice(2, 1); // Removes the cherry.
console.log("After removing cherry:", fruit);
fruit.splice(1, 1, "grape", "orange");
console.log("After removing banana and adding grape and orange:", fruit);

// Create a copy of a portion of an array.
let firstFruits = fruit.slice(1, 2);  // Pulls out only one fruit -- last index is non-inclusive.
let lastFruits = fruit.slice(2);
let copyFruits = fruit.slice();

// Merge to arrays into a larger array.
let left = [3, 2, 6];
let right = [9, 1, 3];
let combo = left.concat(right);
console.log("COMBO:", combo);
let addCombo = left + right;
console.log("ADDCOMBO:", combo);

let words = ["blue", "berry", "pie"];
let wordStr = words.join("");
console.log("WORDSTR:", wordStr);
wordStr = words.join(",");
console.log("WORDSTR:", wordStr);
