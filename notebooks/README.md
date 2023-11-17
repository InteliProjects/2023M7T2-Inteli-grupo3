# Primeira arquitetura de pastas

notebooks/
|-- data/                           # Pasta para conter os dados
|   |-- base/                       # Dados brutos (não processados)
|   |-- processed/                  # Dados processados e prontos para modelagem
|       |-- exploratory_analysis/   # Dados processados a partir da análise exploratória
|       |-- feature_engineering/    # Dados processados a partir da engenharia de dados
|       |-- model_training/         # Dados processados a partir da modelagem treinada
|
|
|
|-- src/                            # Código-fonte do projeto
|   |-- feature_engineering/        # Scripts ou módulos para criação de novas features
|   |-- exploratory_analysis/       # Scripts ou módulos para seleção da análise exploratória
|   |-- model_training/             # Scripts ou módulos para treinamento de modelos
|
|-- models/                         # Modelos treinados
|
|-- README.md                       # REAME explicando a extrutura de bastas

## Notebooks

A pasta "notebooks" contempla toda a parte de de dados e codigos. Nela, encontramos a fonte dos dados, o processamento dos dados(engenharia e análise) e o modelo final ja treinado.

### Data

Nesta pasta será contida a base de dados. A subpasta "base" contem os dados brutos, sendo assim, os dados recebidos sem nenhuma alteração.

A subpasta "processed" representa os dados processados pela feature engineering, exploratory_analysis e pelo model_training.

### src

A pasta "src" contem a base da análise, nela encontramos os jupter notebooks de análise exploratória, de engenharia de dados e modelos de treinamento.

### Models

A pasta "models" contempla o modelo final. Apos todo o ciclo de análise, engenharia e treinamento, será criado um script contendo o modelo ja criado e funcionado.

## Boa praticas

### Arquivos

Os datasets gerados devem ser classificados de acordo com a versão. EXP:
- O primeiro Datasets gerados a partir da análise exploratoria devem ser salvos como "v1"
```
csv_v1.parquet
```
e as versões seguintes, dever seguir uma ordem Cronológico. EXP: 
- O quinto Datasets gerados a partir da análise exploratoria devem ser salvos como "v5"


```
csv_v5.parquet
```

Caso deseje mudar algo na estrutura de pastas, sinta-se à vontade para fazê-lo. A única coisa que seria importante é documentar a mudança e abrir um pull request.

<h2>Em Contrução...
