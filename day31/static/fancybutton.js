document.querySelector(".button").addEventListener("click", (e) => {
    let randomSixDigitHex = Math.floor(Math.random() * 16777215).toString(16);
    document.body.style.backgroundColor = "#" + randomSixDigitHex;
});