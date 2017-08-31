# Pyroch
Simple program which navigates a robot on a grid, taking parameter to modify the outcome.

## Running it
```bash
python entry.php [args...]
```
*Example*
```bash
python entry.php --size-x 10 --size-y 10 --sequence fflff
```
Refer to command list further down the page for more details.
## Running tests
_Before running tests. Makes sure to install nose test runner_
```bash
pip install nose
```
After that you can run tests with
```bash
nosetests tests
```
### Objective/Case tests
_There is a specifc test file used to cover specific sequences and configurations in a fast manner_
```bash
nosetests tests/cases_test.py
```
Which covers the following objectives:

#### Objective 1
100x100 grid,
Robot starts at 0,0 facing SOUTH,
Commands given are fflff,
Robot should end at 2,2

#### Objective 2
50x50 grid,
Robot starts at 1,1 facing NORTH,
Commands given are fflff,
Robot should end at 1,0

#### Objective 3
100x100 grid,
Robot starts at 50,50 facing NORTH,
Commands given are fflffrbb,
Robot should end at 1,0

## Commands
### -h, --help
Shows help and list of commands
### --size-x, -zx
Sets the size for grid on x-axis
```bash
--start-x 10
```
Will result in a grid 10 squares on the x-axis
### --size-y, -zy
Sets the size for grid on y-axis
```bash
--start-y 10
```
Will result in a grid 10 squares on the y-axis
### --start-x, -sx
Sets the start position for robot on x-axis
```bash
--start-x 5
```
Will result the robot starting coordinate 5 on x-axis
### --start-y, -sy
Sets the start position for robot on x-axis

```bash
--start-y 5
```
Will result the robot starting coordinate 5 on y-axis
### --sequence, -s
Inputs a sequence to run through robot
Possible values are f(forward), b(backwards), l(left), r(right)
```bash
--sequence fflff
```
Will result in the robot moving forward, forward, turning left, forward, forward
### --start-facing, -sf
Sets the initial facing of robot.
```bash
--start-facing NORTH
```
Will result in the robot facing north when starting it's sequence.
### --obstacles, -o
Adding one or more obstacles by providing x and y axis positions
```bash
--obstacles 0,0 3,10
```
Will create obstacles in the passed coordinates on the map
