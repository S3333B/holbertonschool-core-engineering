#!/usr/bin/env python3
"""
Module animals

Defines an abstract Animal class and concrete subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class inheriting from Animal.
    """

    def sound(self):
        """
        Return the dog sound.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class inheriting from Animal.
    """

    def sound(self):
        """
        Return the cat sound.
        """
        return "Meow"
