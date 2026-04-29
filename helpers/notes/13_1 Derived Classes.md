## 13.1 Derived classes

A class will commonly share attributes with another class, but with some additions or variations. Ex: A store inventory system might use a class called Item, having name and quantity attributes. But for fruits and vegetables, a class Produce might have the attributes name, quantity, and expiration date. Note that Produce is really an Item with an additional feature, so ideally a program could define the Produce class as being the same as the Item class but with the addition of an expiration date attribute. 

 Such similarity among classes is supported by indicating that a class is *derived* from another class, as shown below.

> **A derived class example: Class Produce is derived from class Items.**
> ```python
> class Item:
>     def __init__(self):
>         self.name = ""
>         self.quantity = 0
> 
>     def set_name(self, nm):
>         self.name = nm
> 
>     def set_quantity(self, qnty):
>         self.quantity = qnty
> 
>     def display(self):
>         print(self.name, self.quantity)
> 
> 
> class Produce(Item):  # Derived from Item
>     def __init__(self):
>         Item.__init__(self)  # Call base class constructor
>         self.expiration = ""
> 
>     def set_expiration(self, expir):
>         self.expiration = expir
> 
>     def get_expiration(self):
>         return self.expiration
> 
> item1 = Item()
> item1.set_name("Smith Cereal")
> item1.set_quantity(9)
> item1.display()
> 
> item2 = Produce()
> item2.set_name("Apples")
> item2.set_quantity(40)
> item2.set_expiration("May 5, 2012")
> item2.display()
> print(f"  (Expires:({item2.get_expiration()}))")
> ```
> ```
> Smith Cereal 9
> Apples 40
>   (Expires:(May 5, 2012))
> ```

The example defines a class named Item.  In the script, an instance of Item is created called item1, the instance's attributes are set to Smith Cereal and 9, and the display() method is called. A class named Produce is also defined. That class was *derived* from the Item class by including the base class Item within parentheses after Produce. Ex: `class Produce(Item):`. As such, instantiating a Produce instance item2 creates an instance object with the data attributes name and quantity (from Item), plus expiration (from Produce), as well as with the methods set_name(), set_quantity(), and display() from Item, and set_expiration() and get_expiration() from Produce. In the script, item2 has instance data attributes set to Apples, 40, and May 5, 2012. The display() method is called, and  then the expiration date is printed using the get_expiration() method.interfaces 

 All of the class attributes of Item are available to instances of Produce, though instance attributes are not. The __init__ method of Item must be explicitly called in the constructor of Produce, Ex: `Item.__init__(self)`, so that the instance of Produce is assigned the name and quantity data attributes. When an instantiation of a Produce instance occurs, Produce.__init__() executes and immediately calls Item.__init__(). The newly created Produce instance is passed as the first argument (self) to the Item constructor, which creates the name and quantity attributes in the new Item instance's namespace. Item.__init__() returns, and Produce.__init__() continues, creating the expiration attribute. The following tool illustrates:

**PythonTutor: Derived class explicitly calls base class' constructor.**

```python
class Item:
    def __init__(self):
        self.name = ""
        self.quantity = 0

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.expiration = ""

item1 = Item()
item2 = Produce()
```

The term derived class refers to a class that inherits the class attributes of another class, known as a base class. Any class may serve as a base class; no changes to the definition of that class are required. The derived class is said to *inherit* the attributes of its base class, a concept called inheritance. An instance of a derived class type has access to all the attributes of the derived class as well as the *class* attributes of the base class by default, including the base class's methods. A derived class instance can simulate inheritance of *instance* attributes as well by calling the base class constructor manually. The following animation illustrates the relationship between a derived class and a base class.

### PARTICIPATION ACTIVITY: Derived class example: Produce derived from Item.

Static Figure: Begin Python code: 
item1 = Item()
item2 = Produce()

# ...
End Python code. Produce is derived from Item. item1 has access to name, quantity, display(), set_name(), set_quantity(). item2 has access to name, quantity, expiration, display(), set_name(), set_quantity(), get_expiration(), set_expiration().
Step 1: Item is the base class. The line of code item1 = Item() is highlighted. item1 has access to name, quantity, display(), set_name(), set_quantity().
Step 2: Produce is derived so Produce inherits Item's attributes. The line of code item2 = Produce() is highlighted. item2 has access to name, quantity, expiration, display(), set_name(), set_quantity(), get_expiration(), set_expiration().

The inheritance relationship is commonly drawn as follows, using Unified Modeling Language (UML) notation (Wikipedia: UML).

### PARTICIPATION ACTIVITY: UML derived class example: Produce derived from Item.

Static figure: Item has public data members name, quantity, and public methods set_name(), set_quantity(), display(). Produce is derived from Item and has the same data members and methods along with additional public data members expiration, and public methods set_expiration(), and get_expiration(). In UML, member access is described by  -, which means private, +, which means public and #, which means protected.
Step 1: A class diagram depicts a class' name, data members, and methods. The class name is Item. The data members are name and quantity and are public. The methods are set_name(), set_quantity(), and display(), and are public.
Step 2: A solid line with a closed, unfilled arrowhead indicates a class is derived from another class. Produce is derived from Item.
Step 3: The derived class shows only additional members. Produce has an additional data member expiration which is public. Produce has additional methods set_expiration() and get_expiration() which are public.

In the above animation, the +, -, and # symbols refer to the access level of an attribute. Ex: Whether or not that attribute can be accessed by anyone (public), only instances of that class (private), or instances derived from that class (protected), respectively. *In Python, all attributes are public.*privacy. Many languages, such as Java, C, and C++, explicitly require setting access levels on every variable and function in a class, thus UML as a language-independent tool includes the symbols.

Various class derivation variations are possible: 

- A derived class can itself serve as a base class for another class. In the earlier example, "class Fruit(Produce):" could be added.
- A class can serve as a base class for multiple derived classes. In the earlier example, "class Book(Item):" could be added.
- A class may be derived from multiple classes. For example, "class House(Dwelling, Property):" could be defined.

### PARTICIPATION ACTIVITY: Interactive inheritance tree.

Inheritance tree: Item is the base class. Produce and Book are derived classes of Item. Dairy and Fruit are derived classes of Produce. Textbook and Audiobook are derived classes of Book.

Item Class Pseudocode:

    Methods: 


            - def set_name(self, nm):
            - def set_quantity(self, qnty):
            - def display(self):

    Data Attributes:


            - self.name
            - self.quantity

Produce Class Pseudocode:

    Methods: 


            - All methods of the Item class are inherited.
            - def set_expiration(self, expir):
            - def get_expiration(self):

    Data Attributes:


            - All data attributes of the Item class are inherited.
            - self.expiration

Book Class Pseudocode:

    Methods: 


            - All methods of the Item class are inherited.
            - def set_title(self, ttl):
            - def get_title(self):

    Data Attributes:


            - All data attributes of the Item class are inherited.
            - self.title

Produce Class Pseudocode:

    Methods: 


            - All methods of the Produce class are inherited, including those inherited from the Item class.
            - def set_has_seeds(self, sds):
            - def get_has_seeds(self):

    Data Attributes:


            - All data attributes of the Produce class class are inherited, including those inherited from the Item class.
            - self.has_seeds

Dairy Class Pseudocode:

    Methods: 


            - All methods of the Produce class are inherited, including those inherited from the Item class.
            - def set_percent_fat(self, percent_fat):
            - def get_percent_fat(self):

    Data Attributes:


            - All data attributes of the Produce class class are inherited, including those inherited from the Item class.
            - self.percent_fat

Textbook Class Pseudocode:

    Methods: 


            - All methods of the Book class are inherited, including those inherited from the Item class.
            - def set_edition(self, edition):
            - def get_edition(self):

    Data Attributes:


            - All data attributes of the Book class class are inherited, including those inherited from the Item class.
            - self.edition

Audiobook Class Pseudocode:

    Methods: 


            - All methods of the Book class are inherited, including those inherited from the Item class.
            - def set_reader(self, reader):
            - def get_reader(self):

    Data Attributes:


            - All data attributes of the Book class class are inherited, including those inherited from the Item class.
            - self.reader

### PARTICIPATION ACTIVITY: Derived classes basics.

**1.** A class that can serve as the basis for another class is called a _______ class.
Answer: `     base     `
*Hint: There are base classes and derived classes.*
*Derived classes inherit from base classes.*

**2.** Class "Dwelling" has the method open_door(). Class "House" is derived from Dwelling and has the methods open_window() and open_basement(). After `h = House()` executes, how many different methods can h call, ignoring constructors?
Answer: 3
*Hint: House is derived from Dwelling, and can thus access methods defined by Dwelling.*
*h can access open_door() defined by Dwelling, and open_window() and open_basement() defined by House.*

### CHALLENGE ACTIVITY: Derived classes.

**Level 1:**

What is the output?

```python
class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)

class Car(Vehicle):
    def print_car_speed(self):
        print("Driving at: ", end = "")
        self.print_speed()

myCar = Car()
myCar.set_speed(25)
myCar.print_car_speed()
```

*Car inherits Vehicle. Member method print_speed() of the base class Vehicle can be accessed by the derived class Car.*

**Level 2:**

What is the output?

```python
class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)

class Car(Vehicle):
    def print_car_speed(self):
        print("Driving at: ", end = "")
        self.print_speed()

class AnimalPowered(Vehicle):
    def __init__(self):
        self.animal = ""

    def set_animal(self, animal_to_set):
        self.animal = animal_to_set

    def print_animal_speed(self):
        print(f"{self.animal} speed: ", end = "")
        self.print_speed()

myCar = Car()
chariot = AnimalPowered()

myCar.set_speed(20)
chariot.set_speed(3)
chariot.set_animal("Horse")

myCar.print_car_speed()
chariot.print_animal_speed()
```

*Car and AnimalPowered both inherit Vehicle. Multiple classes can inherit from a single base class.*

**Level 3:**

What is the output?

```python
class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)

class Car(Vehicle):
    def print_car_speed(self):
        print("Driving at: ", end = "")
        self.print_speed()

class ElectricCar(Car):
    def __init__(self):
        self.battery_level = 0

    def set_battery_level(self, level_to_set):
        self.battery_level = level_to_set

    def print_battery_level(self):
        print(f"Battery: {self.battery_level}")

myCar = ElectricCar()
myCar.set_speed(20)
myCar.set_battery_level(5)

myCar.print_car_speed()
myCar.print_battery_level()
```

*ElectricCar inherits Car, and Car inherits Vehicle. A class can inherit another class, which inherits yet another class.*

### CHALLENGE ACTIVITY: Defining a derived class. (3 Levels)

**Level 1:**

**Task:**
Complete the definition of class [...] so that [...] is derived from the base class [...].

**Explanation pattern:**
The definition of the derived class [...] begins with the keyword `class` followed by the class name [...] and the base class [...] enclosed in parentheses `()`.

**Code structure:**
```python
class ___:
    def __init__(self):
        self.___ = 0
        self.___ = 0

    def set____(self, ____value):
        self.___ = ____value

    def set____(self, ____value):
        self.___ = ____value

    def display(self):
        print(f"___")
""" Your code goes here """
def __init__(self):
        ___.__init__(self)

    def ___(self):
        print("___")

___

___ = ___()
___.set____(____value)
___.set____(____value)
___.___()
___.display()
```

**Level 2:**

**Task:**
Define the [...] class's \_\_init__ method to explicitly call the base class's \_\_init__ method.

**Explanation pattern:**
The definition of the derived class [...]'s \_\_init__ method begins with `def __init__(self):`. In the method, `[...].__init__(self)` is called.

**Code structure:**
```python
class ___:
    def __init__(self):
        self.___ = 0
        self.___ = 0

    def set____(self, ____value):
        self.___ = ____value

    def set____(self, ____value):
        self.___ = ____value

    def display(self):
        print(f"___")

class ___(___):
""" Your code goes here """
def print_title(self):
        print("___")

___

my_job = ___()
my_job.set____(____value)
my_job.set____(____value)
my_job.print_title()
my_job.display()
# First, run main.py as usual
import main

# Next, mock the base class method to see if the method is called
import testmock
import unittest
from unittest.mock import patch
import contextlib
import io

# To implementer:
# 1. Update import to include the base class and derived class names
# 2. Update mock_method_name with 'main.{base_class}.{method_name}'
# 3. Update alert with '{base_class}.{method_name}(self)'

from main import ___, ___   # Update 1

mock_method_name = 'main.___.__init__'   # Update 2
alert = '___.__init__(self) may not be called'   # Update 3

DEBUG = False

class Test___(unittest.TestCase):
    # Mock the base class method as mock_parent_init.
    # After creating the derived class instance, check that mock_parent_init has been called with my_instance.
    @patch(mock_method_name)
    def test_init_called(self, mock_parent_init):
        mock_parent_init.return_value = None
        print('Start unittest')
        my_instance = ___()
        mock_parent_init.assert_called_with(my_instance)
        print('End unittest')

    @patch(mock_method_name)
    def test_super_init_called(self, mock_parent_init):
        mock_parent_init.return_value = None
        print('Start unittest')
        my_instance = ___()
        mock_parent_init.assert_called_with()
        print('End unittest')

    def test_init_defined(self):
        print('Start unittest')
        self.assertIsNot(___.__init__, ___.__init__)
        print('End unittest')

# unittest uses stderr by default. Redirect stderr to buf
with io.StringIO() as buf:
    with contextlib.redirect_stdout(buf):
        # Create test suite. Only one test needed
        suite = unittest.TestSuite()
        suite.addTest(Test___("test_init_called"))
        suite.addTest(Test___("test_super_init_called"))
        suite.addTest(Test___("test_init_defined"))
        # Redirect all stdout from the tests to buf
        unittest.TextTestRunner(stream=buf).run(suite)

    tests_output = buf.getvalue()

    if 'FAIL: test_init_called' in tests_output and 'FAIL: test_super_init_called' in tests_output:
        print(alert)
    if 'FAIL: test_init_defined' in tests_output:
        print('Derived class missing __init__()')
```

**Level 3:**

**Task:**
Complete the definition of the [...] class as follows: - The [...] class is derived from the [...] class.
- The [...] class's \_\_init__ method explicitly calls the [...] class's \_\_init__ method and then initializes the instance attribute named id with value 0.

**Explanation pattern:**
The definition of the [...] class begins with `class [...]([...]):` to indicate that the [...] class is derived from the [...] class. In the [...] class, the \_\_init__ method is defined. In the \_\_init__ method, `[...].__init__(self)` is called. Then, `self.id = 0` initializes the instance attribute named id with value 0.

**Code structure:**
```python
class ___:
    def __init__(self):
        self.___ = 0
        self.___ = 0

    def set____(self, ____value):
        self.___ = ____value

    def set____(self, ____value):
        self.___ = ____value

    def display(self):
        print(f"___")
""" Your code goes here """
def set_id(self, id_value):
        self.id = id_value

    def display_id(self):
        print(f"___{self.id}")

___

___ = ___()
___.display_id()

___.set____(____value)
___.set____(____value)
___.set_id(id_value)
___.display()
___.display_id()
# First, run main.py as usual
import main

# Next, mock the base class method to see if the method is called
import testmock
import unittest
from unittest.mock import patch
import contextlib
import io

# To implementer:
# 1. Update import to include the base class and derived class names
# 2. Update mock_method_name with 'main.{base_class}.{method_name}'
# 3. Update alert with '{base_class}.{method_name}(self)'

from main import ___, ___   # Update 1

mock_method_name = 'main.___.__init__'   # Update 2
alert = '___.__init__(self) may not be called'   # Update 3

DEBUG = False

class Test___(unittest.TestCase):
    # Mock the base class method as mock_parent_init.
    # After creating the derived class instance, check that mock_parent_init has been called with my_instance.
    @patch(mock_method_name)
    def test_init_called(self, mock_parent_init):
        mock_parent_init.return_value = None
        print('Start unittest')
        my_instance = ___()
        mock_parent_init.assert_called_with(my_instance)
        print('End unittest')

    @patch(mock_method_name)
    def test_super_init_called(self, mock_parent_init):
        mock_parent_init.return_value = None
        print('Start unittest')
        my_instance = ___()
        mock_parent_init.assert_called_with()
        print('End unittest')

    def test_init_defined(self):
        print('Start unittest')
        self.assertIsNot(___.__init__, ___.__init__)
        print('End unittest')

# unittest uses stderr by default. Redirect stderr to buf
with io.StringIO() as buf:
    with contextlib.redirect_stdout(buf):
        # Create test suite. Only one test needed
        suite = unittest.TestSuite()
        suite.addTest(Test___("test_init_called"))
        suite.addTest(Test___("test_super_init_called"))
        suite.addTest(Test___("test_init_defined"))
        # Redirect all stdout from the tests to buf
        unittest.TextTestRunner(stream=buf).run(suite)

    tests_output = buf.getvalue()

    if 'FAIL: test_init_called' in tests_output and 'FAIL: test_super_init_called' in tests_output:
        print(alert)
    if 'FAIL: test_init_defined' in tests_output:
        print('Derived class missing __init__()')
```

(*interfaces) For maximal simplicity and brevity in the example, we have used a set of methods that either set or return the value of an attribute. Such an interface to a class is commonly known as a getter/setter design pattern. In Python, the getter/setter interface is better replaced with simple attribute reference operations; e.g., instead of item1.set_name("Hot Pockets"), use item1.name = "Hot Pockets".

(*privacy) Python does have a way to support private variables through name mangling using double underscores in front of an identifier, such as *self.__data*. A private variable is used mostly as a way to prevent name collisions in inheritance trees instead of as a form of information hiding.