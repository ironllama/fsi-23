const arr = [9, 8, 4, 2, 4, 5, 11, 6, 2, 4, 1, 2, 1, 3];

console.log("BEG ARR:", arr.join(", "));

// Decrement i if we changed arr, so that the end of loop i++ increments i back to the same value.
// for (let i = 0; i < arr.length; i++) {
//     if (arr[i] % 2 === 0) {
//         arr.splice(i, 1);
//         i -= 1;
//     }
// }

// // Only advance i, if the result is odd. Or, only advance i if we didn't change arr.
// for (let i = 0; i < arr.length; /* nothing here */) {
//     if (arr[i] % 2 === 0) {
//         arr.splice(i, 1);
//     }
//     else {
//         i += 1;
//     }
// }

// Go backwards through the loop (to the left), since the arr also shifts to the left after deleting one element.
for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] % 2 === 0) {
        arr.splice(i, 1);
    }
}

console.log("END ARR:", arr.join(", "));