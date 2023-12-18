#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes:");
    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    for (i = 0; i < size && i < 10; ++i)
    {
        printf(" %02x", string[i] & 0xff);
    }

    printf("\n");
}

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject representing a Python list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyVarObject *)p)->ob_size);

    for (i = 0; i < size; ++i)
    {
        printf("Element %ld: ", i);

        if (PyBytes_Check(PyList_GetItem(p, i)))
        {
            print_python_bytes(PyList_GetItem(p, i));
        }
        else if (PyFloat_Check(PyList_GetItem(p, i)))
        {
            printf("[.] float object info\n");
            printf("  value: %f\n", PyFloat_AsDouble(PyList_GetItem(p, i)));
        }
        else if (PyTuple_Check(PyList_GetItem(p, i)) || PyList_Check(PyList_GetItem(p, i)))
        {
            print_python_list(PyList_GetItem(p, i));
        }
        else if (PyLong_Check(PyList_GetItem(p, i)))
        {
            printf("int\n");
        }
        else if (PyUnicode_Check(PyList_GetItem(p, i)))
        {
            printf("str\n");
        }
        else
        {
            printf("[ERROR] Invalid List Object\n");
        }
    }
}

/**
 * print_python_float - Print information about Python float object
 * @p: PyObject representing a Python float object
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj = (PyFloatObject *)p;

    if (!PyFloat_Check(p))
    {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}
