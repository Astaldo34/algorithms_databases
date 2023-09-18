class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class BinaryTree:

    """
        Класс бинарного дерева.

        Методы:
            add(self, value)
              Добавьте элементы в дерево.
            search(self, value)
              Найдите элемент в дереве и верните его или нет.
            count_nodes(self)
              Подсчет количества элементов бинарного дерева
            print_node(self)
              Распечатать дерево, начиная с root.
            delete(self, value)
              Найти элемент в дереве по значению и удалите его.

    """

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """
            Добавление элемента в дерево
        """
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

        print(self.root)

    def search(self, node, value, parent=None):
        """
            Нахождение элемента в дереве и возвращение результата
        """
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count_nodes(self):
        """
            Подсчёт количества элементов бинарного дерева
        """
        counter = 0
        current = self.root
        while current is not None:
            counter += 1
            current = current.right

        current = self.root
        while current is not None:
            counter += 1
            current = current.left

        return counter-1

    def print_node(self, node: Node):
        """
            Распечатать дерево, начиная с root.
        """
        if node is None:
            return
        self.print_node(node.left)
        print(node.value)
        self.print_node(node.right)

    def delete(self, value):
        """
            Нахождение элемента в дереве и удаление его
        """
        self.root = self.delete_(self.root, value)

    def delete_(self, current_node, value):
        """
            Вспомогательная функция для метода удаления
        """
        if not current_node:
            return current_node
        elif value < current_node.value:
            current_node.left = self.delete_(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_(current_node.right, value)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                return current_node
        return current_node


bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(4)
bt.add(3)
bt.delete(4)

# print(bt.root)
print(f'Количество элементов - {bt.count_nodes()}')
# print(bt.search(bt.root, 8)[1])
bt.print_node(bt.root)
