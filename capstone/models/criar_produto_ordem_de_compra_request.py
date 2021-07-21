# -*- coding: utf-8 -*-

"""
capstone

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CriarProdutoOrdemDeCompraRequest(object):

    """Implementation of the 'Criar produto ordem de compraRequest' model.

    TODO: type model description here.

    Attributes:
        id_order (int): TODO: type description here.
        id_product (int): TODO: type description here.
        quantity (int): TODO: type description here.
        cost (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id_order": 'id_order',
        "id_product": 'id_product',
        "quantity": 'quantity',
        "cost": 'cost'
    }

    def __init__(self,
                 id_order=None,
                 id_product=None,
                 quantity=None,
                 cost=None):
        """Constructor for the CriarProdutoOrdemDeCompraRequest class"""

        # Initialize members of the class
        self.id_order = id_order
        self.id_product = id_product
        self.quantity = quantity
        self.cost = cost

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id_order = dictionary.get('id_order')
        id_product = dictionary.get('id_product')
        quantity = dictionary.get('quantity')
        cost = dictionary.get('cost')

        # Return an object of this model
        return cls(id_order,
                   id_product,
                   quantity,
                   cost)
