import Box from "./Box";

import './WordBoxes.css';

export default function WordBoxes({ word, lettersGuessed }) {
    const allBoxes = word.map((letter, i) =>
        // <Box key={`box-${i}`} letter={letter} />
        <Box key={`box-${i}`} letter={lettersGuessed.includes(letter) ? letter : ""} />
    );

    return (
        <div className="allBoxes">
            {allBoxes}
        </div>
    );
}