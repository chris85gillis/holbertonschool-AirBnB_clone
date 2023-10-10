#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import os
import uuid
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                if arg == "BaseModel":
                    new_instance = {'id': str(uuid.uuid4())}
                    with open("file.json", "r") as file:
                        data = json.load(file)
                    data[f"BaseModel.{new_instance['id']}"] = new_instance
                    with open("file.json", "w") as file:
                        json.dump(data, file)
                    print(new_instance['id'])
                else:
                    print("** class doesn't exist **")
            except Exception as e:
                print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
