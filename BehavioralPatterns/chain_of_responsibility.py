# Chain of responsibility design pattern

# Base handler class
class SupportHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        pass

# Concrete handler for Junior Support
class JuniorSupport(SupportHandler):
    def handle(self, request):
        if request == 'simple':
            print('Junior Support handling the request: Simple Issue.')
        elif self.next_handler:
            print("Junior Support can't handle it. Passing to Senior Support.")
            self.next_handler.handle(request)

# Concrete handler for Senior Support
class SeniorSupport(SupportHandler):
    def handle(self, request):
        if request == 'complex':
            print('Senior Support handling the request: Complex Issue.')
        elif self.next_handler:
            print("Senior Support can't handle it. Passing to Manager")
            self.next_handler.handle(request)


# Concrete handler for Manager
class Manager(SupportHandler):
    def handle(self, request):
        print('Manager handling the request: Critical Issue.')

# Creating the handler in the chain: Junior > Senior > Manager

manager = Manager()
senior_support = SeniorSupport(manager)
junior_support = JuniorSupport(senior_support)

# Simple Issue
junior_support.handle('simple')
print()

# Complex Issue
junior_support.handle('complex')
print()

# Critical Issue
junior_support.handle('critical')
