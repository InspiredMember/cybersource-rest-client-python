# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2paymentsOrderInformationAmountDetailsSurcharge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'str',
        'description': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'description': 'description'
    }

    def __init__(self, amount=None, description=None):
        """
        Ptsv2paymentsOrderInformationAmountDetailsSurcharge - a model defined in Swagger
        """

        self._amount = None
        self._description = None

        if amount is not None:
          self.amount = amount
        if description is not None:
          self.description = description

    @property
    def amount(self):
        """
        Gets the amount of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        The surcharge amount is included in the total transaction amount but is passed in a separate field to the issuer and acquirer for tracking. The issuer can provide information about the surcharge amount to the customer.  If the amount is positive, then it is a debit for the customer.\\ If the amount is negative, then it is a credit for the customer.  **NOTE**: This field is supported only for Visa Platform Connect (VPC) for Payouts. For CtV, the maximum string length is 8.  For processor-specific information, see the surcharge_amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The amount of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        The surcharge amount is included in the total transaction amount but is passed in a separate field to the issuer and acquirer for tracking. The issuer can provide information about the surcharge amount to the customer.  If the amount is positive, then it is a debit for the customer.\\ If the amount is negative, then it is a credit for the customer.  **NOTE**: This field is supported only for Visa Platform Connect (VPC) for Payouts. For CtV, the maximum string length is 8.  For processor-specific information, see the surcharge_amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param amount: The amount of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        :type: str
        """
        if amount is not None and len(amount) > 15:
            raise ValueError("Invalid value for `amount`, length must be less than or equal to `15`")

        self._amount = amount

    @property
    def description(self):
        """
        Gets the description of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        Merchant-defined field for describing the surcharge amount.

        :return: The description of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        Merchant-defined field for describing the surcharge amount.

        :param description: The description of this Ptsv2paymentsOrderInformationAmountDetailsSurcharge.
        :type: str
        """

        self._description = description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2paymentsOrderInformationAmountDetailsSurcharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
