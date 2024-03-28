import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import MyButton from './components/MyButton'
import Profile from './components/Profile'
import ShoppingList from './components/ShoppingList'
import CounterButton from './components/CounterButton'
import ChildButton from './components/ChildButton'
import TextInput from './components/TextInput'

function App() {
  const [parentCounter, setParentCounter] = useState(0);
  const [newInput, setNewInput] = useState("");

  const handleChildClick = () => {
    setParentCounter(parentCounter + 1);
  }

  return (
    <>
      <div>
        <MyButton></MyButton>
        <Profile></Profile>
        <ShoppingList></ShoppingList>
        <div style={{ display: "flex", gap: "0.5rem", padding: "0.5rem" }}>
          <CounterButton></CounterButton>
          <CounterButton></CounterButton>
        </div>
        <div style={{ display: "flex", gap: "0.5rem", padding: "0.5rem" }}>
          <ChildButton counter={parentCounter} handleClick={handleChildClick}></ChildButton>
          <ChildButton counter={parentCounter} handleClick={handleChildClick}></ChildButton>
        </div>
        <TextInput inputSubmit={setNewInput}></TextInput>
        <div>You submitted: [{newInput}]</div>
      </div>
    </>
  )
}

export default App
