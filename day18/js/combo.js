let allMatches = [];

let inputElem;
let matchesElem;
let searchButton;
let searchCallback;

function createCombo(parentElement, listOfMatches, inCallback) {
    const comboHtml = `
        <div id="combo">
            <input tabindex="1" type="text" placeholder="Enter the name of a university...">
            <div id="matches"></div>
            <button tabindex="2">Search</button>
        </div>
    `;
    parentElement.innerHTML = comboHtml;

    // Store the incoming listOfMatches as allMatches to use in combo.js
    allMatches = listOfMatches;

    // Attach the new elements to the combo.js "global" variable references
    inputElem = parentElement.querySelector("input");
    matchesElem = parentElement.querySelector("#matches");
    searchButton = parentElement.querySelector("button");

    // Create a combo input box - a text input (ie. the HTML input above) that will display all the school names that match your text in a separate area under the text input (ie. the "matches" HTML element above), using simple string matching rules. To keep it fast, but useful, make sure the user types in at least a few characters before suggesting matches. (eg. 3 characters minimum).
    inputElem.addEventListener("input", function (event) {
        if (inputElem.value.length >= 3) {
            const inputName = inputElem.value.toLowerCase();
            const matchingItems = allMatches.filter(match => match.toLowerCase().includes(inputName));

            // Create a string to accumulate the new HTML to insert.
            let matchingItemsHtml = "";
            matchingItems.forEach((match, im) => matchingItemsHtml += `<div tabindex="${im + 3}">${match}</div>`);
            matchesElem.innerHTML = matchingItemsHtml;
            matchesElem.style.display = "block";

            // Add an event listener to all the newly created and added matches. (All the divs added.)
            const allNewElems = matchesElem.querySelectorAll("div");
            allNewElems.forEach(match => match.addEventListener("click", matchToInput));
        }
    });

    // For input box, handle the Enter key and Down Arrow
    inputElem.addEventListener("keyup", function (event) {
        if (inputElem.value.length >= 3) {
            if (event.key === "Enter") {
                doSearch();
            }
            else if (event.key === "ArrowDown") {
                matchesElem.querySelector("div").focus();
                event.preventDefault();
            }
        }
    });

    // Handle arrow keys used in matches list
    matchesElem.addEventListener("keyup", function (event) {
        if (["ArrowDown", "ArrowUp"].includes(event.key)) {
            // Get the current matching item in focus and extract the tab index.
            const currElem = matchesElem.querySelector("div:focus");
            const currTabIndex = currElem.tabIndex;

            // Normally add one, except on up arrow, we subtract one.
            let nextIdx = 1;
            if (event.key === "ArrowUp") nextIdx = -1;

            // Focus the next element.
            const nextElem = matchesElem.querySelector(`div[tabindex="${currTabIndex + nextIdx}"]`);
            if (nextElem) nextElem.focus();

            // event.preventDefault();  // Try to prevent scrolling. Might not be effective.
        }
        else if (event.key === "Enter") {
            matchToInput(event);
        }
    });

    // When the Search button is pushed...
    searchButton.addEventListener("click", doSearch);

    // Assign the "global" function variable reference for when the search is complete.
    searchCallback = inCallback;
}

// Shared function for when any matching school in the matching school list is clicked.
function matchToInput(event) {
    if (inputElem && matchesElem) {
        inputElem.value = event.target.innerHTML;  // Get the text of the matching school.
        inputElem.focus();  // Focus on it (useful if allowing use of 'Enter' key).
        matchesElem.style.display = "none";  // Hide the matches.
    }
}

function doSearch() {
    if (inputElem) {
        const inputName = inputElem.value.toLowerCase();
        // Using find, since we only need to find one (first) match.
        const resultMatch = allMatches.find(match => match.toLowerCase() === inputName);
        if (searchCallback) {
            searchCallback(resultMatch);
        }
    }
}