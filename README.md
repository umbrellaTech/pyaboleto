# Python Yet Another Boleto - pyaboleto
O pyaboleto e um componente de boleto bancario em Python que oferece um conjunto de classes para gerar os dados dos
boletos e não os templates. O pyaboleto é uma reescrita do YaBoleto PHP desenvolvido pela umbrelaTech.

## Instalação
```bash
pip install pyaboleto
```
## Bancos suportados
Atualmente o pyaboleto funciona com os seguintes bancos:


| **Banco**              | **Implementado** | **Testado** |  **Homologado** |
| ---------------------- | ---------------- | ----------- |  -------------- |
| **Banco do Brasil**[1] | Não              | Não         |  Não            |
| **Banrisul**           | Não              | Não         |  Não            |
| **Bradesco**           | Não              | Não         |  Não            |
| **Caixa Economica**    | Não              | Não         |  Não            |
| **HSBC**               | Não              | Nao         |  Não            |
| **Itaú**               | **Sim**          | **Sim**     |  Não            |
| **Real**               | Não              | Não         |  Não            |
| **Santander**          | Não              | Não         |  Não            |

[1] Convênios com 7 dígitos

Demo
----------
```python
# -*- coding: utf-8 -*-
from pyaboleto.itau import *


end = Endereco('59064-520', 'Endereço', 'Nº', 'Complemento', 'Bairro', 'Cidade', 'UF', 'Pais')
sac = Sacado('Nome do cidadão', '999.999.999-99', end, '999999 SSP/UF')
ced = Cedente('Nome empresa', '02.952.192/0001-61', end)
con = Convenio('123456', '109', banco_itau, '9314-9', '32857-7')
bol = ItauBoleto('07006700', date(2015, 7, 6), 34.75, con, ced, sac)

print(bol.campo_livre)
print(bol.codigo_barras)
print(bol.linha_digitavel)
```

Contribua
----------

Toda contribuição é bem vinda. Se você deseja adaptar o pyaboleto a algum outro banco, fique à vontade para
explorar o código. Para implementar as direnças do seu banco, normalmente basta extender da classe pyaboleto.Boleto
e sobreescrever os métodos _validar_codigo_barras e campo_livre.

```bash
git clone https://github.com/umbrellaTech/pyaboleto.git
cd pyaboleto
```

Licença
----------
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
