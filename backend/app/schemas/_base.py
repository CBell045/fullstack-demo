"""
Base file for all pydantic models/schemas

This includes the custom BaseClass that all pydantic models should inherit from
"""

from pydantic import (
    BaseModel,
    ConfigDict,
)
from pydantic_extra_types.phone_numbers import PhoneNumber


class BaseClass(BaseModel):
    """Base class for all pydantic models/schemas"""

    model_config = ConfigDict(
        from_attributes=True,  # This allows us to use the model_dump method
    )


# Custom USPhoneNumber type
class USPhoneNumber(PhoneNumber):
    """
    Inherits from PhoneNumber and sets the default country code to US
    """

    default_region_code = "US"
    phone_format = "E164"
