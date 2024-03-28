import { useState } from 'react'
import WordBoxes from './components/WordBoxes';

import './App.css'
import TextInput from './components/TextInput';

const allWords = ["confused", "pleasant", "unused", "null", "female", "reject", "steam", "interrupt", "holiday", "tiger", "coast", "wind", "equable", "encouraging", "recognise", "detailed", "wood", "pat", "trade", "giant", "recognise", "egg", "inexpensive", "eyes", "organic", "cheer", "strong", "toys", "troubled", "sparkling", "wind", "wicked", "eager", "poised", "film", "milky", "enjoy", "unsuitable", "parched", "chilly", "difficult", "dependent", "soap", "babies", "motion", "color", "observant", "love", "fall", "sprout", "sparkling", "correct", "charming", "left", "wind", "flesh", "stem", "well-made", "intelligent", "plug"];

function App() {
  const [word, setWord] = useState(getNewWord());
  const [guesses, setGuesses] = useState("");
  const [numWrong, setNumWrong] = useState(0);
  const [gameState, setGameState] = useState(0);  // 1 for Win, 2 for Loss

  // console.log("WORD:", word);

  // Randomly select a word from the large array of words.
  function getNewWord() {
    return allWords[Math.floor(Math.random() * allWords.length)].split("")
  }

  const handleGuess = (letter) => {
    if (gameState == 0) {  // Make sure we are not in a Win or Lose state
      if (!guesses.includes(letter)) {  // If this is a new letter, not yet guessed
        const newGuesses = guesses + letter;  // We need to create a new var for state
        setGuesses(newGuesses);

        // Check if user guessed all the letters correctly
        let allFound = true;
        for (let i = 0; i < word.length; i++) {
          if (!newGuesses.includes(word[i])) {
            allFound = false;
            break;
          }
        }
        if (allFound) setGameState(1);

        if (!word.includes(letter)) {  // If the letter is not in the word
          const newWrong = numWrong + 1;
          setNumWrong(newWrong);

          if (newWrong === 5) setGameState(2);  // If too many wrong, Lose game
        }
      }
    }
  }

  // Reset game states to play again
  const resetGame = () => {
    setWord(getNewWord());
    setGuesses("");
    setNumWrong(0);
    setGameState(0);
  }

  // Determine if we show the end of game message and if so, what to show.
  let gameStateElem = null;
  if (gameState == 1) {
    gameStateElem = (
      <div className='gameState'>
        'You win!'
        <button onClick={resetGame}>Reset</button>
      </div>
    )
  } else if (gameState == 2) {
    gameStateElem = (
      <div className='gameState'>
        'You lose!'
        <button onClick={resetGame}>Reset</button>
      </div>
    )
  }

  return (
    <div className='game'>
      {gameStateElem}
      <WordBoxes word={word} lettersGuessed={guesses}></WordBoxes>
      <div className='guesses'>
        <span className='title'>Guesses:</span>
        {guesses.split("").join(", ")}
      </div>
      <div className='bottom'>
        <div className='wrong'>
          <div className='title'>Wrong:</div>
          {numWrong}
        </div>
        <TextInput inputSubmit={handleGuess}></TextInput>
      </div>
    </div>
  )
}

export default App
