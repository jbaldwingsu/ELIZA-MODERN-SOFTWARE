import pytest
from unittest.mock import MagicMock, patch
from io import StringIO
from cookassist import (
    connect_to_database,
    find_ingredients,
    find_recipes_by_ingredients,
    fetch_all_ingredients,
    fetch_all_recipes,
    
    
)

@pytest.fixture(scope="module")
def mock_db_connection():
    # Mocking the database connection
    return MagicMock()

@pytest.fixture(scope="module")
def mock_cursor(mock_db_connection):
    # Mocking the database cursor
    return mock_db_connection.cursor.return_value

def test_connect_to_database():
    # Testing database connection
    db_connection = connect_to_database()
    assert db_connection is not None

def test_find_ingredients(mock_cursor):
    # Mocking the cursor execute method
    mock_cursor.fetchall.return_value = [("Ingredient 1",), ("Ingredient 2",)]
    
    # Testing find ingredients function
    ingredients = find_ingredients(mock_cursor, "Recipe Name")
    assert ingredients == ["Ingredient 1", "Ingredient 2"]

def test_find_recipes_by_ingredients(mock_cursor):
    # Mocking the cursor execute method
    mock_cursor.fetchall.return_value = [("Recipe 1",), ("Recipe 2",)]
    
    # Testing find recipes by ingredients function
    recipes = find_recipes_by_ingredients(mock_cursor, "Ingredient Name")
    assert recipes == ["Recipe 1", "Recipe 2"]

def test_fetch_all_ingredients(mock_cursor):
    # Mocking the cursor execute method
    mock_cursor.fetchall.return_value = [("Ingredient 1",), ("Ingredient 2",)]
    
    # Testing fetch all ingredients function
    ingredients = fetch_all_ingredients(mock_cursor)
    assert ingredients == ["Ingredient 1", "Ingredient 2"]

def test_fetch_all_recipes(mock_cursor):
    # Mocking the cursor execute method
    mock_cursor.fetchall.return_value = [("Recipe 1",), ("Recipe 2",)]
    
    # Testing fetch all recipes function
    recipes = fetch_all_recipes(mock_cursor)
    assert recipes == ["Recipe 1", "Recipe 2"]

# Add more tests as needed

@patch('builtins.input', side_effect=["1", "1", "no"])
@patch('sys.stdout', new_callable=StringIO)
def test_main_choice_1(mock_stdout, mock_input):
    main()
    output = mock_stdout.getvalue()
    assert "See you! Hope the food turns out GREAT!" in output

@patch('builtins.input', side_effect=["2", "1", "no"])
@patch('sys.stdout', new_callable=StringIO)
def test_main_choice_2(mock_stdout, mock_input):
    main()
    output = mock_stdout.getvalue()
    assert "See you! Hope the food turns out GREAT!" in output