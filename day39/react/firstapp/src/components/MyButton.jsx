import './MyButton.css';

export default function MyButton() {
    const number = 10;

    let overunder = "equal to";
    if (number < 10) overunder = "less than";
    else if (number > 10) overunder = "more than";

    function handleClick() {
        alert('You clicked me!');
    }

    return (
        // <button onClick={() => alert('You clicked me!')} className="myButton">
        //     I'm {overunder} 10
        // </button>
        <button onClick={handleClick} className="myButton">
            I'm {overunder} 10
        </button>
    );
}