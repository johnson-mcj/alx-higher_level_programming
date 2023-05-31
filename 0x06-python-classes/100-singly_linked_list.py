#!/usr/bin/python3
"""
Module documentation: Singly Linked List
"""


class Node:
    """
    Node class represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with a given data value and next node.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list.

        Raises:
            TypeError: If the data is not an integer.
            TypeError: If the next_node is not None or a Node object.
        """
        self.__data = None
        self.data = data
        self.__next_node = None
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty SinglyLinkedList object.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list.

        Args:
            value (int): The data value of the new node to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        if self.head is None:
            return ""

        current = self.head
        result = str(current.data)
        while current.next_node is not None:
            current = current.next_node
            result += '\n' + str(current.data)
        return result
