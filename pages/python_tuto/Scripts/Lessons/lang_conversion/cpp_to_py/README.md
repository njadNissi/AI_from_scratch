2. Compilation Steps

Before Python can use this, it must be compiled into a "Shared Object" (.so on Linux/macOS) or a "Dynamic Link Library" (.dll on Windows).

Open your terminal in the cpp_to_py_demo folder.
Linux / macOS (using GCC or Clang)

Run this command:
Bash

```bash
    g++ -shared -fPIC -o mylib.so mylib.cpp
```

- g++: The compiler.

- shared: Create a shared library instead of an executable.

- fPIC: Position Independent Code (required for shared libraries on Linux/Mac).

- o mylib.so: The output filename.

Windows (using MinGW/GCC)
```bash
    g++ -shared -o mylib.dll mylib.cpp
```

Windows (using Visual Studio 'cl.exe')

If you are using the Visual Studio Developer Command Prompt:
DOS

```bash
    cl /LD mylib.cpp
```

(This will likely generate mylib.dll and mylib.lib)

3. The Python Code (run.py)

Now we use ctypes to load that compiled file and call the function inside.

Crucial Detail: You must tell ctypes the specific C data types the function expects as arguments and what type it returns. If you don't, it defaults to C integers, which might cause crashes if you later deal with floats or pointers.