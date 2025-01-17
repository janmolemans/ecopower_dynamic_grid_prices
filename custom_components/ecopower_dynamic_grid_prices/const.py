"""Constants for the DynGridPrices integration."""

DOMAIN = "ecopower_dynamic_grid_prices"

#ENTSOE_DAYAHEAD_URL = "https://transparency.entsoe.eu/api?securityToken={TOKEN}&documentType=A44&in_Domain={AREA}&out_Domain={AREA}&periodStart={START}&periodEnd={END}"
ECOPWR_DAYAHEAD_URL_ACC = "https://acc.ameo.app/api/v2/characteristics/{CURVE}"
ECOPWR_DAYAHEAD_URL = "https://cloud.ameo.app/api/v2/characteristics/{CURVE}"

#ECOPWR_INJECTION_ACC = 590
#ECOPWR_CONSUMPTION_ACC = 622
#ECOPWR_CONSUMPTION_22_7_ACC = 624
#ECOPWR_CONSUMPTION_21_6_ACC = 623

#ENTSOE_HEADERS = {"Content-type": "application/xml; charset=UTF-8"}
ECOPWR_HEADERS = {"Content-type": "application/json; charset=UTF-8", "authorization": "Bearer {TOKEN}"}

ATTRIBUTION = '@infradom'

NAME = "EcopowerPrices"
DEFAULT_NAME = DOMAIN
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.7"
ISSUE_URL = "https://github.com/infradom/ecopower_dynamic_grid_prices/issues"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# configuration options

CONF_NAME            = "name"
CONF_ECOPWR_TOKEN    = "ecopower_token"
CONF_ECOPWR_API_C    = "api_id_cons"
CONF_ECOPWR_API_I    = "api_id_inj"
CONF_TEST_API        = "test_api"


SENSOR = "sensor"
PLATFORMS = [SENSOR]
ICON = "mdi:format-quote-close"


