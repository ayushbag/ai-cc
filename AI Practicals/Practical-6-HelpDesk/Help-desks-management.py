import uuid
from datetime import datetime
from enum import Enum

class Status(Enum):
    OPEN = "Open"
    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"

class Role(Enum):
    USER = "User"
    AGENT = "Agent"
    ADMIN = "Admin"

class Ticket:
    def __init__(self, subject, description, submitted_by, category, priority):
        self.ticket_id = str(uuid.uuid4())
        self.subject = subject
        self.description = description
        self.creation_date = datetime.now()
        self.status = Status.OPEN
        self.priority = priority
        self.submitted_by = submitted_by
        self.assigned_to = None
        self.resolution_details = None
        self.resolution_date = None
        self.category = category

    def __str__(self):
        assigned_to_name = self.assigned_to.username if self.assigned_to else "Not Assigned"
        return (f"ID: {self.ticket_id}, Subject: {self.subject}, Status: {self.status.value}, "
                f"Priority: {self.priority.value}, Submitted by: {self.submitted_by.username}, "
                f"Assigned to: {assigned_to_name}")

class User:
    def __init__(self, username, password, email, role, department, contact_number):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = self._hash_password(password) # In a real application, use a proper hashing library
        self.email = email
        self.role = role
        self.department = department
        self.contact_number = contact_number

    def _hash_password(self, password):
        # In a real application, use a secure hashing library like bcrypt or hashlib with salt
        return password

    def check_password(self, password):
        # In a real application, compare against the hashed password
        return self._hash_password(password) == password

    def __str__(self):
        return f"ID: {self.user_id}, Username: {self.username}, Role: {self.role.value}"

class Department:
    def __init__(self, name):
        self.department_id = str(uuid.uuid4())
        self.name = name

    def __str__(self):
        return f"ID: {self.department_id}, Name: {self.name}"

class Category:
    def __init__(self, name):
        self.category_id = str(uuid.uuid4())
        self.name = name

    def __str__(self):
        return f"ID: {self.category_id}, Name: {self.name}"

class Comment:
    def __init__(self, ticket, user, comment_text):
        self.comment_id = str(uuid.uuid4())
        self.ticket = ticket
        self.user = user
        self.comment_text = comment_text
        self.creation_date = datetime.now()

    def __str__(self):
        return f"ID: {self.comment_id}, Ticket ID: {self.ticket.ticket_id}, User: {self.user.username}, Comment: {self.comment_text}"

class TicketRepository:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def get_ticket_by_id(self, ticket_id):
        return self.tickets.get(ticket_id)

    def get_all_tickets(self):
        return list(self.tickets.values())

    def update_ticket(self, ticket):
        if ticket.ticket_id in self.tickets:
            self.tickets[ticket.ticket_id] = ticket

    def delete_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]

    def find_tickets_by_status(self, status):
        return [ticket for ticket in self.tickets.values() if ticket.status == status]

    def find_tickets_by_user(self, user):
        return [ticket for ticket in self.tickets.values() if ticket.submitted_by == user]

    def assign_ticket(self, ticket_id, agent):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            ticket.assigned_to = agent

class UserRepository:
    def __init__(self):
        self.users = {}

    def create_user(self, user):
        self.users[user.user_id] = user

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)

    def get_user_by_username(self, username):
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user):
        if user.user_id in self.users:
            self.users[user.user_id] = user

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

class DepartmentRepository:
    def __init__(self):
        self.departments = {}

    def create_department(self, department):
        self.departments[department.department_id] = department

    def get_department_by_id(self, department_id):
        return self.departments.get(department_id)

    def get_all_departments(self):
        return list(self.departments.values())

    def update_department(self, department):
        if department.department_id in self.departments:
            self.departments[department.department_id] = department

    def delete_department(self, department_id):
        if department_id in self.departments:
            del self.departments[department_id]

class CategoryRepository:
    def __init__(self):
        self.categories = {}

    def create_category(self, category):
        self.categories[category.category_id] = category

    def get_category_by_id(self, category_id):
        return self.categories.get(category_id)

    def get_all_categories(self):
        return list(self.categories.values())

    def update_category(self, category):
        if category.category_id in self.categories:
            self.categories[category.category_id] = category

    def delete_category(self, category_id):
        if category_id in self.categories:
            del self.categories[category_id]

class CommentRepository:
    def __init__(self):
        self.comments = {}

    def add_comment(self, comment):
        self.comments[comment.comment_id] = comment

    def get_comments_by_ticket_id(self, ticket_id):
        return [comment for comment in self.comments.values() if comment.ticket.ticket_id == ticket_id]

class TicketService:
    def __init__(self, ticket_repository, user_repository):
        self.ticket_repository = ticket_repository
        self.user_repository = user_repository

    def submit_new_ticket(self, subject, description, user_id, category, priority):
        submitted_by = self.user_repository.get_user_by_id(user_id)
        if submitted_by:
            new_ticket = Ticket(subject, description, submitted_by, category, priority)
            self.ticket_repository.create_ticket(new_ticket)
            print(f"Ticket submitted successfully with ID: {new_ticket.ticket_id}")
            return new_ticket
        else:
            print("Error: User not found.")
            return None

    def view_ticket_details(self, ticket_id):
        return self.ticket_repository.get_ticket_by_id(ticket_id)

    def assign_ticket_to_agent(self, ticket_id, agent_id):
        ticket = self.ticket_repository.get_ticket_by_id(ticket_id)
        agent = self.user_repository.get_user_by_id(agent_id)
        if ticket and agent and agent.role == Role.AGENT:
            ticket.assigned_to = agent
            self.ticket_repository.update_ticket(ticket)
            print(f"Ticket {ticket_id} assigned to agent {agent.username}")
        elif not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
        elif not agent:
            print(f"Error: Agent with ID {agent_id} not found.")
        else:
            print("Error: User is not an agent.")

    def update_ticket_status(self, ticket_id, new_status, resolution_details=None):
        ticket = self.ticket_repository.get_ticket_by_id(ticket_id)
        if ticket and isinstance(new_status, Status):
            ticket.status = new_status
            if resolution_details:
                ticket.resolution_details = resolution_details
                ticket.resolution_date = datetime.now()
            self.ticket_repository.update_ticket(ticket)
            print(f"Ticket {ticket_id} status updated to {new_status.value}")
        elif not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
        else:
            print("Error: Invalid status.")

    def get_tickets_by_status(self, status):
        return self.ticket_repository.find_tickets_by_status(status)

    def get_tickets_for_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return self.ticket_repository.find_tickets_by_user(user)
        else:
            print("Error: User not found.")
            return []

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_new_user(self, username, password, email, role, department, contact_number):
        if self.user_repository.get_user_by_username(username):
            print("Error: Username already exists.")
            return None
        new_user = User(username, password, email, role, department, contact_number)
        self.user_repository.create_user(new_user)
        print(f"User {username} registered successfully with ID: {new_user.user_id}")
        return new_user

    def login_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and user.check_password(password):
            print(f"User {username} logged in successfully.")
            return user
        else:
            print("Error: Invalid username or password.")
            return None

    def get_user_details(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def update_user_profile(self, user):
        self.user_repository.update_user(user)
        print(f"User {user.username} profile updated.")

class DepartmentService:
    def __init__(self, department_repository):
        self.department_repository = department_repository

    def create_department(self, name):
        new_department = Department(name)
        self.department_repository.create_department(new_department)
        print(f"Department '{name}' created with ID: {new_department.department_id}")
        return new_department

    def get_department_by_id(self, department_id):
        return self.department_repository.get_department_by_id(department_id)

    def get_all_departments(self):
        return self.department_repository.get_all_departments()

class CategoryService:
    def __init__(self, category_repository):
        self.category_repository = category_repository

    def create_category(self, name):
        new_category = Category(name)
        self.category_repository.create_category(new_category)
        print(f"Category '{name}' created with ID: {new_category.category_id}")
        return new_category

    def get_category_by_id(self, category_id):
        return self.category_repository.get_category_by_id(category_id)

    def get_all_categories(self):
        return self.category_repository.get_all_categories()

class CommentService:
    def __init__(self, comment_repository, ticket_repository, user_repository):
        self.comment_repository = comment_repository
        self.ticket_repository = ticket_repository
        self.user_repository = user_repository

    def add_comment_to_ticket(self, ticket_id, user_id, comment_text):
        ticket = self.ticket_repository.get_ticket_by_id(ticket_id)
        user = self.user_repository.get_user_by_id(user_id)
        if ticket and user:
            new_comment = Comment(ticket, user, comment_text)
            self.comment_repository.add_comment(new_comment)
            print(f"Comment added to ticket {ticket_id} by user {user.username}")
            return new_comment
        elif not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
        else:
            print(f"Error: User with ID {user_id} not found.")
            return None

    def get_comments_by_ticket_id(self, ticket_id):
        return self.comment_repository.get_comments_by_ticket_id(ticket_id)

class HelpDeskCLI:
    def __init__(self, ticket_service, user_service):
        self.ticket_service = ticket_service
        self.user_service = user_service
        self.logged_in_user = None

    def run(self):
        print("Welcome to the Help Desk System!")
        while True:
            if not self.logged_in_user:
                print("\n1. Register\n2. Login\n3. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.register_user()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print(f"\nWelcome, {self.logged_in_user.username} ({self.logged_in_user.role.value})")
                if self.logged_in_user.role == Role.USER:
                    print("1. Submit New Ticket\n2. View My Tickets\n3. Logout")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        self.submit_ticket()
                    elif choice == '2':
                        self.view_my_tickets()
                    elif choice == '3':
                        self.logout()
                    else:
                        print("Invalid choice. Please try again.")
                elif self.logged_in_user.role in [Role.AGENT, Role.ADMIN]:
                    print("1. View All Tickets\n2. Assign Ticket\n3. Update Ticket Status\n4. Logout")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        self.view_all_tickets()
                    elif choice == '2':
                        self.assign_ticket()
                    elif choice == '3':
                        self.update_ticket_status()
                    elif choice == '4':
                        self.logout()
                    else:
                        print("Invalid choice. Please try again.")

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        role_str = input("Enter role (USER, AGENT, ADMIN): ").upper()
        try:
            role = Role[role_str]
        except KeyError:
            print("Invalid role.")
            return
        department = input("Enter department: ")
        contact_number = input("Enter contact number: ")
        self.user_service.register_new_user(username, password, email, role, department, contact_number)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.user_service.login_user(username, password)
        if user:
            self.logged_in_user = user

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully.")

    def submit_ticket(self):
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        category_name = input("Enter category: ")
        priority_str = input("Enter priority (LOW, MEDIUM, HIGH, URGENT): ").upper()
        try:
            priority = Priority[priority_str]
        except KeyError:
            print("Invalid priority.")
            return

        # In a real application, you might fetch or create the category object
        # For this example, we'll just pass the name
        self.ticket_service.submit_new_ticket(subject, description, self.logged_in_user.user_id, category_name, priority)

    def view_my_tickets(self):
        if self.logged_in_user:
            tickets = self.ticket_service.get_tickets_for_user(self.logged_in_user.user_id)
            if tickets:
                print("\nYour Tickets:")
                for ticket in tickets:
                    print(ticket)
            else:
                print("You have no open tickets.")
        else:
            print("You are not logged in.")

    def view_all_tickets(self):
        if self.logged_in_user and self.logged_in_user.role in [Role.AGENT, Role.ADMIN]:
            tickets = self.ticket_service.ticket_repository.get_all_tickets()
            if tickets:
                print("\nAll Tickets:")
                for ticket in tickets:
                    print(ticket)
            else:
                print("No tickets available.")
        else:
            print("You do not have permission to view all tickets.")

    def assign_ticket(self):
        if self.logged_in_user and self.logged_in_user.role in [Role.AGENT, Role.ADMIN]:
            ticket_id = input("Enter the ID of the ticket to assign: ")
            agent_username = input("Enter the username of the agent to assign to: ")
            agent = self.user_service.user_repository.get_user_by_username(agent_username)
            if agent and agent.role == Role.AGENT:
                self.ticket_service.assign_ticket_to_agent(ticket_id, agent.user_id)
            elif not agent:
                print(f"Agent with username '{agent_username}' not found.")
            else:
                print(f"{agent_username} is not an agent.")
        else:
            print("You do not have permission to assign tickets.")

    def update_ticket_status(self):
        if self.logged_in_user and self.logged_in_user.role in [Role.AGENT, Role.ADMIN]:
            ticket_id = input("Enter the ID of the ticket to update: ")
            status_str = input("Enter the new status (OPEN, ASSIGNED, IN_PROGRESS, RESOLVED, CLOSED): ").upper()
            try:
                new_status = Status[status_str]
                resolution_details = None
                if new_status == Status.RESOLVED or new_status == Status.CLOSED:
                    resolution_details = input("Enter resolution details (if any): ")
                self.ticket_service.update_ticket_status(ticket_id, new_status, resolution_details)
            except KeyError:
                print("Invalid status.")
        else:
            print("You do not have permission to update ticket statuses.")

if __name__ == "__main__":
    ticket_repo = TicketRepository()
    user_repo = UserRepository()
    dept_repo = DepartmentRepository()
    cat_repo = CategoryRepository()
    comment_repo = CommentRepository()

    user_service = UserService(user_repo)
    ticket_service = TicketService(ticket_repo, user_repo)
    dept_service = DepartmentService(dept_repo)
    cat_service = CategoryService(cat_repo)
    comment_service = CommentService(comment_repo, ticket_repo, user_repo)

    cli = HelpDeskCLI(ticket_service, user_service)
    cli.run()