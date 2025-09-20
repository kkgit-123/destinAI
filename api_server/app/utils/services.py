from app.storage.repositories import EmployeeRepository
from typing import List, Dict, Any

class EmployeeService:
    """
    Service layer for handling business logic related to employees.
    Interacts with the EmployeeRepository.
    """
    def __init__(self):
        self.employee_repo = EmployeeRepository()

    def get_all_employees(self, user_id: int) -> List[Dict[str, Any]]:
        """
        Retrieves all employees.
        In a real application, this might involve authorization checks based on user_id.
        """
        # Example of using user_id in service layer
        # if user_id != 123: # Only user 123 can see all employees
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to view all employees")
        employees = self.employee_repo.get_all_employees()
        return employees

    def get_employee_by_id(self, employee_id: int, user_id: int) -> Dict[str, Any] | None:
        """
        Retrieves a single employee by ID.
        In a real application, this might involve authorization checks based on user_id.
        """
        employee = self.employee_repo.get_employee_by_id(employee_id)
        # Example of using user_id in service layer for access control
        # if employee and employee.get("owner_id") != user_id:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to view this employee")
        return employee

# Example usage (for testing purposes)
if __name__ == "__main__":
    from app.storage.database import initialize_database
    initialize_database() # Ensure DB is set up

    service = EmployeeService()
    dummy_user_id = 123 # Replace with a valid user ID for testing
    print("All employees (via service):", service.get_all_employees(dummy_user_id))
    print("Employee with ID 1 (via service):", service.get_employee_by_id(1, dummy_user_id))
    print("Employee with ID 99 (via service):", service.get_employee_by_id(99, dummy_user_id))
