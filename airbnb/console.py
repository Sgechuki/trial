#!/usr/bin/python3
"""This module holds the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from model.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand inherits from cmd class
    and defines our customized command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "City": City, "State": State, "Amenity": Amenity,
               "Review": Review}

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        If the class name is missing, print ** class name missing **
        If the class name doesn’t exist, print ** class doesn't exist **
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation
        of an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        else:
            k = args.replace(' ', '.')
            if k in storage.all():
                objs = storage.all()
                print(objs[k])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        else:
            k = args.replace(' ', '.')
            if k in storage.all():
                objs = storage.all()
                del objs[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation
        of all instances based or not on the class name"""
        lst = []
        objs = storage.all()
        if len(arg) == 0:
            for k in objs.keys():
                a = str(objs[k])
                lst.append(a)
            print(lst)
        elif arg in self.classes.keys():
            for k in objs.keys():
                cls = k.split()[0]
                if k == cls:
                    b = str(objs[k])
                    lst.append(b)
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()[1]) == 0:
            print("** instance id missing **")
        else:
            cls = args.split()[0]
            uid = args.split()[1]
            key = "{}.{}".format(cls, uid)
            if key not in objs.keys():
                print("** no instance found **")
            elif len(args.split()[2]) == 0:
                print("** attribute name missing **")
            elif len(args.split()[3]) == 0:
                print("** value missing **")
            else:
                attr = args.split()[2]
                value = args.split()[3]
                setattr(objs[key], attr, value[1:-1])
                storage.save()

    def do_quit(self, arg):
        """Quit command exits the program"""
        return True

    def do_EOF(self, arg):
        """exits the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute
        anything"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
