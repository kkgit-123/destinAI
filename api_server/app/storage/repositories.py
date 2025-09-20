from app.storage.database import get_db_connection
from typing import List, Dict, Any

class EmployeeRepository:
    """
    Repository class for interacting with employee data in the database.
    """
    def get_all_employees(self) -> List[Dict[str, Any]]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, position FROM employees")
        employees = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return employees

    def get_employee_by_id(self, employee_id: int) -> Dict[str, Any] | None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, position FROM employees WHERE id = ?", (employee_id,))
        employee = cursor.fetchone()
        conn.close()
        return dict(employee) if employee else None

# Example usage (for testing purposes)
if __name__ == "__main__":
    from app.storage.database import initialize_database
    initialize_database() # Ensure DB is set up

    repo = EmployeeRepository()
    print("All employees:", repo.get_all_employees())
    print("Employee with ID 1:", repo.get_employee_by_id(1))
    print("Employee with ID 99:", repo.get_employee_by_id(99))
