from .tensor import Tensor
from typing import Tuple
import numpy as np 


__all__ = ["dot", "rand", "zeros", "multiply" ,"tensor2strings"]


def dot(tensor1: Tensor, tensor2: Tensor) -> Tensor:
    """
        This static method defines the dot product.

        Args:
            tensor1: the first Tensor.
            tensor2: the second Tensor.

        Returns:
            A Tensor, the result of the dot product of tensor1 and tensor2.
    """

    if tensor1.shape[1] != tensor2.shape[1]:
        s1, s2 = tensor1.shape, tensor2.shape
        raise ValueError(f": shapes {s1} and {s2} not aligned: {s1[1]} != {s2[0]}")
    
    return Tensor(np.dot(tensor1, tensor2.T))


def rand(*shape: Tuple[int]) -> Tensor:
    """
        This static method creates a Tensor with random values.

        Args:
            shape: a tuple of integers, defining the shape of the Tensor.

        Returns:
            A Tensor.
    """

    return Tensor(np.random.rand(*shape))



def zeros(*shape: Tuple[int]) -> Tensor:
    """
        This static method creates a Tensor of zeros.

        Args:
            shape: a tuple of integers, defining the shape of the Tensor.

        Returns:
            A Tensor.
    """

    return Tensor(np.zeros(shape))


def multiply(tensor1: Tensor, tensor2: Tensor) -> Tensor:
    #TODO: write docstrings for multiply:
     
    return Tensor(np.multiply(tensor1, tensor2))


def tensor2strings(tensor: Tensor) -> str:
    return np.array2string(tensor)