# Discord bot specification

## Discord Channels

Only Eagle-6 can write in any channels, players can only react to messages

- Nest - channel for all-game announcements
- _Falcon / Hawk_ HQ - for team specific messages

## Actions

### Starting game

Cued by Initiator via text specifiing the discord server it should run on.
A message is sent to the Nest channel, players are asked to react to the message with emotes representing teams (or a random team??)
Closed by Initiator by a text, then the game starts.

Players will be assigned roles based on the team they are in.

### Generating codewords

The codenames for each team are sent to respective channel and pinned

### Generating codes

Generated code is sent to the encryptor via DM (with codenames), then they send back a list of clues in a single message
```
1. [Clue 1]
2. [Clue 2]
3. [Clue 3]
```

### Gathering Submissions

Clues are forwarded to Nest channel.
Players are allowed to send submissions in DMs, which are forwarded to respective team channel.
Players vote on submissions by reacting to the messages and when any of them gets votes from the whole team, they are locked in and a message about it is send to Nest.
When both teams lock in submissions, the round wraps.

### Round wrap

Round is evaluated, information about the result of last round is provided as well as current state of tokens.
Winners are announced and game ends, if applicable

### Clean up

Users have their roles removed, chats are emptied. (Channels are removed ??)
