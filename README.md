# Project Valerie

## Design
The entire project's design is laid out in [Evernote](https://www.evernote.com/shard/s508/nl/192803964/3275716d-2238-3837-0a49-f8b1b701f130?title=Project%20Valerie)

## Outline
Using GPT-3 to create a general purpose digital extension that can make decisions, execute processes, and retain information.

This project aims to create a characterization with the AI, which I’ve chosen to name Valerie. My vision for Valerie is that of a being that can experience, form opinions, make decisions, and have memories. They should take on a personality as they take in more of the world. Everything they are exposed to should inform their characterization. That means chatting with people on the web, actions they take, memories, decisions they’ve made in the past.

Some components  I might  include in the project:
- A python backend running on surfstation connected to a user interface via WebSocket
- An email account
- Access to the daily news
- Access to a few different select APIs


## Conventions
Every program I write is more elegant than the last.
With this project I'm going to make heavy use of the following paradigms and conventions:
 - static typing
 - constants
 - f-strings
 - error handling as program flow
 - readability
 - simplicity
 - maintainability
 

 I'm tired of opening up an old project and having no idea what anything does, I'm going to place a lot of emphasis on minimizing that annoyance with this project

 I'm also going to use a more elaborate debugging system, where a single constant defines which commentary should be printed

 ### Static Typing
  - most functions should have the  parameter and return objeects' data type hinted at