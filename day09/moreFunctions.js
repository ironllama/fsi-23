function addTen(num) {
    return num + 10;
}

// let newNum = addTen(4); // -> let newNum = 14;
// console.log("ADDTEN:", newNum);
console.log("ADDTEN:", addTen(4));  // -> console.log("ADDTEN:", 14);

function addFour(num) {
    console.log(num + 4);
}

// let newNum = addFour(5);  // -> let newNum = undefined
// console.log("ADDFOUR:", newNum); // -> console.log("ADDFOUR:", undefined);
console.log("ADDFOUR:", addFour(5));  // -> console.log("ADDFOUR:", undefined);

const addSix = num => console.log(num + 6);
console.log("ADDSIX:", addSix(8));  // -> console.log("ADDSIX:", undefined);

const addEight = num => { console.log(num + 8); }
console.log("ADDEIGHT:", addEight(1));  // -> console.log("ADDEIGHT:", undefined);


const addTwo = num => num + 2;
console.log("ADDTWO:", addTwo(6));  // -> console.log("ADDTWO:", 8);

const addNine = num => { num + 9; }
console.log("ADDNINE:", addNine(3));  // -> console.log("ADDNINE:", undefined);


const matingCall = () => console.log("Blah");
matingCall();

// const matingCall = () => "Blah";
// console.log("MATINGCALL:", matingCall());  // -> console.log("MATINGCALL:", "Blah");

// const matingCall = () => {
//     const call = "Blah";
//     console.log(call);
//     return call;
// }
// console.log("MATINGCALL:", matingCall());  // -> console.log("MATINGCALL:", "Blah");

// const matingCall = function () {
//     console.log("Blah");
// }
