# 🍽️ Digital Recipe Book Manager

A command-line Recipe Management System built with Python that allows users to create, organize, search, edit, and manage recipes efficiently. The application uses local file storage to save recipes, ensuring data persists between sessions.

---

##  Overview

The Digital Recipe Book Manager is a menu-driven application designed to help users maintain a personal recipe collection. It provides a simple command-line interface with input validation, automatic file handling, searching, filtering, editing, exporting, and statistical summaries.

---

##  Features

-  Add new recipes
-  View all recipes
-  View recipes by ID
-  Search recipes by ingredient
-  Filter recipes by:
  - Category
  - Cooking time
  - Number of ingredients
-  Edit recipe details
-  Delete recipes
-  View recipe statistics
-  Automatically save recipes
-  Automatically load saved recipes
-  Export individual recipes to text files

---

## 🛠 Technologies Used

- Python 3
- File Handling
- Dictionaries
- Lists
- Tuples
- Sets
- Functions
- Loops
- Conditional Statements
- Exception Handling

---

## Project Structure

```text
Digital-Recipe-Book-Manager/
│
├── python-recipe-book-manager.py
├── recipes.txt
├── RCP006.txt
├── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x installed on your computer

### Running the Application

```bash
python python-recipe-book-manager.py
```

---

## Main Menu

```text
1  - Add New Recipe
2  - View All Recipes
3  - View Recipe by ID
4  - Search by Ingredient
5  - Filter Recipes
6  - Edit Recipe
7  - Delete Recipe
8  - View Statistics
9  - Save Recipes
10 - Export Recipe
11 - Exit
```

---

## Data Storage

Recipes are stored in a local text file named:

```text
recipes.txt
```

Each recipe contains:

- Recipe ID
- Recipe Name
- Category
- Cooking Time
- Ingredients
- Tags

The application automatically loads saved recipes when it starts and saves changes after modifications.

---

## Statistics

The application provides:

- Total number of recipes
- Recipes grouped by category
- Top 3 most frequently used ingredients
- Average number of ingredients per recipe

---

## Input Validation

The program validates user input by checking:

- Recipe name format
- Ingredient names
- Quantity values
- Measurement units
- Cooking time format
- Recipe category
- Duplicate ingredient confirmation
- Invalid menu selections
- File handling errors

---

## Export Functionality

Individual recipes can be exported as separate text files.

Example:

```text
RCP006.txt
```

---

## Python Concepts Demonstrated

- Functions
- Dictionaries
- Lists
- Tuples
- Sets
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- Input Validation
- Modular Programming

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- CRUD (Create, Read, Update, Delete) operations
- Data validation
- Local file persistence
- Command-line application development
- Python data structures
- Structured programming techniques

---

## Author

**Pesandi Hettiarachchi**
