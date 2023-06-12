#include <stdio.h>
#include "Python.h"
/**
 * print_python_list_info - prints info about a python list
 * @p: list object
 */
void print_python_list_info(PyObject *p)
{
    int i;
    PyListObject *pp;
    /*
     * lists in python are of the type PyListObject. PyObject is just a type
     * used to pass other types around. So you will need to cast your object back
     * to its oringinal type
     */
    pp = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
    printf("[*] Allocated = %ld\n", pp->allocated);

    for (i = 0; i < pp->ob_base.ob_size; i++)
    {
        printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);

    }
}
