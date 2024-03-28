import { useState } from "react";

export default function CounterButton() {
    const [counter, setCounter] = useState(0);
    // let counter = 0;

    function handleClick() {
        // counter += 1;
        setCounter(counter + 1);
        console.log("CounterButton: handleClick: counter:", counter);
    }

    // return <button onClick={handleClick}> Clicked {counter} times </button>;
    // Above works, but is ugly, so we split it into separate lines.
    // Remember the parenthesis to prevent JS from automatically inserting a semicolon.
    return (
        <button onClick={handleClick}>
            Clicked {counter} times
        </button>
    );
}