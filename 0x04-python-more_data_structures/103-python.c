#include <Python.h>
#include <stdio.h>

void print_hexn(const char *str, int n)
{
    int i = 0;

    for (; i < n - 1; ++i)
        printf("%02x ", (unsigned char)str[i]);

    printf("%02x", str[i]);
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *clone = (PyBytesObject *)p;
    int new_size, csize = 0;

    printf("[.] bytes object info\n");
    if (PyBytes_Check(clone))
    {
        csize = PyBytes_Size(p);
        new_size = csize + 1;

        if (new_size >= 10)
            new_size = 10;

        printf("  size: %d\n", csize);
        printf("  trying string: %s\n", clone->ob_sval);
        printf("  first %d bytes: ", new_size);
        print_hexn(clone->ob_sval, new_size);
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p)
{
    int i = 0, ll = 0;
    PyObject *elem;
    PyListObject *clone = (PyListObject *)p;

    printf("[*] Python list info\n");
    ll = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %d\n", ll);
    printf("[*] Allocated = %zd\n", clone->allocated);

    for (; i < ll; ++i)
    {
        elem = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, elem->ob_type->tp_name);

        if (PyBytes_Check(elem))
            print_python_bytes(elem);
    }
}
