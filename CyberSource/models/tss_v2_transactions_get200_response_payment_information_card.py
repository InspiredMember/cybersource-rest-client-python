# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TssV2TransactionsGet200ResponsePaymentInformationCard(object):
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
        'suffix': 'str',
        'prefix': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'start_month': 'str',
        'start_year': 'str',
        'issue_number': 'str',
        'type': 'str',
        'account_encoder_id': 'str',
        'use_as': 'str'
    }

    attribute_map = {
        'suffix': 'suffix',
        'prefix': 'prefix',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'start_month': 'startMonth',
        'start_year': 'startYear',
        'issue_number': 'issueNumber',
        'type': 'type',
        'account_encoder_id': 'accountEncoderId',
        'use_as': 'useAs'
    }

    def __init__(self, suffix=None, prefix=None, expiration_month=None, expiration_year=None, start_month=None, start_year=None, issue_number=None, type=None, account_encoder_id=None, use_as=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformationCard - a model defined in Swagger
        """

        self._suffix = None
        self._prefix = None
        self._expiration_month = None
        self._expiration_year = None
        self._start_month = None
        self._start_year = None
        self._issue_number = None
        self._type = None
        self._account_encoder_id = None
        self._use_as = None

        if suffix is not None:
          self.suffix = suffix
        if prefix is not None:
          self.prefix = prefix
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year
        if issue_number is not None:
          self.issue_number = issue_number
        if type is not None:
          self.type = type
        if account_encoder_id is not None:
          self.account_encoder_id = account_encoder_id
        if use_as is not None:
          self.use_as = use_as

    @property
    def suffix(self):
        """
        Gets the suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Last four digits of the cardholder’s account number. This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder. 

        :return: The suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Last four digits of the cardholder’s account number. This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder. 

        :param suffix: The suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if suffix is not None and len(suffix) > 4:
            raise ValueError("Invalid value for `suffix`, length must be less than or equal to `4`")

        self._suffix = suffix

    @property
    def prefix(self):
        """
        Gets the prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        The description for this field is not available.

        :return: The prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        The description for this field is not available.

        :param prefix: The prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if prefix is not None and len(prefix) > 6:
            raise ValueError("Invalid value for `prefix`, length must be less than or equal to `6`")

        self._prefix = prefix

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Two-digit month in which the credit card expires. `Format: MM`. Possible values: 01 through 12.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 12.  For processor-specific information, see the customer_cc_expmo field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Two-digit month in which the credit card expires. `Format: MM`. Possible values: 01 through 12.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 12.  For processor-specific information, see the customer_cc_expmo field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_month: The expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Four-digit year in which the credit card expires. `Format: YYYY`.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 2021.  For processor-specific information, see the customer_cc_expyr field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Four-digit year in which the credit card expires. `Format: YYYY`.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 2021.  For processor-specific information, see the customer_cc_expyr field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_year: The expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def start_month(self):
        """
        Gets the start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_month: The start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if start_month is not None and len(start_month) > 2:
            raise ValueError("Invalid value for `start_month`, length must be less than or equal to `2`")

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_year: The start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if start_year is not None and len(start_year) > 4:
            raise ValueError("Invalid value for `start_year`, length must be less than or equal to `4`")

        self._start_year = start_year

    @property
    def issue_number(self):
        """
        Gets the issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  The issue number is not required for Maestro (UK Domestic) transactions. 

        :return: The issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  The issue number is not required for Maestro (UK Domestic) transactions. 

        :param issue_number: The issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if issue_number is not None and len(issue_number) > 5:
            raise ValueError("Invalid value for `issue_number`, length must be less than or equal to `5`")

        self._issue_number = issue_number

    @property
    def type(self):
        """
        Gets the type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :return: The type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :param type: The type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        #if type is not None and len(type) > 3:
            #raise ValueError("Invalid value for `type`, length must be less than or equal to `3`")

        self._type = type

    @property
    def account_encoder_id(self):
        """
        Gets the account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Identifier for the issuing bank that provided the customer’s encoded account number. Contact your processor for the bank’s ID. 

        :return: The account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._account_encoder_id

    @account_encoder_id.setter
    def account_encoder_id(self, account_encoder_id):
        """
        Sets the account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Identifier for the issuing bank that provided the customer’s encoded account number. Contact your processor for the bank’s ID. 

        :param account_encoder_id: The account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if account_encoder_id is not None and len(account_encoder_id) > 3:
            raise ValueError("Invalid value for `account_encoder_id`, length must be less than or equal to `3`")

        self._account_encoder_id = account_encoder_id

    @property
    def use_as(self):
        """
        Gets the use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  **Cielo** and **Comercio Latino**  Possible values:   - CREDIT: Credit card  - DEBIT: Debit card  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet. 

        :return: The use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  **Cielo** and **Comercio Latino**  Possible values:   - CREDIT: Credit card  - DEBIT: Debit card  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet. 

        :param use_as: The use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """
        if use_as is not None and len(use_as) > 2:
            raise ValueError("Invalid value for `use_as`, length must be less than or equal to `2`")

        self._use_as = use_as

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other