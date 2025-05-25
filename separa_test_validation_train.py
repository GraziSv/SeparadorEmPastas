#Separador de imagens por train, validation e test#
#Para utilizar este código, tenha na pasta as imagens em .png na pasta "imagens", o arquivo "metadata.xlsx" com a coluna 'img_id' com os nomes das imagens e a coluna "diagnostic"
import os
import shutil
import pandas as pd
import random
from collections import Counter

# Função para renomear imagens sem movê-las para subpastas
def processar_imagens(excel_path, imagens_dir, destino_dir):
    # Carregar o arquivo Excel
    df = pd.read_excel(excel_path)

    # Verifique se o DataFrame tem as colunas corretas
    if 'img_id' not in df.columns or 'diagnostic' not in df.columns:
        print("Erro: O arquivo Excel deve conter as colunas 'img_id' e 'diagnostic'.")
        return

    # Criar a pasta destino se não existir
    if not os.path.exists(destino_dir):
        os.makedirs(destino_dir)

    # Contador para armazenar a quantidade de imagens por diagnóstico
    contador = Counter()

    # Iterar sobre as imagens e renomeá-las
    for _, row in df.iterrows():
        img_id = row['img_id']  # img_id já contém a extensão .png
        diagnostico = row['diagnostic']
        
        # Caminho completo da imagem original
        imagem_path = os.path.join(imagens_dir, img_id)
        
        if os.path.exists(imagem_path):
            # Criar o novo nome do arquivo
            novo_nome = f"{diagnostico}_{img_id}"
            destino_path = os.path.join(destino_dir, novo_nome)
            
            # Mover e renomear a imagem
            shutil.move(imagem_path, destino_path)
            contador[diagnostico] += 1
            print(f"Movendo e renomeando {img_id} para {novo_nome}")
        else:
            print(f"Imagem {img_id} não encontrada em {imagens_dir}")
    
    # Exibir a contagem de imagens por diagnóstico
    print("\nQuantidade de imagens por diagnóstico:")
    for diagnostico, quantidade in contador.items():
        print(f"{diagnostico}: {quantidade}")

# Função para dividir os arquivos em train, validation e test
def dividir_datasets(destino_dir):
    # Criar pastas de destino
    datasets = {"train": 0.7, "validation": 0.15, "test": 0.15}
    for dataset in datasets.keys():
        os.makedirs(os.path.join(destino_dir, dataset), exist_ok=True)
    
    # Listar todas as imagens na pasta destino
    imagens = [img for img in os.listdir(destino_dir) if os.path.isfile(os.path.join(destino_dir, img))]
    diagnosticos = Counter([img.split('_')[0] for img in imagens])
    
    # Dicionário para armazenar a distribuição final
    distribucao_final = {"train": Counter(), "validation": Counter(), "test": Counter()}
    
    for diagnostico, total in diagnosticos.items():
        imagens_diagnostico = [img for img in imagens if img.startswith(diagnostico)]
        random.shuffle(imagens_diagnostico)
        
        num_train = max(int(total * 0.7), 10)
        num_test = max(int(total * 0.15), 10)
        num_validation = max(int(total * 0.15), 10)
        
        # Ajustar os limites caso ultrapassem o total disponível
        if num_train + num_test + num_validation > total:
            num_train = max(int(total * 0.7), 10)
            restante = total - num_train
            num_test = max(restante // 2, 10)
            num_validation = total - num_train - num_test
        
        train_files = imagens_diagnostico[:num_train]
        test_files = imagens_diagnostico[num_train:num_train + num_test]
        validation_files = imagens_diagnostico[num_train + num_test:num_train + num_test + num_validation]
        
        for file, dataset in zip([train_files, validation_files, test_files], ["train", "validation", "test"]):
            for img in file:
                shutil.move(os.path.join(destino_dir, img), os.path.join(destino_dir, dataset, img))
                distribucao_final[dataset][diagnostico] += 1
    
    # Exibir distribuição final
    print("\nDistribuição final das imagens por conjunto e diagnóstico:")
    for dataset, contagem in distribucao_final.items():
        print(f"\n{dataset.capitalize()}:")
        for diagnostico, quantidade in contagem.items():
            print(f"  {diagnostico}: {quantidade} imagens")

# Caminhos dos diretórios
caminho_excel = '/home/graziela/Área de trabalho/PADUFES20/metadata.xlsx'  # Ajuste o caminho
imagens_dir = '/home/graziela/Área de trabalho/PADUFES20/imagens'  # Ajuste o caminho
destino_dir = '/home/graziela/Área de trabalho/PADUFES20/destino'  # Ajuste o caminho

# Chamar a função para processar as imagens
processar_imagens(caminho_excel, imagens_dir, destino_dir)

# Chamar a função para dividir as imagens em train, validation e test
dividir_datasets(destino_dir)

#usar o comando:  /home/graziela/miniconda3/bin/python "/home/graziela/Área de trabalho/PADUFES20/tudojunto.py"
