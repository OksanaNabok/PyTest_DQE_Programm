import pytest
import sys
import os

# Add the parent directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_connection import get_db_connection

# Test Case 1: Check total number of records in the Address table
def test_address_record_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Person].[Address];")
    result = cursor.fetchone()
    conn.close()
    assert result[0] == 19614, f"Expected 19614 records, but got {result[0]}"  # Adjust 19614 to your actual expected record count

# Test Case 2: Verify the count of distinct Postal Codes in the Address table
def test_address_postal_code_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT [PostalCode]) FROM [Person].[Address];")
    postal_codes = cursor.fetchone()
    conn.close()
    assert postal_codes[0] == 661, f"Expected 661 records, but got {postal_codes[0]}" # Current value is 661. Replace 661 with your expected value

