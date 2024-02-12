// 1. Using the array.map function, add 100 to each of the following items in the array:
const lotsOfNumbers = [7, 46, 99, 32, 15, 46, 23, 47, 15, 82, 17, 83, 97, 95, 97, 31, 16, 96];
const numPlus10 = lotsOfNumbers.map(v => v + 100);

// 1b. Print out the array in descending order.
function mySortFunc(a, b) { return a - b; }
numPlus10
    .sort(mySortFunc)
    .reverse();

console.log("SORTED, REVERSED:", numPlus10);


// 2. Using the lotsOfPeople array, generate a new array that contains a true or false for each item, depending on whether the person is under 21. And then print the number of people under 21, using this array of boolean values.
// For example, this portion:
// [
//     ["Edythe", 49],
//     ["Arthur", 76],
//     ["Irwin", 12],
//     ["Mylene", 19],
//     ["Nicolette", 61],
// ]
// Would turn into this portion:
// [
//     false,
//     false,
//     true,
//     true,
//     false,
// ]
// And there are 2 items that are true, so 2 people under 21.

const { lotsOfPeople } = require("./people");
const under21 = lotsOfPeople
    .map(p => p[1] < 21)
    .filter(u21 => u21)
    .length;

console.log("UNDER 21:", under21);


// 3. Using the array.map function, convert the following table of F temperatures into C:
const mayTemps = [
    [86, 78, 85, 79, 86, 78, 80],
    [84, 82, 74, 85, 83, 82, 79],
    [76, 79, 80, 81, 82, 81, 78],
    [77, 79, 83, 84, 85, 80, 78],
    [83, 81, 78]
];

// C = (F-32)/(5/9)
function toCelsius(fahr) {
    // return Math.round((fahr - 32) / (9 / 5));
    // return ((fahr - 32) / (9 / 5)).toFixed(1);
    return (Math.round(((fahr - 32) / (9 / 5)) * 10)) / 10;
}

mayTemps.forEach(week => {
    week.forEach((day, di) => {
        let c = toCelsius(day);
        if (c % 1 == 0) c = c + ".0";  // Just to get the extra *.0 on the whole numbers.
        week[di] = c;  // Assignment back to week, since days are retreived by value.
    })
});

console.log("3. Celsius temps");  // These are the expected values/ouput.
console.log(`['30.0', '25.6', '29.4', '26.1', '30.0', '25.6', '26.7']
['28.9', '27.8', '23.3', '29.4', '28.3', '27.8', '26.1']
['24.4', '26.1', '26.7', '27.2', '27.8', '27.2', '25.6']
['25.0', '26.1', '28.3', '28.9', '29.4', '26.7', '25.6']
['28.3', '27.2', '25.6']`);

console.log(mayTemps.forEach(week => {
    let output = "["
    week.forEach(day => output += `'${day}', `);
    const outputArr = output.split("");
    outputArr.splice(output.length - 2, 2, "]");
    console.log(outputArr.join(""));
}));  // Print out your results, here.
