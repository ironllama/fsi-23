// export default function ChildButton(props) {
//     const { counter, handleClick } = props;
// Same as above, without the props intermediate variable.
export default function ChildButton({ counter, handleClick }) {
    return (
        <button onClick={handleClick}>
            Clicked {counter} times
        </button>
    );
}