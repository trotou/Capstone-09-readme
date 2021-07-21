# -*- coding: utf-8 -*-

"""
capstone

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CriarOperadorCaixaRequest(object):

    """Implementation of the 'Criar operador caixaRequest' model.

    TODO: type model description here.

    Attributes:
        id_operator (int): TODO: type description here.
        id_cashier (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id_operator": 'id_operator',
        "id_cashier": 'id_cashier'
    }

    def __init__(self,
                 id_operator=None,
                 id_cashier=None):
        """Constructor for the CriarOperadorCaixaRequest class"""

        # Initialize members of the class
        self.id_operator = id_operator
        self.id_cashier = id_cashier

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
        id_operator = dictionary.get('id_operator')
        id_cashier = dictionary.get('id_cashier')

        # Return an object of this model
        return cls(id_operator,
                   id_cashier)
