import pytest
from db_connection import get_db_connection


# Test Case 1: Verify Minimum ModifiedDate in UnitMeasure Table
def test_unitmeasure_min_modified_date():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MIN([ModifiedDate]) FROM [Production].[UnitMeasure];")
    result = cursor.fetchone()
    conn.close()
    # You may replace the expected minimum date with an actual known value
    assert str(result[0]) >= '2000-01-01', f"Unexpected minimum ModifiedDate: {result[0]}"


# Test Case 2: Check for unique names in the UnitMeasure table
def test_unitmeasure_unique_name_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT [Name]) FROM [Production].[UnitMeasure];")
    result = cursor.fetchone()
    conn.close()
    assert result[0] == 38, f"Expected 38 unique names, but got {result[0]}"  # Replace 38 with your known expected count
