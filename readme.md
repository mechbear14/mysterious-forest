# 4. Mystery Forest

## Functionality

### Read config file of a forest

### Draw forest and blocks

### Place the player somewhere

### The player clicks on one block

#### If the block is not revealed, reveal it

#### If the block has been revealed, show task

##### If the player completes the task, open it

#### If the block has been opened, pass it and leave the previous block

### When the player reaches a state, end/restart game

## Architecture

Models in this game:

### Objects

#### Forest

- Contains a list of blocks, a graph representation
- resets itself
- Renders itself

#### Block

- Contains its location on map, its images and state
- resets itself
- Renders itself

#### Player

- Contains its location, its images and state
- resets itself
- Renders itself

### Components

#### Message

- Base class for other message types

#### UI

- Contains areas on screen

### Game

#### Config

- Contains player position and blocks

#### Scene

- Contains forest and player
- Reads file and construct the forest
- Handles mouse clicks and UIs
- Updates player based on blocks

#### Game

- Contains message queue and scenes
- Switch between scenes

## Public API

### Forest

- On receive

### Block

- On reveal
- On open
- On pass
- On leave
- On receive

### Player

- On move
- On walk
- On receive
