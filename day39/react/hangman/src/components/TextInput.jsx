import { useState } from "react"

import "./TextInput.css"

export default function TextInput({ inputSubmit }) {
    const [input, setInput] = useState("");

    const handleChange = (evt) => {
        setInput(evt.target.value.at(-1) ?? '');  // Only 1 letter allowed.
    }

    const handleKey = (evt) => {
        if (evt.key === 'Enter') handleClick();
    }

    const handleClick = () => {
        inputSubmit(input);
        setInput("");
    }

    return (
        <div className="textInput">
            <div className="inputWrapper">
                <input
                    value={input}
                    onChange={handleChange}
                    onKeyDown={handleKey}
                    type="text"
                />
            </div>
            <button onClick={handleClick}>Submit</button>
        </div>
    )
}