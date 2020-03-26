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

Objects in this model:

### Forest

- Contains a list of blocks, a graph representation
- resets itself
- Renders itself

### Block

- Contains its location on map, its images and state
- resets itself
- Renders itself

### Player

- Contains its location, its images and state
- resets itself
- Renders itself

### Game

- Contains message queue
- Reads file and construct the forest
- Handles mouse clicks and UIs
- Updates player based on blocks

### UI

- Contains areas on screen

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
