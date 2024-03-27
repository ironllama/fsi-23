DROP TABLE IF EXISTS ChatMessages;

CREATE TABLE ChatMessages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    message TEXT,
    created_date DATETIME
);

INSERT INTO ChatMessages (username, message, created_date) VALUES
("Alice", "Hey, how are you?", NOW() - INTERVAL 1 DAY),
("Bob", "I'm good, thanks! How about you?", NOW() - INTERVAL 1 DAY - INTERVAL 2 HOUR),
("Alice", "I'm doing alright, just busy with work.", NOW() - INTERVAL 1 DAY - INTERVAL 1 HOUR),
("Carrie", "What's everyone up to?", NOW() - INTERVAL 2 DAY),
("Daniel", "Just finished watching a movie.", NOW() - INTERVAL 2 DAY - INTERVAL 3 HOUR),
("Carrie", "Nice! Which movie did you watch?", NOW() - INTERVAL 2 DAY - INTERVAL 2 HOUR),
("Esther", "Hey guys, what's going on?", NOW() - INTERVAL 3 DAY),
("Frank", "I'm studying for an exam.", NOW() - INTERVAL 3 DAY - INTERVAL 4 HOUR),
("Esther", "Good luck with that!", NOW() - INTERVAL 3 DAY - INTERVAL 3 HOUR),
("Heather", "I'm so excited for the weekend!", NOW() - INTERVAL 4 DAY - INTERVAL 10 MINUTE),
("Iggy", "Me too! Any plans?", NOW() - INTERVAL 4 DAY - INTERVAL 5 HOUR),
("Jessica", "I'm going hiking with some friends.", NOW() - INTERVAL 4 DAY - INTERVAL 4 HOUR),
("Kevin", "Just got back from a road trip.", NOW() - INTERVAL 5 DAY),
("Kevin", "How was it?", NOW() - INTERVAL 5 DAY - INTERVAL 3 HOUR),
("Kevin", "Amazing! Saw some breathtaking views.", NOW() - INTERVAL 5 DAY - INTERVAL 2 HOUR),
("Heather", "I'm so excited for the concert next week!", NOW() - INTERVAL 6 DAY),
("Iggy", "Yeah, it's going to be awesome!", NOW() - INTERVAL 6 DAY - INTERVAL 3 HOUR),
("Jessica", "I can't wait to see my favorite band.", NOW() - INTERVAL 6 DAY - INTERVAL 2 HOUR),
("Frank", "I need help with this math problem.", NOW() - INTERVAL 7 DAY),
("Esther", "Sure, let me take a look.", NOW() - INTERVAL 7 DAY - INTERVAL 1 HOUR),
("Frank", "Thanks, I appreciate it.", NOW() - INTERVAL 7 DAY - INTERVAL 30 MINUTE),
("Daniel", "What's everyone up to?", NOW() - INTERVAL 1 DAY),
("Carrie", "Just finished cooking dinner.", NOW() - INTERVAL 1 DAY - INTERVAL 2 HOUR),
("Daniel", "I made spaghetti with meatballs.", NOW() - INTERVAL 1 DAY - INTERVAL 1 HOUR),
("Bob", "I'm feeling tired today.", NOW() - INTERVAL 2 DAY),
("Alice", "Make sure to get enough rest.", NOW() - INTERVAL 2 DAY - INTERVAL 1 HOUR),
("Bob", "Thanks for the reminder.", NOW() - INTERVAL 2 DAY - INTERVAL 30 MINUTE),
("Jessica", "I'm thinking of redecorating my room.", NOW() - INTERVAL 3 DAY),
("Iggy", "That sounds like a fun project!", NOW() - INTERVAL 3 DAY - INTERVAL 1 HOUR),
("Jessica", "I'm excited to try out some new ideas.", NOW() - INTERVAL 3 DAY - INTERVAL 30 MINUTE),
("Heather", "I just finished reading a great book.", NOW() - INTERVAL 4 DAY),
("Frank", "What book was it?", NOW() - INTERVAL 4 DAY - INTERVAL 2 HOUR),
("Heather", "It was ""The Alchemist"" by Paulo Coelho.", NOW() - INTERVAL 4 DAY - INTERVAL 1 HOUR),
("Carrie", "I'm feeling stressed lately.", NOW() - INTERVAL 5 DAY),
("Bob", "Try taking some deep breaths to relax.", NOW() - INTERVAL 5 DAY - INTERVAL 3 HOUR),
("Carrie", "Thanks, I'll give that a try.", NOW() - INTERVAL 5 DAY - INTERVAL 2 HOUR),
("Alice", "I just finished a workout and I feel great.", NOW() - INTERVAL 6 DAY),
("Kevin", "Exercise is such a mood booster.", NOW() - INTERVAL 6 DAY - INTERVAL 1 HOUR),
("Alice", "I try to make it a daily habit.", NOW() - INTERVAL 6 DAY - INTERVAL 30 MINUTE),
("Esther", "I'm craving pizza right now.", NOW() - INTERVAL 7 DAY),
("Daniel", "Let's order some together!", NOW() - INTERVAL 7 DAY - INTERVAL 1 HOUR),
("Esther", "That sounds like a plan.", NOW() - INTERVAL 7 DAY - INTERVAL 30 MINUTE);

-- Make sure we have some messages today by manually changing messages from 7 days ago to today.
-- UPDATE chatmessages SET created_date=(created_date + INTERVAL 7 DAY) WHERE DATE(created_date)=(CURDATE() - INTERVAL 7 DAY);
UPDATE chatmessages SET created_date=(created_date + INTERVAL 7 DAY) WHERE created_date <= (CURDATE() - INTERVAL 6 DAY);
