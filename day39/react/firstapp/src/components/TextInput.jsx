import { useState } from "react"

import "./TextInput.css"

export default function TextInput({ inputSubmit }) {
    const [input, setInput] = useState("");

    const handleChange = (evt) => {
        setInput(evt.target.value);
    }

    const handleClick = () => {
        inputSubmit(input);
    }

    return (
        <div className="textInput">
            <div className="inputWrapper">
                <input
                    value={input}
                    onChange={handleChange}
                    type="text"
                    placeholder="Something"
                />
            </div>
            <button onClick={handleClick}>Submit</button>
        </div>
    )
}