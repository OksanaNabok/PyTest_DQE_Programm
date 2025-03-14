import pytest
from db_connection import get_db_connection

# Test Case 1: Ensure no null values in FileExtension column
def test_file_extension_not_null():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Production].[Document] WHERE [FileExtension] IS NULL;")
    result = cursor.fetchone()
    conn.close()
    assert result[0] == 0, f"Found {result[0]} FileExtension with NULL summaries"

# Test Case 2: Validate Total Records in the Document Table is greater than 10
def test_document_record_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Production].[Document];")
    result = cursor.fetchone()
    conn.close()
    assert result[0] > 10, f"Expected more than 10 documents, but got {result[0]}"