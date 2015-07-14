# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'

from datetime import date

from pyaboleto import Endereco, Sacado, Cedente, Convenio


def test_all():
    test_base()
    test_itau()


if __name__ == "__main__":
    test_all()


def _test_padrao():
    end = Endereco('12345-123', 'Logradouro', 'Nº', 'Complemento', 'Bairro', 'Cidade', 'UF', 'Brasil')
    sac = Sacado('Nome do cidadão', '123.456.789-01', end, '123465 SSP/UF')
    ced = Cedente('Nome da empresa', '12.345.678/9012-34', end)
    return end, sac, ced


def test_base():
    from . import Boleto, Banco
    end, sac, ced = _test_padrao()
    con = Convenio('123456', '21', Banco('000', 'Banco Brasileiro'), '1234-5', '12345-6')
    bol = Boleto('123456789', date(2015, 12, 12), 123.45, con, ced, sac)

    bol._validar_codigo_barras()


def test_itau():
    from pyaboleto.itau import ItauBoleto, banco_itau
    end, sac, ced = _test_padrao()
    con = Convenio('123456', '109', banco_itau, '9314-9', '32857-7')
    bol = ItauBoleto('07006700', date(2015, 7, 6), 34.75, con, ced, sac)

    print(bol.campo_livre)
    print(bol.codigo_barras)
    print(bol.linha_digitavel)

