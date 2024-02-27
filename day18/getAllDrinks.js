// This was a script to download the complete list of drinks. This was run with nodejs and is not something that I expect you to know, but I'm providing it, if you're curious!

const allCharacters = "0123456789abcdefghijklmnopqrstuvwxyz";
const allCharsArray = allCharacters.split("");

const fetchPromisesArray = allCharsArray.map(char => {
    return fetch("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + char)
        .then(res => res.json());
});

Promise.all(fetchPromisesArray)
    .then(allResults => {
        // allResults = allResults.drinks.flat();
        allResults = allResults.reduce((acc, v) => v.drinks ? acc.concat(v.drinks) : acc, []);

        require('fs').writeFileSync("allCocktails.json", JSON.stringify(allResults));
    });