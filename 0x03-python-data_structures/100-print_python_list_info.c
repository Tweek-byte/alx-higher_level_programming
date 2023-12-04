#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: PyObject representing a Python list
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc;
	Py_ssize_t i;

	size = Py_SIZE(p);
	alloc = list->allocated;
	printf("[] Size of the Python List = %zd\n", size);
	printf("[] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
