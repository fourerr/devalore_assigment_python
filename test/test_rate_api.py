import pytest

from devalore.api import all_currency_names_rate_lower_10_real_data


def test_rate_api_real():
	with pytest.raises(AttributeError) as exe:
		all_currency_names_rate_lower_10_real_data()
	assert "dict" in str(exe.value)
