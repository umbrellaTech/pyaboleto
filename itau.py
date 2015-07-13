# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright 2013 Umbrella Tech.

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


from . import *
import re

banco_itau = Banco('341', 'Banco Itaú')

class ItauBoleto(Boleto):
    """
    Gera o campo livre do código de barras.

    """

    @property
    def campo_livre(self):
        if not re.match('\d{3}', self.convenio.carteira):
            raise Exception('A carteira deve conter 3 digitos (000)')

        if not re.match('\d{4}\-\d', self.convenio.agencia):
            raise Exception('A agencia deve conter 4 digitos, 1 hífen e 1 dv (0000-0)')

        if not re.match('\d{5}\-\d', self.convenio.conta):
            raise Exception('A conta deve conter 5 digitos, 1 hífen e 1 dv (00000-0)')

        agencia_conta = "%4s%5s" % (self.convenio.agencia[:-2], self.convenio.conta[:-2])
        campo_livre = "%3s%s%1s%4s%5s%1s000" % (self.convenio.carteira,
                                                 self.nosso_numero,
                                                 modulo10("%s%3s%8s" %
                                                          (agencia_conta, self.convenio.carteira, self.nosso_numero)),
                                                 self.convenio.agencia[:-2],
                                                 self.convenio.conta[:-2],
                                                 modulo10(agencia_conta))
        return campo_livre


# def show_me():
end = Endereco('59064-520', 'Rua Senador José Ferreira de Souza', '1916', None, 'Candelária', 'Natal', 'RN')
sac = Sacado('Nome do cidadão', '999.999.999-99', end, '999999 SSP/UF')
ced = Cedente('Cabo Telecom', '02.952.192/0001-61', end)
con = Convenio('123456', '109', banco_itau, '9314-9', '32857-7')
bol = ItauBoleto('07006700', date(2015, 7, 6), 34.75, con, ced, sac)

print(bol.campo_livre)
print(bol.codigo_barras)
print(bol.linha_digitavel)