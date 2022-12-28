from __future__ import annotations


class UnitConverter:
    def __init__(self):
        self._pattern_mul = '{}*{}'
        self._pattern_div = '{}/{}'
        self._coefficients = {
            'po-kg': 0.453592,
            'in-cm': 2.54,
        }
        self._convert_units = {
            'po=>kg': self._pattern_mul,
            'kg=>po': self._pattern_div,
            'in=>cm': self._pattern_mul,
            'cm=>in': self._pattern_div,
        }

    def convert(self, first_unit: str, second_unit: str, value: int | float) -> int | float:

        coef_key = f'{first_unit}-{second_unit}'
        if self._coefficients.get(coef_key) is None:
            coef_key = f'{second_unit}-{first_unit}'

        conv_key = f'{first_unit}=>{second_unit}'

        coefficient = self._coefficients[coef_key]
        res = eval(self._convert_units[conv_key].format(value, coefficient))
        return round(res, 2)
