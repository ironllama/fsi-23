const products = [
    { title: 'Cabbage', isFruit: false, id: 1 },
    { title: 'Garlic', isFruit: false, id: 2 },
    { title: 'Apple', isFruit: true, id: 3 },
];

export default function ShoppingList() {
    // First, create an array of JSX objects
    const listItems = products.map(product => (
        <li
            key={product.id} // React needs a key for items in an array
            style={{ color: product.isFruit ? 'magenta' : 'darkgreen' }}
        >
            {product.title}
        </li>
    ));

    // Just add the array to the JSX to show all the items
    return (
        <ul>{listItems}</ul>
    );
}
