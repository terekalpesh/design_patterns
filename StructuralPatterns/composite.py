# Composite design pattern

from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def get_size(self):
        return self.size

    @abstractmethod
    def display(self, indent = 0):
        pass
        
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
    
    def display(self, indent=0):
        return print(' '*indent + f'File: {self.name}, Size: {self.get_size()} bytes')


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        if component is not None:
            self.components.append(component)
    
    def remove(self, component):
        if component in self.components:
            self.components.remove(component)

    def get_size(self):
        total_size = 0
        for component in self.components:
            total_size += component.get_size()
        return total_size
    
    def display(self, indent=0):
        print(' '*indent + f'Directory: {self.name}')
        for component in self.components:
            component.display(indent+2)
            

file1 = File('file1.txt', 500)
file2 = File('file2.txt', 400)
file3 = File('file3.txt', 600)

dir1 = Directory('dir1')
dir1.add(file1)
dir1.add(file2)

dir2 = Directory('dir2')
dir2.add(file3)

root_dir = Directory('root')
root_dir.add(dir1)
root_dir.add(dir2)

root_dir.display()
print(root_dir.get_size())
print(dir2.get_size())