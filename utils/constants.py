from dataclasses import dataclass
from enum import Enum

DEFAULT_WAIT = 10  # sec
BASE_URL = 'https://hb-autotests.stage.sirenltd.dev'


@dataclass
class SetUpProjectSelectItem:
    value: str
    automation_id: str


class ProjectTypes(Enum):
    REPLACEMENT = SetUpProjectSelectItem('Replacement/Installation', 'data-autotest-radio-projecttype-replacementorinstallation')
    REPAIR = SetUpProjectSelectItem('Repair', 'data-autotest-radio-projecttype-repair')
    NOT_SURE = SetUpProjectSelectItem('Not sure', 'data-autotest-radio-projecttype-replacementorinstallation-notsure')


class InvolvedEquipment(Enum):
    AIR_COND = SetUpProjectSelectItem('Air conditioner', 'data-autotest-checkbox-equipment-airconditioner')
    HEATING = SetUpProjectSelectItem('Central heating/furnace', 'data-autotest-checkbox-equipment-heatingorfurnace')
    BOILER = SetUpProjectSelectItem('Boiler/radiator', 'data-autotest-checkbox-equipment-boilerorradiator')
    HEAT_PUMP = SetUpProjectSelectItem('Heat pump', 'data-autotest-checkbox-equipment-heatpump')
    WATER_HEATER = SetUpProjectSelectItem('Water heater', 'data-autotest-checkbox-equipment-waterheater')
    NOT_SURE = SetUpProjectSelectItem('Not sure', 'data-autotest-checkbox-equipment-notsure')


class HVACResource(Enum):
    GAS = SetUpProjectSelectItem('Gas', 'data-autotest-radio-energysource-gas')
    ELECTRICITY = SetUpProjectSelectItem('Electricity', 'data-autotest-radio-energysource-electricity')
    PROPANE = SetUpProjectSelectItem('Propane', 'data-autotest-radio-energysource-propane')
    OIL = SetUpProjectSelectItem('Oil', 'data-autotest-radio-energysource-oil')
    NOT_SURE = SetUpProjectSelectItem('Not sure', 'data-autotest-radio-energysource-notsure')


class EquipmentAge(Enum):
    LESS_5 = SetUpProjectSelectItem('Less than 5 years', 'data-autotest-radio-equipmentage-5')
    FROM_5_TO_10 = SetUpProjectSelectItem('5 to 10 years', 'data-autotest-radio-equipmentage-10')
    MORE_10 = SetUpProjectSelectItem('Older than 10 years', 'data-autotest-radio-equipmentage-10plus')
    NOT_SURE = SetUpProjectSelectItem('Not sure', 'data-autotest-radio-equipmentage-notsure')


class PropertyType(Enum):
    DETACHED = SetUpProjectSelectItem('Detached, semi-detached, row house', 'data-autotest-radio-propertytype-detached')
    MOBILE = SetUpProjectSelectItem('Mobile, modular, manufactured home', 'data-autotest-radio-propertytype-mobile')
    COMMERCIAL = SetUpProjectSelectItem('Commercial', 'data-autotest-radio-propertytype-commercial')
    APARTMENT = SetUpProjectSelectItem('Apartment building or condominium', 'data-autotest-radio-propertytype-apartment')


class AuthorizedOrOwner(Enum):
    YES = SetUpProjectSelectItem('Yes', 'data-autotest-radio-owner-yes')
    NO = SetUpProjectSelectItem('No', 'data-autotest-radio-owner-no')
