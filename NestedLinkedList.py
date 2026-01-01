class Computer:
    def __init__(self, compName, compId):
        self.compName = compName
        self.compId = compId
        self.next = None


class Table:
    def __init__(self, tableName):
        self.tableName = tableName
        self.computers = None
        self.next = None


class TableList:
    def __init__(self):
        self.head = None

    def add_Table(self, name):
        new_Table = Table(name)
        if self.head is None:
            self.head = new_Table
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_Table

    def find_Table(self, name):
        temp = self.head
        while temp:
            if temp.tableName == name:
                return temp
            temp = temp.next
        return None

    def add_computer(self, tableName,compName, compId):
        table = self.find_Table(tableName)
        if table is None:
            print(f"Student named {name} was not found.")
            return
        new_comp = Computer(compName, compId)
        if table.computers is None:
            table.computers = new_comp
        else:
            temp = table.computers
            while temp.next:
                temp = temp.next
            temp.next = new_comp

    def display(self):
        temp_table = self.head
        while temp_table:
            print(f"\ Table: {temp_table.tableName}")
            if temp_table.computers is None:
                print("No computers added yet.")
            else:
                temp_computers = temp_table.computers
                while temp_computers:
                    print(f"Computer Id: {temp_computers.compId} | Computer Name: {temp_computers.compName}")
                    temp_computers = temp_computers.next
            temp_table = temp_table.next


tables = TableList()

tables.add_Table("Masa 1")
tables.add_Table("Masa 2")

tables.add_computer("Masa 1", "1", "Computer 1")
tables.add_computer("Masa 1", "2", "Computer 2")
tables.add_computer("Masa 2", "3", "Computer 3")

tables.display()