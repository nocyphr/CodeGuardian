- [CodeGuardian](#codeguardian)
- [What do i want?](#what-do-i-want)
- [ToDo](#todo)
- [How to run tests](#how-to-run-tests)
  - [BDD tests](#bdd-tests)
  - [unittests](#unittests)
  - [Criteria to check for](#criteria-to-check-for)
    - [Keep all entities small](#keep-all-entities-small)
    - [cyclomatic complexity](#cyclomatic-complexity)
      - [Step 1](#step-1)
      - [Step 2](#step-2)
      - [Step 3](#step-3)
      - [Step 4](#step-4)
- [What should be the outcome?](#what-should-be-the-outcome)
  - [Detailed report (v1)](#detailed-report-v1)
    - [Examples (v1)](#examples-v1)
    - [config](#config)
  - [Global report(v1)](#global-reportv1)
  - [Detailed report (v2)](#detailed-report-v2)
  - [Detailed report (v3)](#detailed-report-v3)


# CodeGuardian
The next generation of ai assisted agent based code reviews

# What do i want?

In order to have fast code reviews
As a Developer
I want an AI that analyzes my code from different quality perspectives and provides suggestions for improvements


# ToDo
- Feature: create report showing cyclomatic complexity for a single file input
  - write unit-test for function counting lines, then make it pass, should return len of findall - regex: ^(?!\s*$)(?!\s*#).+


# How to run tests
## BDD tests
1. activate venv `source venv/bin/activate`
2. run behave `behave ara/features`

## unittests
1. run pytest `pytest`
2. for test-coverage run `pytest --cov --cov-report term-missing`

## Criteria to check for
- Keep All Entities Small
- Don’t Abbreviate
- One Dot per Line
- Only One Level of Indentation per Method/function
- Don’t Use the `else` Keyword

---

- **CQRS (Command Query Responsibility Segregation)**
This pattern separates reading data (query) from modifying data (command)
- **Single Responsibility Principle**
A class should have only one reason to change, meaning it should only have one job or responsibility.
- **Open/Closed Principle**
Software entities should be open for extension but closed for modification. This means you should be able to add new features without changing existing code.
- **Liskov Substitution Principle**
Objects of a superclass should be replaceable with objects of subclasses without affecting the correctness of the program.
- **Interface Segregation Principle**
Clients should not be forced to depend on interfaces they do not use. 
- **Dependency Inversion Principle**
High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **DRY (Don't Repeat Yourself)**

--- 

- **Long Method**
A method that has grown too large and tries to do too much, making it hard to understand.
- **Large Class**
A class that has too many lines of code and responsibilities, which makes it complex and difficult to maintain.
- **Primitive Obsession**
Using primitive data types to represent complex concepts, instead of creating specific classes.
- **Long Parameter List**
Methods that have too many parameters, which can make them challenging to understand and use.
- **Data Clumps**
Groups of data that are often used together but not structured into a class or object.
- **Feature Envy**
A method that seems more interested in a class other than the one it actually is in.
- **Divergent Change**
When making a single change requires modifying many different classes.
- **Shotgun Surgery**
Opposite of Divergent Change, it occurs when a single change is made in multiple places across the codebase.
- **Lazy Class/Freeloader**
Classes that do very little and are not pulling their weight.
- **Speculative Generality**
Writing code that is more general than it needs to be, often to support anticipated future features that never get used.
- **Switch Statements**
Overuse of switch statements or complex conditionals, often a sign that polymorphism could be used.
- **Temporary Field**
Fields that are only set in certain circumstances. This can be confusing since the object does not always use all of its fields.
- **Refused Bequest**
When a subclass does not use methods and properties inherited from its parent class.
- **Data Class**
A class that only contains fields and crude methods for accessing them (getters/setters).
- **Message Chains**
Occurs when a client asks one object for another object, which the client then asks for another object, and so on.
- **Middle Man**
When a class does nothing but delegate to another class.
- **Parallel Inheritance Hierarchies**
Every time you make a subclass of one class, you also have to make a subclass of another.
- **Inappropriate Intimacy**
When one class knows too much about the internals of another class.
- **Alternative Classes with Different Interfaces**
Two classes perform identical functions but have different method names.

---

- **Test-Coverage** 
per line

---

### Keep all entities small
- Function/Method: 5-15 lines of code
- Classes: Under 100-200 lines of code
- Methods per Class: No more than 10-20 methods
- Parameters per Method: Fewer than 4
- Cyclomatic Complexity: Under 10
- Lines of Code per File: 200-500 lines of code

### cyclomatic complexity
#### Step 1
let gpt create a control flow graph
```
main
  |
  +---> argparse
        |
        +---> join (if command is 'join')
        |     |
        |     +---> load_db_schema
        |     |
        |     +---> is_unused_id (for 'players')
        |     |     |
        |     |     +---> insert_into_db (if ID is unused)
        |     |           |
        |     |           +---> build_insert
        |     |
        |     +---> is_unused_id (for 'tables')
        |           |
        |           +---> insert_into_db (if ID is unused)
        |           |     |
        |           |     +---> build_insert
        |           |
        |           +---> update_column (if ID is used)
        |                 |
        |                 +---> (update 'tables')
        |                 +---> (update 'players')
        |
        +---> init_db (if command is 'init')
        |     |
        |     +---> (initiates database)
        |
        +---> parser.print_help (for other cases)
```

#### Step 2
using this graph make gpt give you 
E: The number of edges in the flow graph.
N: The number of nodes in the flow graph.
P: The number of connected components (e.g., subgraphs) in the flow graph.

Template: 
[E]=[number of edges in flow graph]
[N]=[number of nodes in flow graph]
[P]=[number of connected components in flow graph]

#### Step 3
Regex on this output to get the numbers

#### Step 4
then calculate cyclomatic complexity using the formula: 
CC = E - N + 2P
(do not use gpt for this but python)

# What should be the outcome?
I want to have a report detailing what is currently wrong with  my code and where. 

## Detailed report (v1)
- cyclomatic complexity per file
- violation of maxlines per file
- violation of maxlines per function/method
- violation maxmethods per class
- violation of maxparameters per class/function
- method/function does not return anything
- violations of One Level of Indentation rule
- violations of do not abbreviate rule
- violations of Don’t Use `else` rule
- free floating globals or logic that is not wrapped in a function or class
- violations of CQRS principle (command query separation) per method/function

### Examples (v1)
```
path/to/file: 
average cc - 2 
total cc - 500
nesting over max - 3 
lines over max - 100 
used global vars - true 
unwrapped logic - true 

	function1: 
		lines over max - 10
		parameters over max - 2
		no return value - true
		CQRS violated - true
	
	lines: 
		abbreviation - lines[1, 6, 33, 65]
		used ELSE - lines[3,5, 25]
		
	classA: 
		methods over max - 3
		parameters over max - 1
		lines over max - 50
```


### config
```
max_methods: 20
function_max_lines: 15
max_parameters: 4
class_max_lines: 200
file_max_lines: 500
global_max_cc: 10
file_max_cc: 3
```

## Global report(v1)
- total cyclomatic complexity
- bad files/total files
- SOLID violations


## Detailed report (v2)
- add testability
- add readability 
	- bools should start with "is"/"has" varname
	- Class should be Nouns
	- functions/methods should start with verbs (what does it DO)
	- varnames should imply datatype in name (customer_list, payroll_dict, etc)
	- varnames should be used consistently across functions/methods/classes (same name if injected in another component)


## Detailed report (v3)
- add testcoverage per lines (config: command to execute tests)