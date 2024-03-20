# 1. Create a page that contains a text input asking for a name. If the
#     name matches one of the names of the Jetsons' family members, show
#     the family member's details on another page. If the name is not a
#     member of the family, then show an appropriate error message below
#     the text input. Use a template to show the details.
jetsons_details = {
  "george": {
    "name": "George",
    "age": 40,
    "height": 178,
    "weight": 72,
    "hair": "red",
    "occupation": "Digital Index Operator at Spacely Space Sprockets",
    "phrase": "Jane! Stop this crazy thing!",
    "pic": "https://charactersdb.com/wp-content/uploads/george-jetson.png",
  },
  "jane": {
    "name": "Jane",
    "age": 33,
    "height": 163,
    "weight": 54,
    "hair": "orange",
    "occupation": "Homemmaker",
    "phrase": "Elroy, why aren't you ready for school?",
    "pic": "https://charactersdb.com/wp-content/uploads/jane-jetson.png",
  },
  "judy": {
    "name": "Judy",
    "age": 15,
    "height": 157,
    "weight" : 48,
    "hair": "bleached blonde",
    "occupation": "Student at Orbit High School",
    "phrase": "Eeeeyuck!",
    "pic": "https://charactersdb.com/wp-content/uploads/judy-jetson.png",
  },
  "elroy": {
    "name": "Elroy",
    "age": 6,
    "height": 115,
    "weight" : 21,
    "hair": "blonde",
    "occupation": "Student at Little Dipper School",
    "phrase": "We can make money the old-fashioned way: we can borrow it.",
    "pic": "https://charactersdb.com/wp-content/uploads/elroy-jetson.png",
  },
}

# 2. Create another page that randomly displays Jetson's trivia questions.
#     All the questions are stored on the backend and only one question and
#     possible answers are displayed on the browser at a time. Users can
#     click on to guess with one of the possible answers. If it is a correct
#     answer, the UI displays another random trivia question. Make sure the
#     answer itself is never sent to the browser. Instead, each user guess is
#     validated on the backend by another endpoint to see whether or not the
#     guess is correct. Use a template to show the trivia question.
#     Source: (https://www.usefultrivia.com/tv_trivia/the_jetsons_trivia.html)
jetsons_trivia = [
  {
    "question": "In which century does The Jetsons take place?",
    "guesses": ['23RD CENTURY', '21ST CENTURY', '25TH CENTURY', '27TH CENTURY'],
    "answer": "21ST CENTURY"
  },
  {
    "question": "Where do the Jetsons live?",
    "guesses": ['GALAXY CITY', 'METEOR CITY', 'JUPITER CITY', 'ORBIT CITY'],
    "answer": "ORBIT CITY"
  },
  {
    "question": "Who is the youngest member of the Jetson family?",
    "guesses": ['ELROY', 'JUDY', 'JANE', 'GEORGE'],
    "answer": "ELROY"
  },
  {
    "question": "Where does George Jetson work?",
    "guesses": ["GAZOO'S GALACTIC GIZMOS", "COGSWELL'S COSMIC COGS", 'SPACELY SPACE SPROCKETS', 'ORBIT CITY GOLF CLUB'],
    "answer": "SPACELY SPACE SPROCKETS"
  },
  {
    "question": "What kind of pet do the Jetsons have?",
    "guesses": ['PARROT', 'DINOSAUR', 'CAT', 'DOG'],
    "answer": "DOG"
  },
  {
    "question": "What is Jane Jetson's favorite store?",
    "guesses": ['COSMIC COAT FACTORY', 'SAKS SINGULARITY', 'BIG BANG JEWELRY', 'MOONING DALES'],
    "answer": "MOONING DALES"
  },
  {
    "question": "What does George's space car transform into after he gets to work?",
    "guesses": ['WATCH', 'BRIEFCASE', 'DESK', 'SCOOTER'],
    "answer": "BRIEFCASE"
  },
  {
    "question": "What pop idol does Judy win a date with?",
    "guesses": ['BOOM-BOOM BASIL', 'JET SCREAMER', 'CONRAD BIRDIE', 'VIC FONTAINE'],
    "answer": "JET SCREAMER"
  },
  {
    "question": "What was Astro's name before he was adopted by the Jetsons?",
    "guesses": ['BALTO', 'SAGAN', 'SNUFFLES', 'TRALFAZ'],
    "answer": "TRALFAZ"
  },
  {
    "question": "What kind of robot is Rosie?",
    "guesses": ['XB-500', 'IG-88', 'TC-14', 'EV-1000'],
    "answer": "XB-500"
  },
]

# 3. We are going to now create a complete website with a new home page that
#     includes the following introduction paragraph and the two other pages
#     you've created above. A common nav bar will be used to navigate the
#     website, amongst the three pages (home, characters, trivia) and a
#     common footer will be used to list whatever else you'd like in the
#     footer of every page. Be sure to also include common CSS and any JS in
#     the common base template.
intro = """
The Jetsons is an American animated sitcom produced by Hanna-Barbera Productions. It originally aired in prime time from September 23, 1962, to March 17, 1963, on ABC, then later aired in reruns via syndication, with new episodes produced from 1985 to 1987. It was Hanna-Barbera's Space Age counterpart to The Flintstones.

While the Flintstones lived in a world which was a comical version of the Stone Age, with machines powered by birds and dinosaurs, the Jetsons live in a comical version of a century in the future, with elaborate robotic contraptions, aliens, holograms, and whimsical inventions.

The show, spanning 75 episodes over three seasons, became a beloved part of pop culture. With its vibrant animation and imaginative depiction of life in the future, the series captured the hearts of viewers young and old. The final episode aired on 12 November 1987, marking the end of an era. Even today, the theme song continues to evoke a sense of nostalgia and adventure. The theme song to the Jetsons is called “Meet the Jetsons” by Hoyt Curtin.
"""