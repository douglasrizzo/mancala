# Mancala Game + Agents in Python

This is a project I started after hearing about a game called mancala on [a YouTube video](https://www.youtube.com/watch?v=RdbvgP1DQN0). In the video, one of the guys mention he created an AI agent that was able to play mancala at an advanced level.

My goal is to create my own AI agents for mancala. The first one will be made through the use of Reinforcement Learning. In the future, I might tackle the challenge of creating a search-based agent.

## Modeling the environment

The main sources I used to learn about the rules of the game are [this YouTube video](https://www.youtube.com/watch?v=-A-djjimCcM) and the [Wikipedia page](https://en.wikipedia.org/wiki/Mancala) on the game.

The game I modeled is played by two players and has 2 rows of 6 holes in each, Each hole starts with 4 seeds. 2 additional holes at the right end of each row is the player's hole, where their points are kept. According to The Wiki, it looks like the games of [kalah](https://en.wikipedia.org/wiki/Kalah) or [oware](https://en.wikipedia.org/wiki/Oware).

## Rules of the game

There are many different rules to mancala. I have implemented these ones:

 * A player can only start their turn by selecting a hole on their side of the board.
 * If a player ends his stone with a point move they get an additional turn.
 * Multiple laps or relay sowing: if the last seed during sowing lands in an occupied hole, all the contents of that hole, including the last sown seed, are immediately re-sown from the hole.

An additional rule, which seems famous but I have not implemented is the one in which, if a player's sowing ends in an empty hole on their side of the board, they steal the seeds from the opponent's hole opposite to their empty hole and add to it.

The game ends when the board has no seeds in one of the player's sides.