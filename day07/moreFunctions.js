function doSomething() {
    // Something
}
doSomething();

(function () {
    // Something
})();
// IIFE - Immediately Invoked Function Expression

const doSomethingElse = function () {
    // Something else
}
// Named Function Expression or Named Anonmymous Function
doSomethingElse();

const doSomethingDifferent = () => {
    // Something different
}
// Arrow function

const addTen = num => num + 10;
console.log("ADD TEN:", addTen(2));



// Using standard function declaration.
// document.querySelector(".box").addEventListener("click", boxClicked);
// function boxClicked() {  // Seems to be defined AFTER it is used, but it is HOISTED automatically by JS.
//     console.log("BOOM!");
// }

// // Using an anonymous function.
// document.querySelector(".box").addEventListener("click", function () {
//     console.log("BOOM!");
// });

// Using an arrow function.
// document.querySelector(".box").addEventListener("click", () => console.log("BOOM!"));

const boxClicked = () => console.log("BOOM!");
document.querySelector(".box").addEventListener("click", boxClicked);
// const boxClicked = () => console.log("BOOM!");  // Can't defined this AFTER using, must be defined BEFORE.


let numArray = [5, 3, 7, 1, 8];
function multiplyBy(inArray, inMult) {
    let returnArray = [];

    for (let i = 0; i < inArray.length; i++) {
        returnArray.push(inArray[i] * inMult);
    }

    return returnArray;
}
console.log("MULT ARRAY:", numArray, "*", 3, multiplyBy(numArray, 3));

// Same as above.
// function multiplyElement(item) {
//     return item * 3;
// }
// let newArray = numArray.map(multiplyElement);
// let newArray = numArray.map(function (item) { return item * 3});
// let newArray = numArray.map(item => {
//     return item * 3;
// });
let newArray = numArray.map(item => item * 3);  // Same above, with assumed return and no block (single expression)
console.log("MULT ARRAY:", numArray, "*", 3, newArray);
// map always creates a new array with the same number of elements as the original array

// numArray.forEach(element => console.log(element * 5));
// numArray.forEach((item, idx) => {  // Foreach does not require a return, since foreach does not return anything.
//     console.log(`${idx}: value: ${item}`);
// });
numArray.forEach((item, idx) => console.log(`${idx}: value: ${item}`));  // No block, assumed return

// console.log("TOTAL:", numArray.reduce((acc, val) => {
//     console.log("ADDING:", val, "TO ACC", acc);
//     return acc + val;
// }, 0));
// console.log("TOTAL:", numArray.reduce((acc, val) => acc + val, 0));  // No block, assumed return
console.log("TOTAL:", numArray.reduce((total, number) => total + number, 0));  // No block, assumed return
