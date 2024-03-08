const buffSize = 80;
const buffer = Buffer.alloc(buffSize);

console.log("Enter something: ");
const buffUsed = require('fs').readSync(process.stdin.fd, buffer, 0, buffSize);

console.log("You typed:", buffer.toString('utf8', 0, buffUsed).trim());
