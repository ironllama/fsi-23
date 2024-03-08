function dec2hex(num) {
    const hexLookup = "0123456789ABCDEF";  // Possible digits
    const baseNum = 16;
    const finalHex = ["0", "0"];  // NOTE: This is least significant to most significant.

    // Process from most significant to least significant
    const posMaxDigit = Math.floor(Math.log(num) / Math.log(16));
    for (let i = posMaxDigit; i >= 0; i--) {
        const position = baseNum ** i;  // Digit position

        const digitValue = Math.floor(num / position);  // Digit multiple
        finalHex[i] = hexLookup[digitValue];

        num = num - (position * digitValue)  // Prep for next digit
    }

    // Remember to reverse finalHex to most significant to least significant!
    return finalHex.reverse().join("");
}

console.log("DF:", dec2hex(223));
console.log("57:", dec2hex(87));
console.log("0C:", dec2hex(12));
console.log("5F:", dec2hex(95));
console.log("93:", dec2hex(147));
console.log("49A87F:", dec2hex(4827263));
console.log("393B5D86991:", dec2hex(3932945934737));
console.log("35EA185424F0B:", dec2hex(948472748592907));
