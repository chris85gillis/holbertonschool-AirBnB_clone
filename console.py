#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
import os
import uuid
from models import storage
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

    def show(self, args):
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        
        named_class = args_list[0]
        if named_class not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        objid = args_list[1]

        instances = BaseModel.all()
        key = named_class + "." + objid
        obj = instances.get(key)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def destroy(self, args):
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return

        named_class = args_list[0]
        if named_class not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        objid = args_list[1]

        instances = BaseModel.all()
        key = named_class + "." + objid
        obj = instances.get(key)

        if obj:
            instances.pop(key)
            BaseModel.save_to_file()
        else:
            print("** no instance found **")

    def all(self, args):
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        
        named_class = args_list[0]
        if named_class not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args_list) > 1:
            try:
                instances = BaseModel.all(eval(named_class))
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            instances = BaseModel.all()
        print([str(obj) for obj in instances.values()])

    def update(self, args):
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return

        named_class = args_list[0]
        if named_class not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        objid = args_list[1]
        instances = BaseModel.all()
        key = named_class + "." + objid

        if key not in instances:
            print("** no instance found **")
            return
        
        if len(args_list) < 4:
            print("** attribute name missing **")
            return

        attr_name = args_list[2]
        attr_value = args_list[3]

        obj = instances[key]
        if hasattr(obj, attr_name):
            try:
                if isinstance(obj.__dict__[attr_name], int):
                    setattr(obj, attr_name, int(attr_value))
                elif isinstance(obj.__dict__[attr_name], float):
                    setattr(obj, attr_name, float(attr_value))
                else:
                    setattr(obj, attr_name, attr_value.strip("''"))
                obj.save()
            except (ValueError, TypeError):
                print("** invalid value type **")
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
