#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        list of lists of ints/floats: The resulting matrix.

    Raises:
        ValueError: If matrices are not compatible for multiplication.
        ImportError: If NumPy is not installed.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ImportError:
        raise ImportError("NumPy is required use 'pip install numpy'")
    except ValueError:
        raise ValueError("Matrix are not compatible for multiplication.")
