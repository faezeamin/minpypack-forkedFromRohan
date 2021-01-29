## Minimal python packaging for local development

I have codes that are under development while also being used across multiple local projects that use custom environments (e.g. specified with `conda`).
 - I don't want to make copies of the code
 - appending paths through `sys.path.append()` is cumbersome, and will have to be cleaned up eventually if I'm sharing my code

 Using `pip` to install codes as a package locally is a clean solution. It also promotes better practices for eventually releasing codes. This repository is a minimal package showing how to structure code, write the setup file and complete the installation with pip in any local environment:
 
The parent `minpypack` directory contains a subfolder with the same name that contains all codes to use in multiple environments. The `setup.py` file contains installation instructions used by `pip`.

```bash
#minpypack directory structure:
└── minpypack
    ├── README.md
    ├── minpypack
    │   ├── A
    │   │   ├── A_file.py
    │   │   └── __init__.py
    │   ├── B
    │   │   ├── B_file.py
    │   │   └── __init__.py
    │   ├── C.py
    │   └── __init__.py
    └── setup.py
```

Some terminology:
 - `A` and `B` are (sub) packages (because they contain the `__init__.py` file).
 - `A_file.py`, `B_file.py`, `C.py` are modules - i.e. `.py` files containing functions and classes. 

⚠️ Only modules or the functions, classes inside of them can be imported [(explanation)](https://bytebaker.com/2008/07/30/python-namespaces/).

```python
#Valid ways of importing:
import SomeModule
from SomeModule import SomeFuncName, SomeClassName, etc.
from SomeModule import SomeFuncName as SomeOtherName
from SomeModule import *
```

Accordingly for our project:

🚫 This fails: 
```python
#Fails because B is not a module, but a package:
import minpypack.B as bb
bb.B_file.main() 
```

✅ These work:
```python
#Works because B_file is a module with function main:
import minpypack.B.B_file as bb
bpack.main() 

#Works because C is a module with function BfromC
import minpypack.C as cc
cc.BfromC()
```


Navigate to where the `setup.py` file is located. Install `minpypack` into current environment:
```bash
pip install -e .
```

Installation performed in this manner includes symbolic links to the files. 
 - 🛠 Changes to any `minpypack` source files are immediately available in all environments it is installed.
 - ⚠️ If `minpypack` folder is moved after installation, you will have to reinstall it. 

[`pip` also provides an easy way to install remote repositories]((https://pip.pypa.io/en/stable/reference/pip_install/)) e.g. private github repositories you have access to.
