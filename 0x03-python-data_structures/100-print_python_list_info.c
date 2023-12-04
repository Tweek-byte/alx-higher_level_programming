#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Print basic information about Python lists
 * @p: PyObject representing a Python list
 *
 * Return: None
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *) p;
    int size = Py_SIZE(p);
    int alloc = list->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (int i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
