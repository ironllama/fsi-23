// const urlParams = new URLSearchParams(window.location.search);
// const signInFlag = urlParams.get('signIn');

// if (signInFlag) {
//     document.querySelector(".leftMain .overlay").style.display = "none";
//     document.querySelector(".rightMain .overlay").style.display = "flex";
// }
// document.querySelector(".leftMain .overlay button").addEventListener("click", () => window.location.href = "?signIn=true")
// document.querySelector(".rightMain .overlay button").addEventListener("click", () => window.location.href = "?")

// Source: https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest
async function digestMessage(message) {
    const msgUint8 = new TextEncoder().encode(message); // encode as (utf-8) Uint8Array
    const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8); // hash the message
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // convert buffer to byte array
    const hashHex = hashArray
        .map((b) => b.toString(16).padStart(2, "0"))
        .join(""); // convert bytes to hex string
    return hashHex;
}

function toggleSignIn() {
    document.querySelector(".leftMain .overlay").classList.toggle("hidden")
    document.querySelector(".rightMain .overlay").classList.toggle("hidden")
}
document.querySelectorAll(".overlay button").forEach(b => b.addEventListener("click", toggleSignIn));

document.querySelector(".leftMain .inputForm").addEventListener("submit", async (evt) => {
    // Stop original submission. Because of the await later on, form submittion
    // will use the original pass.value instead of the await'ed one. To make it use
    // the await'ed one, we cancel this submission and manually force submission
    // at the end, after the await'ed stuff is finished.
    evt.preventDefault();

    const pass = evt.target.querySelector("#password");
    pass.value = await digestMessage(pass.value);

    evt.target.submit();  // Manual
});

document.querySelector(".rightMain .inputForm").addEventListener("submit", async (evt) => {
    evt.preventDefault();

    const pass = evt.target.querySelector("#password");
    const confirm = evt.target.querySelector("#confirm");
    if (pass.value !== confirm.value) {
        alert("Passwords do not match!");
        evt.preventDefault();
        return;
    }

    pass.value = await digestMessage(pass.value);
    confirm.value = "";
    evt.target.submit();
});
