# SeparadorEmPastas
O código separa_test_validation_train.py irá pegar os arquivos da pasta "imagens" e a planilha nomeada "metadata.xlsx" com a coluna 'img_id' com os nomes dos arquivos da pasta imagens e a coluna 'diagnostic' com os diagnósticos.

A partir disso irá adicionar o diagnóstico ao nome dos arquivos de imagens e colocá-los na pasta "destino".

Ele irá contar quantas imagens tem de cada diagnóstico e dividir em 70% para a pasta "train", 15% para a pasta "validation" e 15% para a pasta "test".

Após direcionar as imagens para as pastas, irá informar quantas imagens de cada diagnóstico tem em cada pasta, se a quantidade não for exata, irá deixar as sobras do lado de fora.

Exemplo 1:

Utilizando as imagens do PADUFES20:

Quantidade de imagens por diagnóstico:
ACK: 730
BCC: 845
MEL: 52
NEV: 244
SCC: 192
SEK: 235

Distribuição final das imagens por conjunto e diagnóstico:

Train:
  SEK: 164 imagens
  BCC: 591 imagens
  SCC: 134 imagens
  ACK: 510 imagens
  NEV: 170 imagens
  MEL: 36 imagens

Validation:
  SEK: 35 imagens
  BCC: 126 imagens
  SCC: 28 imagens
  ACK: 109 imagens
  NEV: 36 imagens
  MEL: 6 imagens

Test:
  SEK: 35 imagens
  BCC: 126 imagens
  SCC: 28 imagens
  ACK: 109 imagens
  NEV: 36 imagens
  MEL: 10 imagens

Exemplo 2:
Utilizando as imagens do HAM10000:

Quantidade de imagens por diagnóstico:
bkl: 1099
nv: 6705
df: 115
mel: 1113
vasc: 142
bcc: 514
akiec: 327
Distribuição final das imagens por conjunto e diagnóstico:

Train:
  bkl: 769 imagens
  nv: 4693 imagens
  df: 80 imagens
  mel: 779 imagens
  vasc: 99 imagens
  bcc: 359 imagens
  akiec: 228 imagens

Validation:
  bkl: 164 imagens
  nv: 1005 imagens
  df: 17 imagens
  mel: 166 imagens
  vasc: 21 imagens
  bcc: 77 imagens
  akiec: 49 imagens

Test:
  bkl: 164 imagens
  nv: 1005 imagens
  df: 17 imagens
  mel: 166 imagens
  vasc: 21 imagens
  bcc: 77 imagens
  akiec: 49 imagens

Como podem observar, eles contém abreviações diferentes para os mesmos diagnósticos, e ele seque as classificações da planilha, não precisando renomear e padronizar, somente indicando o nome da coluna "diagnostic".
