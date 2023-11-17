# Documentação Modelo Preditivo - Inteli

## Mirai

### Grupo BlueBird

#### Antônio Ribeiro Cavalcante, Eduardo França Porto, Elisa de Oliveira Flemer, Felipe Campos, Filipe Kikuchi, Joao Carazzato e Patricia Honorato

## Sumário

- [Documentação Modelo Preditivo - Inteli](#documentação-modelo-preditivo---inteli)
  - [Mirai](#mirai)
    - [Grupo BlueBird](#grupo-bluebird)
      - [Antônio Ribeiro Cavalcante, Eduardo França Porto, Elisa de Oliveira Flemer, Felipe Campos, Filipe Kikuchi, Joao Carazzato e Patricia Honorato](#antônio-ribeiro-cavalcante-eduardo-frança-porto-elisa-de-oliveira-flemer-felipe-campos-filipe-kikuchi-joao-carazzato-e-patricia-honorato)
  - [Sumário](#sumário)
  - [Estrutura de pastas](#estrutura-de-pastas)
  - [Introdução](#introdução)
  - [Entendimento de negócio](#entendimento-de-negócio)
    - [Matriz de oceano azul](#matriz-de-oceano-azul)
    - [Matriz de riscos](#matriz-de-riscos)
    - [Persona](#persona)
    - [Canvas de proposta de valor](#canvas-de-proposta-de-valor)
    - [User stories](#user-stories)
    - [Análise financeira](#análise-financeira)
  - [Economia circular](#economia-circular)
  - [Requisitos do projeto](#requisitos-do-projeto)
    - [Requisitos funcionais](#requisitos-funcionais)
    - [Requisitos não funcionais](#requisitos-não-funcionais)
    - [Viabilidade técnica](#viabilidade-técnica)
  - [Proposta geral do sistema](#proposta-geral-do-sistema)
  - [Arquitetura da Solução](#arquitetura-da-solução)
  - [Frontend](#frontend)
  - [Interface](#interface)
  - [Visualização de dados](#visualização-de-dados)
  - [Arquitetura de dados](#arquitetura-de-dados)
    - [Descrição dos dados recebidos](#descrição-dos-dados-recebidos)
  - [Machine learning](#machine-learning)
    - [Sprint 2](#sprint-2)
      - [Descrição da transformação dos dados](#descrição-da-transformação-dos-dados)
      - [Processamento e Preparação dos dados](#processamento-e-preparação-dos-dados)
      - [Modelagem e Resultados](#modelagem-e-resultados)
    - [Classifier on regressor](#classifier-on-regressor)
      - [Pré-processamento](#pré-processamento)
      - [Feature engineering](#feature-engineering)
      - [Treinamento](#treinamento)
        - [Time series](#time-series)
        - [Classificador](#classificador)
    - [Treinamento com dados balanceados](#treinamento-com-dados-balanceados)
      - [Regressão](#regressão)
    - [Análise exploratória para o modelo de agreggator com pycaret](#análise-exploratória-para-o-modelo-de-agreggator-com-pycaret)
      - [Origem dos dados](#origem-dos-dados)
      - [Pré-processamento dos Dados](#pré-processamento-dos-dados)
      - [Análises](#análises)
      - [Análises subsequentes e conclusões](#análises-subsequentes-e-conclusões)
    - [**Agreggator com pycaret**](#agreggator-com-pycaret)
    - [Exponential Smoothing Simples](#exponential-smoothing-simples)
    - [**Classificação com o PyCaret**](#classificação-com-o-pycaret)
      - [1ª Etapa : Preparação dos dados](#1ª-etapa--preparação-dos-dados)
      - [2ª Etapa: Criação da coluna  alvo](#2ª-etapa-criação-da-coluna-alvo)
      - [3ª Etapa : Criando o modelo](#3ª-etapa--criando-o-modelo)
  - [Tecnologias selecionadas](#tecnologias-selecionadas)
    - [Frontend](#frontend-1)
    - [Backend](#backend)
    - [Armazenamento de dados](#armazenamento-de-dados)
    - [Machine learning](#machine-learning-1)
  - [Próximos passos](#próximos-passos)
  - [Referências](#referências)

## Estrutura de pastas

```
├───ambientes (venv)
├───api (backend mockado para utilizar Prisma na POC)
├───backend (backend para Pocketbase)
├───documentos (documentação)
├───frontend (interface gráfica em Next.js)
│   ├───app
│   ├───context
│   └───public
├───machine-learning (scripts derivados dos notebooks)
└───notebooks (notebooks para pré-processamento, feature engineering e treinamento)
    ├───agregator
    ├───data
    ├───exploratory_analysis
    ├───feature_engineering
    ├───models
    ├───model_training
```

## Introdução

O projeto do módulo 7 de Engenharia da Computação consiste na criação de sistema de manutenção preditiva para a empresa Azul, a maior companhia aérea brasileira e reconhecida como a melhor do mundo pelo TripAdvisor. Atualmente, as manutenções preventivas das aeronaves da Azul são baseadas em avaliações subjetivas dos técnicos de manutenção, que analisam manualmente os dados das aeronaves para decidir quando realizar uma manutenção. Esse processo, além de não ser escalável, pode levar a atrasos de voos e aumento no consumo de combustível caso ocorram falhas durante o voo.

O objetivo principal do projeto é superar essas limitações através da implementação de um sistema de manutenção preditiva para o sistema de bleed das aeronaves. O sistema utilizará técnicas avançadas de análise de dados, aprendizado de máquina e inteligência artificial para identificar padrões e anomalias nos dados operacionais das aeronaves. Essa abordagem permitirá prever com maior precisão os momentos ideais para realizar a manutenção, evitando falhas inesperadas durante os voos.

A implantação desse sistema trará diversos benefícios significativos para a Azul. Além de aumentar a confiabilidade das operações aéreas, reduzirá os atrasos nos voos e otimizará o consumo de combustível, contribuindo para a economia de recursos financeiros e a melhoria da experiência dos passageiros. Além disso, a escalabilidade do sistema permitirá que a Azul gerencie eficientemente sua frota de aeronaves, maximizando a disponibilidade e a eficiência operacional.

## Entendimento de negócio

Nesta seção, adotamos uma abordagem abrangente, começando pela análise de riscos por meio de uma matriz de riscos, seguida pela exploração das oportunidades estratégicas com a Matriz do Oceano Azul. Além disso, desenvolvemos personas para compreender as necessidades dos stakeholders e utilizamos o Canvas de Proposta de Valor para definir os benefícios tangíveis e intangíveis da implementação do sistema, garantindo uma base sólida para as etapas subsequentes do projeto.

### Matriz de oceano azul

Fundada em 2008, a Azul Linhas Aéreas Brasileiras é uma proeminente companhia aérea de baixo custo no Brasil. Com uma rede extensa de voos, tanto domésticos quanto internacionais, a companhia opera uma frota atualizada que inclui aeronaves da Embraer e Airbus. Conhecida por seus preços acessíveis, a Azul não compromete a qualidade, oferecendo serviços como refeições gratuitas em voos de longa distância, entretenimento a bordo e assentos aconchegantes. Além de seu serviço de passageiros, a Azul também gerencia cargas e correios e mantém aeronaves por meio de sua subsidiária, Azul Viagens. Liderando o mercado brasileiro, a Azul atende a 158 destinos, realizando o maior número de decolagens diárias e mantendo uma malha aérea versátil.

Atualmente, visando atingir seu compromisso com a excelência técnica, a Azul busca resolver um problema pertinente ligado ao consumo elevado de combustível. Esse desafio emerge das falhas no sistema de Bleed dos motores das aeronaves Embraer E2, forçando a operação em altitudes menores, onde o ar mais denso aumenta a resistência e, consequentemente, o consumo de combustível. Com o intuito de superar esse obstáculo, em parceria com o Inteli - Instituto de Liderança e Tecnologia, a companhia está apoiando um projeto de desenvolvimento de uma machine learning para detecção de degradação nos componentes críticos do sistema Bleed.

**Custo**: custo de implementação da solução;

**Velocidade de feedback**: velocidade com que se determina a necessidade de realizar uma manutenção, partindo da análise do sistema de bleed até a conclusão;

**Dashboard**: existência de um dashboard com dados do sistema;

**Segurança**: trata-se da segurança do processo em relação ao trabalhadores, que, atualmente, precisam verificam o sistema pessoalmente para avaliar a necessidade de uma manutenção;

**Custos desnecessários**: refere-se ao investimento em atividades desnecessárias ou minimamente urgentes. Para abordar essa questão, o projeto se baseia em um modelo de tomada de decisão altamente preciso. Esse modelo estipula que as manutenções preditivas sejam realizadas somente quando os indicadores apontarem de forma positiva, garantindo que, ao seguir essa indicação, haja convicção na real necessidade de intervenção. Como resultado direto dessa abordagem, observa-se uma redução considerável dos gastos evitáveis.

**Precisão**: No contexto das manutenções preditivas, a "precisão" refere-se à confiabilidade das intervenções realizadas. Essa medida é calculada como a proporção de Verdadeiros Positivos em relação aos resultados classificados como positivos. O projeto visa atingir uma alta precisão, acionando manutenções preditivas somente quando há confiança substancial na sua necessidade.

**Mão de obra**: Quantidade de pessoas que são necessárias para realizar uma manutenção preditiva;

**Comercialização**: Possibilidade de vender a solução para outras empresas.

![](./outros/matriz_oceano_azul.png)

### Matriz de riscos

A matriz de riscos é uma ferramenta essencial na avaliação e gestão de potenciais desafios em um projeto. Ela envolve a identificação, classificação e análise dos diversos riscos que podem impactar o sucesso do empreendimento. Por meio dessa matriz, os riscos são geralmente categorizados com base na probabilidade de ocorrência e no impacto que podem causar. Ao fornecer uma visão abrangente das possíveis incertezas e ameaças, a matriz de riscos permite que sejam adotadas estratégias adequadas para mitigar, monitorar ou responder a cada risco, garantindo a tomada de decisões mais informadas e a implementação de medidas preventivas eficazes.

![](./outros/matrizDeRiscos.png)

Seguem abaixo cada risco com sua possível mitigação e/ou potencialização:

**Falha na leitura dos dados**: Implementar uma pipeline de pré-processamento capaz de lidar com dados faltantes através de fill-forward e média entre valores recentes.

**Demora do parceiro fornecer os dados necessários**: Estabelecer um plano de comunicação regular e prazos definidos para a obtenção dos dados, incentivando uma colaboração mais eficiente.

**Falha em criar um modelo com uma boa acurácia**: Realizar uma análise detalhada dos algoritmos e métodos de aprendizado de máquina, ajustando-os e refinando-os iterativamente para alcançar os resultados desejados com o auxílio dos professores a cada sprint.

**Conflito de merge no GIT**: Adotar práticas de gerenciamento de código como revisões de código, branchs separados para desenvolvimento e testes, e um processo de merge bem definido.

**Ausência de membros**: Criar um plano de contingência com papéis e responsabilidades claras, além de treinamento cruzado para garantir que o projeto continue mesmo na ausência de um membro.

**Falta de comunicação**: Estabelecer canais de comunicação regulares, como as dailies e o próprio Slack, além de uma cultura de colaboração forte.

**Incerteza com a expectativa dos entregáveis**: Discutir requisitos claros e objetivos para cada entregável com o orientador, com revisões regulares para garantir que as expectativas estejam alinhadas.

**Viés na análise dos dados**: Implementar práticas rigorosas de análise, incluindo revisões por pares e validações cruzadas, para minimizar a introdução de viés nos resultados.

**O MVP ser adotado pelo parceiro**: Maior motivação para a turma como um todo para os próximos módulos.

**Aumento significativo na identificação de falhas nos componentes**: Satisfação de nosso parceiro com as interações para com o Inteli.

![](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/Matriz_de_risco.png?raw=true)

### Persona

![](./outros/persona.png)

Nesta seção, mergulhamos na compreensão detalhada das necessidades, características e perspectivas dos principais envolvidos no projeto. Por meio da criação de personas cuidadosamente elaboradas, buscamos personificar os diversos perfis de usuários, stakeholders e membros da equipe. Essas personas proporcionam uma visão aprofundada das expectativas e desafios enfrentados por cada grupo, orientando o processo de design e tomada de decisões de forma centrada no usuário e alinhada aos objetivos estratégicos do projeto.

**Nome:** Marcela Rocha  
**Idade:** 38 anos  
**Ocupação:** Gerente de Operações de Manutenção na Azul Linhas Aéreas  
**Formação:** Bacharel em Administração de Empresas com foco em Gestão de Transportes  
**Experiência Profissional:** Trabalhou por mais de 10 anos na indústria da aviação, começando como assistente de planejamento de manutenção e avançando para o cargo atual de Gerente de Operações de Manutenção na Azul.

**Histórico e Motivação:**  
Marcela é apaixonada por aviação desde criança, e seu sonho de trabalhar na indústria se tornou realidade quando ingressou na Azul Linhas Aéreas. Sua carreira foi marcada por sua capacidade de tomar decisões inteligentes e eficazes em situações críticas. Ela entende a importância de manter as aeronaves funcionando perfeitamente para garantir a segurança dos passageiros e o sucesso operacional da empresa.

**Hobbies e Interesses:**  
Nos finais de semana, Marcela gosta de praticar ciclismo e fazer trilhas na natureza. Ela também é uma ávida leitora de biografias de personalidades notáveis e busca inspiração em suas histórias de superação e liderança.

**Desafios e Dores:**  
Marcela enfrenta constantemente o desafio de minimizar os atrasos de voos causados por falhas inesperadas no sistema de bleed das aeronaves. Isso não apenas prejudica a imagem da empresa, mas também resulta em custos adicionais devido ao consumo de combustível extra quando as aeronaves precisam voar em altitudes mais baixas. Ela busca maneiras de melhorar a eficiência da manutenção, reduzir o tempo de inatividade das aeronaves e maximizar a utilização dos recursos.

**Objetivos e Necessidades:**  
Marcela está empenhada em encontrar soluções que permitam prever falhas no sistema de bleed com antecedência, de modo a evitar atrasos e otimizar a utilização de recursos. Ela precisa de um dashboard claro e intuitivo que apresente informações cruciais de previsão de falhas de maneira compreensível, mesmo sem um profundo conhecimento técnico. Deseja também que a previsão forneça um tempo de reação suficientemente longo (mais de 7 dias) para permitir a programação eficiente da manutenção preventiva e a alocação de peças e técnicos, evitando interrupções não planejadas nas operações.

### Canvas de proposta de valor

O canvas de proposta de valor é uma ferramenta visual e concisa que ajuda a definir e comunicar de maneira clara como um produto ou serviço atende às necessidades específicas dos clientes. Ele descreve os principais elementos que tornam a oferta única, destacando os problemas que ela resolve, as soluções que oferece, os benefícios-chave para os clientes e o valor exclusivo que a diferencia da concorrência. Assim, o canvas de proposta de valor é uma abordagem prática e estratégica para construir uma proposição convincente que ressoa com o público-alvo e impulsiona o sucesso do negócio.

![](./outros/canvas.png)

### User stories

Como Marcela, gerente de operações de manutenção na Azul, quero visualizar previsões claras de falhas no sistema de bleed das aeronaves, para que eu possa tomar decisões informadas e agendar a manutenção preventiva de forma eficiente.

Como Marcela, quero receber notificações proativas sobre possíveis falhas no sistema de bleed com pelo menos 7 dias de antecedência, para garantir que tenha tempo suficiente para planejar a alocação de peças e técnicos e evitar atrasos devido a interrupções inesperadas.

Como Marcela, desejo acessar um dashboard online intuitivo e amigável, que apresente as previsões de falha do sistema de bleed de maneira clara e compreensível, mesmo sem conhecimento técnico profundo.

Como Marcela, preciso ter a capacidade de consultar a API conectada ao sistema de previsão de falhas, para que eu possa integrar essas informações com nossos sistemas internos de gerenciamento de frota e manutenção.

Como Marcela, quero ver um histórico das previsões de falha anteriores e das falhas reais que ocorreram, para avaliar a precisão do modelo preditivo ao longo do tempo e tomar decisões baseadas em evidências.

Como Marcela, desejo ter a opção de ajustar as configurações de previsão, como o horizonte de tempo para as previsões e os limiares de alerta, para personalizar a abordagem de acordo com as necessidades da nossa operação.

Como Marcela, desejo ver indicadores visuais que mostrem o nível de confiança das previsões, permitindo-me avaliar a certeza das informações e tomar decisões com base na qualidade da previsão.

Como Marcela, quero receber análises e insights periódicos sobre a eficácia do modelo preditivo, incluindo métricas de desempenho e sugestões para melhorar a precisão das previsões.

### Análise financeira

A análise financeira é fundamental para entendermos os gastos que a Azul terá ao desenvolver o MVP do projeto com base na nossa solução proposta. Nós examinamos detalhadamente os custos envolvidos, desde a contratação de pessoal até despesas como hospedagem. Além disso, também consideramos a possibilidade de a Azul obter lucro ao oferecer serviços para outras empresas usando o produto que iremos criar. Em resumo, essa análise nos ajuda a entender quanto será necessário investir e como podemos aproveitar as oportunidades para gerar retorno financeiro.

| Serviço              | Preço p/ ano    | Preço p/ mês  |
| -------------------- | --------------- | ------------- |
| MVP                  | R$ 5,213,600.00 | R$ 434,466.67 |
| Manutenção do modelo | R$ 355,000.00   | R$ 29,583.33  |
| Total em reais       | R$ 5,568,600.00 | R$ 464,050.00 |

No que diz respeito à equipe encarregada do MVP, nossa composição inclui dois desenvolvedores juniores com um custo mensal de R$ 16.000 cada, dois desenvolvedores plenos com um custo de R$ 21.000 cada, dois desenvolvedores seniores com um custo de R$ 26.000 cada, além de dois gerentes com um custo de R$ 40.000 cada. Adicionalmente, contamos com a liderança de um diretor, cujo custo mensal é de R$ 20.000. Além desses custos de pessoal, também está incluído o custo mensal de manutenção pós-projeto, estimado em R$ 29.583, que leva em conta as projeções feitas para o MVP.

| Serviços MVP         | Preço p/ ano    | Preço p/ mês  |
| -------------------- | --------------- | ------------- |
| Equipe de Cientistas | R$ 1,476,000.00 | R$ 123,000.00 |
| AWS                  | R$ 386,000.00   | R$ 32,166.67  |
| Implementação        | R$ 3,351,600.00 | R$ 279,300.00 |
| Total em reais       | R$ 5,213,600.00 | R$ 434,466.67 |

O custo associado à hospedagem na Amazon Web Services (AWS) é projetado em torno de 33 mil reais por mês, abrangendo serviços de hospedagem do modelo, banco de dados e armazenamento de arquivos para análises, como planilhas. Com todas essas informações consideradas, a estimativa de gastos mensais para todo o projeto é de aproximadamente 434 mil reais. Essa cifra abarca o desenvolvimento do MVP no primeiro ano e assume a não terceirização do produto. No entanto, esse valor pode variar dependendo das decisões futuras do cliente em relação à terceirização.

Uma outra maneira pela qual a Azul pode recuperar os custos está relacionada a reduzir o tempo em que as aeronaves ficam paradas ou voam com defeitos. Isso é fundamental, já que uma aeronave inoperante para manutenção acarreta uma perda média de 500 mil reais por dia para a empresa. Essa diminuição no tempo de inatividade não apenas resulta em economia financeira direta, mas também contribui para preservar a imagem da marca e da empresa, evitando possíveis impactos negativos.

## Economia circular

**Processo produtivo**

Apesar de ser o objeto de estudo principal do projeto e sua importância para a aeronave, o sistema de bleed é um dos vários sistemas que a compõem. Para entendermos a plenitude de sua dimensão, pode-se destrinchar o processo produtivo de uma aeronave, bem como os impactos e as consequências que seu mal funcionamento podem causar.

O processo para a produção de um avião envolve a manufatura de vários materiais, incluíndo fibras sintéticas e vários metais que são resistentes e flexíveis. Nesse contexto, materiais como Alumínio, Titânio, Aço e fibras de carbono são essenciais para produzir estruturas leves e duradouras. Consequentemente, é uma área que possui uma grande demanda por recursos naturais, processos de transformações fisico-químicas e infraestrutura. Todas essas atividades possuem forte impacto socioambiental, incluíndo emissões de gases de efeito estufa e aproveitamento de espaços para construção de aeroportos e armazenamento de aviões.

No segmento de atuação da Azul, o ciclo de vida de uma aeronave pode ser resumida em cinco grandes etapas:

1.  Fase de projeto: Os objetivos e especificações da aeronave são estabelecidos durante o processo de projeto e planejamento. O primeiro passo é usar desenhos, equações, simulações e prototipações.
2.  Fase de construção: Envolve o processo de fabricaçao dos componentes. Nesta etapa, a maioria dos materiais é consumida para a criação das partes e vários requisitos de qualidade precisam ser atingidos.
3.  Fase de montagem: Todos os componentes precisam ser agragados para, enfim, formar a aeronave. Após isso, vários testes são feitos para garantir a integridade do produto.
4.  Fase de operação: Consiste no gerenciamento do uso da aeronave, manutenção e reparo. No nicho da aviação comercial, é nesta fase em que a nave é utilizada como transporte de passageiros e deve ser constantemente monitorada para que não haja problemas. Nesse contexto, é o período em que as falhas do sistemas podem ocorrer por razões diversas (exposição a condições extremas de temperatura e pressão, falhas elétricas, etc), causando restrições operacionais e, consequentemente, o maior gasto de combustível, que prejudica economicamente a empresa e pode diminuir a vida útil do bordo, uma vez que há maior desgaste dos sistemas.
5.  Fase de descomissionamento: envolve o descarte seguro ou a reciclagem da aeronave. Devido a motivos diversos (obsolecência das peças, inviabilidade econômica), o serviço prestado pelo exemplar é descontinuado e a aeronave pode ser armazenada ou desmantelada para reaproveitamento de materiais.

**Análise das Matérias-Primas, Processos de Produção e Impactos Socioambientais na Fabricação de Aeronaves**

A fabricação de aeronaves é um processo multifacetado que envolve uma vasta gama de matérias-primas, processos técnicos e considerações ambientais. A interação entre esses elementos não apenas molda a eficiência e a eficácia das aeronaves, mas também tem implicações significativas na economia, no ambiente e na sociedade como um todo.

A tabela a seguir foi elaborada para fornecer uma visão detalhada dessas complexidades, destacando as matérias-primas específicas utilizadas, os recursos extraídos, os processos de fabricação envolvidos e os impactos resultantes, tanto positivos quanto negativos. Essa abordagem sistemática fornece uma perspectiva abrangente da cadeia de produção, permitindo uma compreensão mais profunda das responsabilidades e oportunidades associadas ao setor aeroespacial.

| Matérias-primas                                             | Recursos                                                                                                                              | Processos                                                                      | Impactos Positivos                                                                                                                                                                                                             | Impactos Negativos                                                                                                                                                                                        |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Petróleo**                                                | Combustível, querosene, lubrificantes, asfalto                                                                                        | Extração; Refinamento; Processos químicos (destilação, tratamento e conversão) | Geração de empregos; Incremento na economia e receita tributária; Aumento da produção de petróleo.                                                                                                                             | Poluição marinha por vazamentos; Impactos sobre sedimento, qualidade da água e emissões atmosféricas; Aumento do fluxo populacional; Pressão sobre a infra-estrutura de disposição de resíduos.           |
| **Minérios (Alumínio e Titânio)**                           | Fabricação de motores, estruturas de fuselagem, tubulações e dutos, reguladores de pressão e válvulas, trocadores de calor, atuadores | Mineração; Processos químicos (Redução, refino e eletrólise)                   | Redução de emissões (redução do peso das aeronaves); Eficiência e durabilidade; Reciclagem; Desenvolvimento de Infraestrutura local; Desenvolvimento econômico; Inovação Tecnológica; Educação e treinamento de trabalhadores. | Degradação de ambientes aquáticos; Desmatamento, erosão do solo; Poluição do ar e água; Saúde Ocupacional (problemas respiratórios); Impacto sobre comunidades indígenas; Perda de Meios de Subsistência. |
| **Materiais resistentes (Aço, Fibra de Carbono, Plástico)** | Tubulações e dutos, válvulas de controle, atuadores, isoladores térmicos, componentes de degelo, sensores e conectores                | Extração de matérias-primas; Processamento e fabricação; Descarte              | Desempenho Aprimorado; Durabilidade; Segurança; Reciclagem e economia circular (reutilização de materiais); Educação e conscientização; Estímulo a pesquisas científicas.                                                      | Consumo de recursos naturais; Uso de energia; Poluição de água e solo; Geração de resíduos.                                                                                                               |

_**Sistema de Bleed**_

Durante a fase de operação, o sistema de Bleed é acionado e possui funções vitais para o bom funcionamento do avião:

1.  Iniciador de motores: Ar bleed pode ser usado para iniciar outros motores do avião.
2.  Sistema de pressurização: Mantêm a cabine em um nível confortável de pressão e oxigênio para os passageiros.
3.  Sistema de descongelamento (de-icing): O avião tem um número de válvulas pneumáticas, pelas quais o avião direciona o ar bleed para as asas, calda e propulsores para ajudar a remover qualquer gelo que possa ter se acumulado. Isso ajuda a melhorar a aerodinâmica e manter o avião voando com segurança.
4.  Condicionamento de Ar: Alimenta o sistema de Ar Condicionado do avião e sistemas gerais de HVAC (aquecimento, ventilação e ar condicionado).

_**Requisitos de visualização**_

Devido à grande quantidade de profissionais envolvidos na operação dessas aeronaves, deve-se pensar nas opções e possibilidades de acesso e visualização de dados de forma a atender suas necessidades. Entendeu-se que há diferentes áreas (Engenharia, Cientistas de Dados, Planejamento) com demandas distintas de consumo dos dados e resultados gerados. Em um primeiro momento, houve a sugestão de entregá-los por meio de dashboards que indicassem limites operacionais (tresholds).

_**Infográfico**_

Com o intuito de mapear todo o processo de produção e consumo, elaborou-se um infográfico:

![Infográfico](/documentos/outros/Infogr%C3%A1fico.jpg)

[Download PDF](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/infografico.pdf).

## Requisitos do projeto

Esta seção detalha os requisitos funcionais e não funcionais do projeto de Manutenção Preditiva para o Sistema de Bleed do Motor da Azul. O objetivo do projeto é utilizar técnicas de análise de séries temporais, para prever possíveis falhas no sistema de bleed de aeronaves da Azul. Essas previsões permitirão tomar medidas preventivas, evitando atrasos operacionais, reduzindo custos com combustível e melhorando a imagem da empresa.

### Requisitos funcionais

**Aquisição de Dados:**

- O sistema deve receber dados provenientes dos voos, através da integração com sistemas já existentes.
- O sistema deve armazenar esses dados na nuvem, como a AWS.

**Pré-processamento de Dados:**

- Os dados brutos recebidos devem ser pré-processados para limpeza, normalização e detecção de outliers, garantindo a qualidade dos dados de entrada para os modelos de predição.
- Os dados limpos devem ser manipulados para priorizar as features mais importantes, segundo o formato esperado pelos algoritmos de treinamento do modelo.

**Modelo:**

- O sistema deve implementar modelos para análise e previsão de séries temporais dos dados do sistema de bleed.
- Deve ser possível ajustar os hiperparâmetros dos modelos  de acordo com as características dos dados e a complexidade das séries temporais.

**Treinamento e Atualização Automatizada:**

- Uma pipeline automatizada de treinamento e atualização do modelo  deve ser estabelecida.
- O pipeline deve ser capaz de re-treinar os modelos em intervalos regulares com os dados mais recentes, incorporando novas informações para melhorar a precisão das previsões.
- O sistema deve gerar gráficos e relatórios para a avaliação do desempenho do novo modelo comparado aos modelos antigos.

**Previsão de Falhas:**

- Com base nos modelos  treinados, o sistema deve fornecer previsões de probabilidade de falha no sistema de bleed para um período de tempo futuro definido.
- Deve ser possível filtrar as previsões por tipo de aeronave.

**API e Dashboard:**

- Uma API REST deve ser desenvolvida para disponibilizar as previsões em tempo real para aplicativos e sistemas externos.
- Um dashboard intuitivo deve ser projetado para permitir que usuários não técnicos visualizem as previsões de falhas de forma clara e compreensível.
- O sistema deve ser capaz de gerar alertas e notificações quando a probabilidade de falha no sistema de bleed atingir um limite predefinido.

### Requisitos não funcionais

- Os modelos  devem ser treinados com precisão para garantir a confiabilidade das previsões de falhas.
- O pipeline de treinamento de modelos deve ser eficiente e escalável para garantir a atualização regular com novos dados.
- Medidas de segurança rigorosas devem ser implementadas para proteger os dados e garantir a privacidade dos usuários.
- O sistema deve ser capaz de dimensionar recursos de acordo com a demanda, garantindo desempenho consistente.
- A API e o dashboard devem ser intuitivos e fáceis de usar, mesmo para usuários não técnicos.
- O sistema deve estar disponível de forma consistente e confiável, minimizando o tempo de inatividade.
- Todas as soluções e componentes devem ser compatíveis com os serviços e padrões de segurança da AWS.

### Viabilidade técnica

A viabilidade técnica baseia-se em técnicas de inteligência artificial, mais especificamente na aplicação de modelos de machine learning para análise de séries temporais. Essa escolha é justificada pela capacidade inerente dos modelos em identificar padrões, tendências e sazonalidades em dados sequenciais.

A estruturação e implementação dos modelos serão facilitadas pela adoção da plataforma de nuvem AWS (Amazon Web Services). A AWS oferece um ecossistema robusto que viabiliza o desenvolvimento, treinamento e implantação de modelos de aprendizado de máquina de maneira escalável e eficiente. A infraestrutura em nuvem possibilita a fácil criação de ambientes de processamento, garantindo a agilidade na subida dos modelos e a configuração de pipelines de treinamento automatizadas.

Além disso, a AWS disponibiliza pipelines pré-configuradas para processamento de dados, permitindo que nossos dados em formato parquet sejam facilmente manipulados e transformados em insights valiosos. A escolha do formato parquet se justifica pela otimização do armazenamento e manipulação de dados estruturados, o que contribui para a agilidade e eficiência do processo analítico.

O histórico de sucesso de sistemas preditivos em outras indústrias é uma evidência sólida da eficácia dessa abordagem. Setores como energia e manufatura já colheram os benefícios da manutenção preditiva, onde sistemas semelhantes permitiram prever falhas em equipamentos críticos e otimizar a operação. A aplicação bem-sucedida dessas técnicas em cenários desafiadores corrobora a viabilidade técnica e o potencial impacto positivo do projeto.

Portanto, a combinação da aplicação de modelos de machine learning, a infraestrutura da AWS, a utilização de pipelines de processamento e o formato otimizado Parquet para manipulação de dados evidenciam uma sólida viabilidade técnica para a implementação bem-sucedida do produto.

## Proposta geral do sistema

A proposta geral deste sistema é a criação e implantação de uma solução de Manutenção Preditiva para o Sistema de Bleed das aeronaves da Azul. O objetivo central é empregar modelos de análise de séries temporais, para prever a ocorrência de falhas no sistema de bleed com base nos dados coletados durante o voo. Essas previsões permitirão uma abordagem proativa, antecipando possíveis falhas e permitindo intervenções preventivas antes que elas ocorram.

Através da aplicação avançada de técnicas de feature engineering e modelagem preditiva, a solução visará melhorar significativamente a eficiência operacional da frota de aeronaves. Além disso, a implementação da solução na infraestrutura de nuvem AWS garantirá a escalabilidade, flexibilidade e confiabilidade necessárias para lidar com a alta frequência de dados e a complexidade da análise. Dessa forma, a proposta alinha-se diretamente com a missão de minimizar atrasos operacionais, reduzir custos e elevar a qualidade dos serviços prestados pela Azul, solidificando sua posição como uma empresa líder no setor de aviação.

## Arquitetura da Solução

![](outros/Arquitetura%20do%20sistmea.png)

Nossa visão com este projeto é propor uma solução agnóstica no que tange à nuvem e plataforma. Desse modo, escolhemos usar os serviços da AWS para a implementação da arquitetura, mas acreditamos que ela pode ser facilmente adaptada para outras plataformas, como o Google Cloud Platform ou o Microsoft Azure.

Nossa arquitetura da solução consiste em um ciclo que começa e termina na interface gráfica. Nesse sentido, o frontend possui dois módulos: a tela de input de novos parquets, para retreinamento do modelo com informações novas, e a tela de dashboard para visualização das métricas dos modelos e computação de novas predições. O frontend é composto por um módulo em Next.js, que contém a interface em si, e um módulo de Streamlit, que traz os gráficos derivados dos dados de sensores e performance de modelos. O Streamlit, no caso, é embutido na UI do Next.js, apesar de ser gerado por um servidor à parte. Ambos foram contêinerizados para serem executados numa EC2 de IP elástico 52.22.56.34.

Ainda na UI, temos a tela de "/upload". O formulário dessa página permite enviar arquivos parquet para nosso bucket "parquets" no S3. Para isso, uma outra EC2 roda a imagem da API "parquet_api" Essa API, ainda, se conecta com uma coleção no DynamoDB, denominada "bucket_size", que mantém a contagem de arquivos adicionados ao bucket desde o último treinamento de modelo. Toda vez que essa contagem ultrapassa uma threshold específica, essa API aciona o script de pré-processamento e treinamento do modelo com os dados novos.

Nesse momento, os dados são pré-processados e salvos como itens em um tabela relacional, em um servidor MySQL em RDS. Depois disso, o script de treinamento executado e o modelo é salvo em outro bucket para uso posterior.

Então, novamente no frontend, a página de predição se comunica com uma API de predict, também deployada em EC2. Nesse contexto, a API consome o modelo exportado, a partir do S3, e, ao receber os inputs do formulário, retorna a estimativa de quantos dias faltam para a próxima falha. Da mesma forma, uma coleção em DynamoDB fornece os dados para os gráficos do Streamlit.

## Interface

A aplicação é composta por uma tela de login que utiliza o Firebase como autenticador. Ao clicar em login, uma janela pop-up abrirá para selecionar uma conta Google.

![Tela de login](./outros/Login-page.png)

Na aba Upload, é possível selecionar arquivos .parquet na máquina.

![Tela de upload](./outros/Upload.png)

Na aba predict, é possível entrar com dados nos campos que representam as diferentes leituras dos sensores. Após seu preenchimento, há um botão de Submit, em que os dados serão processados e o modelo gerará uma predição. Para uma primeira implementação da aplicação, os campos serão preenchidos manualmente pelo usuário. Pretendemos, em versões futuras, fazer com que os dados sejam capturados automaticamente a partir do upload do arquivo.

![Tela de predict](./outros/Predict.png)

## Visualização de dados

A visualização de dados acontece através da biblioteca streamlit, que é lançada juntamente com o serviço de frontend. Aqui, os dados são consumidos diretamente da base de dados e servidos em gráficos interativos.

![](./outros/Dashboards.png)

Os gráficos desempenham um papel fundamental na avaliação da qualidade dos modelos e na estimativa dos dias restantes até a próxima falha na frota. O principal objetivo é capacitar o usuário a tomar decisões embasadas em dados sólidos, fornecendo uma visão abrangente do estado da frota.

A escolha do gráfico à esquerda se deve ao fato de que ele permite uma visualização mais clara da possibilidade de ocorrer uma falha em um determinado período de tempo, sendo de fácil compreensão para todos os usuários.

Além disso, à direita da interface, encontra-se um gráfico de barras que exibe a qualidade dos modelos, expressa em porcentagem de acurácia. Esse gráfico possibilita uma comparação direta entre os modelos, permitindo que o usuário avalie a qualidade de cada um deles e escolha o mais adequado às suas necessidades.

A escolha do gráfico de barras se deve principalmente à sua excelente facilidade de visualização e interpretação de dados. Além disso, ele viabiliza a comparação entre diferentes modelos, capacitando o usuário a tomar decisões bem fundamentadas com base nas informações disponíveis. Dessa forma, a aplicação proporciona uma visão geral completa do estado da frota, permitindo que qualquer usuário tome decisões informadas e embasadas nos dados apresentados.

## Arquitetura de dados

Nesta seção, examinamos como os dados são organizados e gerenciados para o sistema de manutenção preditiva das aeronaves da Azul. Isso envolve definir como as informações são coletadas, armazenadas e processadas para tomar decisões informadas. Nosso objetivo é garantir que os dados estejam disponíveis quando necessário, sejam confiáveis e seguros, para que o sistema funcione de maneira eficiente e eficaz.

![](outros/Arquitetura_dos_dados.png)

### Descrição dos dados recebidos

A descrição dos dados coletados para o sistema de manutenção preditiva dos aviões da Azul é fundamental para compreender a natureza e a qualidade das informações que serão utilizadas na análise. Os dados foram originados de 17 aeronaves distintas, sendo que cada voo de cada aeronave gerou um arquivo parquet individual. Cada um desses arquivos se torna um DataFrame (df), ao entrar no pipeline, composto em média por 80.000 linhas e 96 colunas. Os valores foram registrados num intervalo de 50 milissegundos (ms), capturando informações detalhadas sobre o desempenho dos componentes e sensores das aeronaves.

É importante ressaltar que esses dados possuem peculiaridades significativas, como campos nulos e valores não numéricos (NaN), resultantes de diferentes taxas de aquisição de dados para cada componente e sensor. A Azul selecionou um conjunto de colunas específicas (features) que foram consideradas potencialmente relevantes para a análise, totalizando 45 colunas. Essas colunas representam uma variedade de parâmetros associados ao funcionamento das aeronaves.

Nesse sentido, o foco da análise estará nas 45 colunas recomendadas pela Azul, proporcionando uma abordagem centrada nos dados mais relevantes para a identificação de padrões, correlações e tendências que possam contribuir para aprimorar a eficácia das estratégias de manutenção preditiva e garantir a segurança e a operação confiável das aeronaves.

Dentre as colunas selecionadas, a maioria apresenta valores numéricos do tipo float64, exceto pela coluna "recording_time", que possui um tipo int64. Os valores registrados nas colunas estão predominantemente na faixa entre -1 e 3, embora isso possa variar dependendo da coluna específica em questão. Notavelmente, o valor mais frequente nos dados é 0, quando não há informações ausentes (NaN). Tudo isso foi examinado com base em uma amostra de cinco parquets.

Além disso, os dados "y" desejados para a análise são indicativos de falhas e são identificados por nomes específicos ("Message0418DAA1" e "Message0422DAA1"). Esses dados "y" representam eventos de falha relacionados ao BLEED, sendo um elemento crucial para a análise de manutenção preditiva, uma vez que fornecem insights sobre o comportamento e a ocorrência de falhas nos sistemas das aeronaves.

## Machine learning

Esta seção traz nossas iterações de pré-processamento, feature engineering e treinamento de modelos através das sprints. Cada tentativa tem sua própria subseção e é correspondida por uma pasta dentro de "notebooks", onde os códigos são mantidos. As versões implementadas na arquitetura completa serão deixadas como scripts na pasta "machine-learning".

### Sprints 2 e 3 (modelos antigos)

#### Descrição da transformação dos dados

Criamos um arquivo Jupyter Notebook, nomeado "agregador", para guiar a primeira etapa da nossa transformação de dados. O principal objetivo desse script é receber arquivos em formato Parquet e prepará-los para pré-processamento e posterior treinamento do modelo.

Ao examinar o dataframe, observamos uma alta frequência de coleta de dados pelos sensores do sistema "bleed". Isso resultou em uma significativa repetição de informações nas linhas de várias tabelas. Com base nisso, decidimos focar na eliminação de dados redundantes e valores nulos como prioridade.

**Ações Tomadas:**

Concatenação de Dados: Unimos dados de 100 arquivos Parquet que correspondiam a um único voo. Essa concatenação juntou apenas arquivos que continham as colunas desejadas.

Eliminação de Redundâncias: Removemos linhas com informações idênticas em todas as colunas, retendo apenas a primeira instância de cada conjunto repetido. Esta ação levou a uma notável redução de 75% no tamanho original do arquivo após a concatenação.

Formatação de Datas: Combinamos as colunas que continham detalhes sobre a data, hora e ano do voo, criando uma coluna unificada no formato datetime. Esta reestruturação foi implementada para simplificar futuras análises de séries temporais.

Após essas ações, o dataframe foi salvo em um novo arquivo parquet por meio da API Dask para ser utilizado no treinamento do modelo.

##### Processamento e Preparação dos dados

Conforme mencionado anteriormente, após a eliminação de linhas com dados repetidos, direcionamos nosso foco também para as colunas. Especificamente, removemos colunas em que todos os valores eram iguais a zero, devido à sua falta de variância e relevância estatística. Do total de 52 colunas, o novo dataframe passou para 36 colunas.

Em relação às colunas que continham nossa variável alvo, realizamos uma transformação para que todos os seus valores fossem convertidos para '1'. Desta forma, adaptamos o conjunto de dados para um problema de classificação binária: identificar se há ou não falha.

##### Modelagem e Resultados

Com os dados devidamente tratados e preparados, prosseguimos com a aplicação do modelo Random Forest Regressor. O objetivo era avaliar a possibilidade de prever futuras falhas. Nesta primeira iteração, os resultados mostraram-se promissores, com um erro quadrático médio de aproximadamente 40%.

#### Classifier on regressor

Esta abordagem híbrida baseia-se em duas etapas: uma de séries temporais e outra de classificação binária. O objetivo é utilizar modelos de série temporal para prever o valor de cada feature em dado momento futuro e, a partir dessas estimativas, classificar o estado de falha do sistema de bleed com um modelo de classificador normal/não temporal. Para isso, foram testados diversos métodos de pré-processamento e feature engineering, assim como vários algoritmos de treinamento, que serão descritos abaixo.

##### Pré-processamento

Como explorado em outras abordagens neste projeto, iniciamos a pipeline com uma etapa de agregação dos diversos parquets. Por limitações de armazenamento e processamento, não podíamos utilizar todos os parquets disponíveis; então, escolhemos trabalhar com a pasta '06120033', pois ela apresentava cerca de 2 GB de dados e, com isso, aumentava o potencial de encontrarmos a variância necessária sem comprometer nosso poder computacional.

De posse dessa pasta, nosso primeiro passo foi identificar quais parquets incluíam casos de falha. O resultado foram 7: 'TCRF_ARCHIVE_06120033_20220530132603.parquet', 'TCRF_ARCHIVE_06120033_20220601151236.parquet', 'TCRF_ARCHIVE_06120033_20220603051739.parquet', 'TCRF_ARCHIVE_06120033_20220603142239.parquet', 'TCRF_ARCHIVE_06120033_20221106150243.parquet', 'TCRF_ARCHIVE_06120033_20230103035245.parquet' e 'TCRF_ARCHIVE_06120033_20230714050245.parquet'. Sabendo disso, passamos à fase de agregação dos parquets em um único arquivo simplificado. Essa fase teve duas ramificações, uma que se focava em séries temporais, e por isso se preocupava em acessar todos os parquets cronologicamente, e outra focada em classificação, priorizando, portanto, o balanceamento dos dados e a inclusão do máximo de casos de falha possível.

Para o dataset de séries temporais, selecionamos os arquivos de index 30 a 1000 da subpasta. Escolhemos esse intervalo porque ele abrangia o máximo de casos de falha, conforme os detectados anteriormente, sem exigir um tempo muito longo de processamento. Para o dataset de classificação, selecionamos os arquivos de index 1220-1950, pois eles não incluíam falha, e então os outros sete parquets identificados com as falhas. Feito isso, realizamos as manipulações seguintes para ambos os casos:

1.  Em cada arquivo, selecionamos apenas as 45 colunas sugeridas pela Azul
2.  Tiramos a média do valor de cada coluna, ignorando valores nulos, para cada janela de 1 hora (72000 linhas). Então, substituímos essas janelas por uma única linha com as médias correspondentes. Nas colunas target, substituímos a janela inteira por 1 caso pelo menos um valor seja não nulo e diferente de zero.
3.  Por fim, juntamos todos esses dataframes em um só e salvamos o arquivo final em 'aggregated_classifier.csv' e 'aggregate_time_series.csv'.

##### Feature engineering

Na feature engineering, começamos a ciência de dados, considerando que, até agora, trabalhamos apenas com engenharia de dados. Nesse sentido, essa etapa se separa em duas ramificações: uma para preparação dos dados para a série temporal e outra para a classificação. Os passos em comum entre elas foram:

1.  Substituir as colunas target (\['message0418DAA-1', 'message0422DAA-1'\]) por uma única, chamada 'failure', que assume 1 quando pelo menos uma das colunas originais é 1, e 0 no caso contrário. Queríamos, com isso, trabalhar com apenas um target.
2.  Checar se existem colunas de valores constantes. Se sim, excluí-las.
3.  Checar se existem colunas com apenas dois valores. Se sim, excluí-las. Assumimos que elas seriam outliers ou extremamente correlatas com outras features de maior variância.
4.  Aplicar forward-fill em quaisquer valores nulos restantes; em geral, muito poucos.
5.  Normalizar todas as colunas, exceto recording_time.

Também criamos uma função de PCA a ser utilizada por ambos os modelos.

Na série temporal, desejávamos testar tanto o Pycaret quando o Prophet para gerar os modelos. Para o primeiro, bastava uma coluna de timestep/timeindex, já para o segundo, era necessário uma coluna de timestamp baseada em datetime. Por isso, criamos as duas colunas, seguindo estes passos:

1.  Abrimos o CSV "aggregated.csv" como dataframe.
2.  Geramos uma coluna "hour", que iniciava em 0 e aumentava uma unidade a cada linha. Também criamos a coluna "ds", que segue a mesma lógica, mas em timestamps, em vez de apenas inteiros. Então, excluímos a coluna "recording_time".
3.  Executamos um algoritmo de PCA para encontrar as 5 colunas mais importantes. Atualizamos o dataframe para que ele contenha essas features, assim como 'failure', 'hour' e 'ds'
4.  Salvamos esse dataframe como CSV ('time_series_data.csv').

Para o classificador, balanceamos os dados utilizando um oversampler e rodamos o mesmo PCA. Selecionamos as 5 features mais importantes e salvamos o dataframe resultante com a coluna target também em 'classifier_data.csv'.

##### Time series

Tínhamos duas abordagens em mente para esta etapa: utilizar o Prophet para realizar a regressão de cada feature, utilizar o Pycaret para realizar a regressão e depois aplicar um classificador, ou aplicar o Pycaret direto para tudo, em único modelo.

Com o Prophet, conseguimos péssimos resultados.

| Coluna                    | Erro Absoluto Médio (MAE) | Erro Absoluto Médio Percentual (MAPE) | Erro Quadrático Médio (RMSE) |
| ------------------------- | ------------------------- | ------------------------------------- | ---------------------------- |
| bleedFavTmFbk-1b          | 0.3839                    | 12,163.62%                            | 0.40                         |
| bleedPrsovClPosStatus-1a  | 0.2399                    | 14,719,566,127,678,746.00%            | 0.28                         |
| bleedHprsovOpPosStatus-1b | 0.3145                    | 8,490,252,914,530,495.00%             | 0.37                         |
| bleedHprsovOpPosStatus-2a | 0.2956                    | 15,609,047,287,048,710.00%            | 0.35                         |
| bleedOnStatus-1b          | 0.2356                    | 9,819,424,402,249,172.00%             | 0.27                         |

Analisando os resultados, observamos que as colunas "têm valores de MAPE extraordinariamente altos, indicando que as previsões estão muito distantes dos valores reais em termos percentuais. Sem mais, desistimos dessa proposta.

Passamos, então, ao Pycaret de Time Series. Nele, nenhum dos modelos conseguiu sequer um R² positivo, ficamos sempre em valores negativos, o que indica que nossos modelos performaram piores que uma linha horizontal. Portanto, desistimos dessa ideia também.

Aplicando o Pycaret para séries temporais que prevejam a resposta final ('failure'), utilizando todas as outras features, tivemos conclusões também desanimadoras. O modelo "Naive Forecaster" exibe um desempenho modesto na tarefa de previsão, o que o torna uma escolha adequada como linha de base. Isso ocorre porque todos os outros modelos treinados pelo PyCaret apresentaram resultados inferiores.

| Model  | MASE   | RMSSE  | MAE    | RMSE   | MAPE          | SMAPE  | R2       | TT (Sec) |
| ------ | ------ | ------ | ------ | ------ | ------------- | ------ | -------- | -------- |
| naive  | 3.1650 | 1.0271 | 0.0133 | 0.0667 | 0.0133        | 0.0267 | 0.6528   | 2.2567   |
| snaive | 3.1650 | 1.0271 | 0.0133 | 0.0667 | 0.0133        | 0.0267 | 0.6528   | 0.1033   |
| stlf   | 3.1666 | 1.0272 | 0.0133 | 0.0667 | 33177466470.7 | 2.0000 | \-0.0139 | 0.086    |

O modelo Naive Forecaster apresenta um alto MASE (Mean Absolute Scaled Error) de 3.1650, indicando que suas previsões são aproximadamente 3.17 vezes piores do que um modelo ingênuo que assume valores futuros iguais aos valores históricos. Além disso, o RMSSE (Root Mean Squared Scaled Error) de 1.0271 sugere uma considerável variabilidade nas previsões em relação aos dados reais. Embora o MAE (Mean Absolute Error) e o RMSE (Root Mean Squared Error) indiquem erros médios e quadráticos médios relativamente baixos, isso pode ser enganador, pois o modelo pode consistentemente subestimar ou superestimar os valores reais. O MAPE (Mean Absolute Percentage Error) e o SMAPE (Symmetric Mean Absolute Percentage Error) mostram erros percentuais relativamente baixos. No entanto, o R2 (Coeficiente de Determinação) de 0.6528 sugere que o modelo explica apenas cerca de 65.28% da variabilidade nos dados, sugerindo espaço para melhorias significativas na precisão das previsões.

##### Classificador

Ademais, tentamos também empregar o Pycaret em um classificador simples. As métricas obtidas foram muito superiores, porém, sabemos que essa abordagem só será efetiva se tambem tivermos regressores temporais igualmente bem-sucedidos para as features.

| Método   | Nome Completo                   | Precisão | Revocação | F1-Score | Acurácia | Precisão Média | Revocação Média | AUC-ROC |
| -------- | ------------------------------- | -------- | --------- | -------- | -------- | -------------- | --------------- | ------- |
| et       | Extra Trees Classifier          | 0.9538   | 0.9809    | 0.9671   | 0.9424   | 0.9544         | 0.9076          | 0.9081  |
| lightgbm | Light Gradient Boosting Machine | 0.9483   | 0.9859    | 0.9652   | 0.9338   | 0.9491         | 0.8966          | 0.8973  |
| rf       | Random Forest Classifier        | 0.9478   | 0.9826    | 0.9643   | 0.9339   | 0.9487         | 0.8957          | 0.8964  |

Os três modelos de classificação, Extra Trees Classifier (et), Light Gradient Boosting Machine (lightgbm) e Random Forest Classifier (rf), demonstraram desempenhos notáveis em uma variedade de métricas de avaliação. Todos eles alcançaram altas pontuações em termos de precisão, revocação, F1-Score e AUC-ROC, sugerindo que são capazes de fazer previsões precisas.

O Light Gradient Boosting Machine (LightGBM) obteve a maior pontuação de precisão e revocação, indicando uma capacidade superior de identificar corretamente tanto os exemplos positivos quanto negativos. No entanto, o Extra Trees Classifier (ET) e o Random Forest Classifier (RF) não ficaram muito atrás, demonstrando um desempenho robusto e consistente em todas as métricas.

Uma vantagem do Extra Trees Classifier (ET) é a sua menor propensão ao overfitting, em comparação com os outros modelos. Isso ocorre devido à introdução de uma maior aleatoriedade durante o processo de construção das árvores de decisão no ET, o que ajuda a evitar ajustes excessivos aos dados de treinamento. Portanto, a escolha do ET pode ser justificada não apenas pelo seu desempenho consistente em métricas de avaliação, mas também pela sua capacidade inerente de manter um equilíbrio entre precisão e generalização, minimizando os riscos de overfitting em situações práticas de aplicação do modelo.

#### Treinamento com dados balanceados

Para esta análise de dados, o objetivo final é demonstrar os resultados de modelos construídos a partir de conjuntos de dados balanceados, possuindo quantidades semelhantes tanto para dados com erros de bleed quanto para dados sem erros de bleed. Para alcançar esse resultado, testamos vários modelos de regressão utilizando a biblioteca PyCaret para AutoML.

##### Regressão

Modelos de regressão são utilizados para prever resultados numéricos em vez de binários, seja relacionados ao tempo, quantidade ou outros tipos de dados numéricos. No nosso caso, os utilizaremos para prever em quanto tempo ocorrerá um erro de bleed.

|          | Model                           | MAE    | MSE      | RMSE    | R2     | RMSLE  | MAPE   | TT (SEC) |
|----------|---------------------------------|--------|----------|---------|--------|--------|--------|----------|
| et       | Extra Trees Regressor           | 2.2843 | 65.6331  | 8.0737  | 0.8318 | 0.4705 | 0.4435 | 41.2920  |
| rf       | Random Forest Regressor         | 2.7578 | 96.4672  | 9.7847  | 0.7539 | 0.5171 | 0.5304 | 175.6570 |
| lightgbm | Light Gradient Boosting Machine | 4.8688 | 117.8259 | 10.8249 | 0.6974 | 0.7744 | 1.0813 | 3.7930   |

Os três modelos apresentados, Extra Trees Regressor (ET), Random Forest Regressor (RF) e Light Gradient Boosting Machine (LIGHTGBM) , obtiveram resultados relativamente semelhantes quando considerados como um todo, estando todos próximos uns dos outros. No entanto, o melhor desempenho foi alcançado pelo Extra Trees Regressor, que apresentou um R2 score de 83,18%, o que é um resultado satisfatório, principalmente para métricas de regressão, que tendem a ser menores que de classificação, em comparação.

Em relação ao pré-processamento feito, objetivou-se reduzir a dimensionalidade dos dados, porém ser perder suas tendências.
Para isso todos os parquets selecionados foram reduzidos, usando a média dos valores a cada 300 linhas, o que equivale à 15 segundos.

Outro ponto a ser considerado é a seleção de parquets e como ocorreu. O objetivo foi escolher intervalos de parquets anteriores à uma falha, de modo que quanto mais perto do erro, mais relevância aquele dado deveria ter. Para isso então, foram selecionados intervalos entre 15-30, 60-75, 115-130, 180-195 e 255-270 de parquets anteriores ao erro. Nos intervalos fica visível que o a distância entre eles aumenta, exatamente com o objetivo de dar mais importância aos dados próximo ao bleed.

Para entender mais à fundo como foi feito o tratamento dos dados, segue link do notebook: [processing_data_rp.ipynb](../notebooks/sprint_4/regression-pycaret/processing_data_rp.ipynb)

#### Análise exploratória para o modelo de agreggator com pycaret

A análise exploratória foi realizada com um conjunto de dados provenientes de uma única aeronave. O intuito foi identificar padrões, tendências, anomalias e características-chave que possam orientar futuros processos analíticos e de modelagem. A natureza do dataset, os procedimentos adotados para sua limpeza e transformação, assim como os principais insights adquiridos, serão discutidos a seguir.

##### Origem dos dados

O dataset dessa etapa foi construído a partir de 30 arquivos parquets, todos referentes a aeronave 06120089. Este formato foi utilizado para lidar com dados de grande volume, garantindo eficiência na leitura e no processamento.

**Estrutura Inicial:**

- Total de entradas: 1.885.000
- Colunas selecionadas para análise: `_['recording_time', 'dateDay-1', 'dateMonth-1', 'dateYear-1', 'phaseOfFlight-1', 'message0418DAA-1','message0422DAA-1','amscHprsovDrivF-1a', 'amscHprsovDrivF-1b', 'amscHprsovDrivF-2b', 'amscPrsovDrivF-1a', 'amscPrsovDrivF-1b', 'amscPrsovDrivF-2b', 'basBleedLowPressF-1a', 'basBleedLowPressF-2b', 'basBleedLowTempF-1a', 'basBleedLowTempF-2b', 'basBleedOverPressF-1a', 'basBleedOverPressF-2b', 'basBleedOverTempF-1a', 'basBleedOverTempF-2b', 'bleedFavTmCmd-1a', 'bleedFavTmCmd-1b', 'bleedFavTmCmd-2a', 'bleedFavTmCmd-2b', 'bleedFavTmFbk-1a', 'bleedFavTmFbk-1b', 'bleedFavTmFbk-2b', 'bleedHprsovCmdStatus-1a', 'bleedHprsovCmdStatus-1b', 'bleedHprsovCmdStatus-2a', 'bleedHprsovCmdStatus-2b', 'bleedHprsovOpPosStatus-1a', 'bleedHprsovOpPosStatus-1b', 'bleedHprsovOpPosStatus-2a', 'bleedHprsovOpPosStatus-2b', 'bleedMonPress-1a', 'bleedMonPress-1b', 'bleedMonPress-2a', 'bleedMonPress-2b', 'bleedOnStatus-1a', 'bleedOnStatus-1b', 'bleedOnStatus-2b', 'bleedOverpressCas-2a', 'bleedOverpressCas-2b', 'bleedPrecoolDiffPress-1a', 'bleedPrecoolDiffPress-1b', 'bleedPrecoolDiffPress-2a', 'bleedPrecoolDiffPress-2b', 'bleedPrsovClPosStatus-1a', 'bleedPrsovClPosStatus-2a', 'bleedPrsovFbk-1a', 'timeHours-1', 'timeMinutes-1', 'timeSeconds-1']_`

##### Pré-processamento dos Dados

**(i) Concatenação dos Arquivos:**

Os 30 arquivos foram combinados em um único dataframe, resultando em um conjunto unificado com ênfase nas colunas de interesse.

**(ii) Limpeza de Dados:**

Para redução dos dados, foram removidas linhas que continham informações duplicadas em todas as colunas, exceto na 'recording_time'. Assim, foi-se mantido apenas a primeira linha com informações duplicadas.

Este processo de limpeza levou a uma redução considerável, deixando o dataframe com 1.032.654 linhas.

**(iii) Transformações:**

- A combinação de colunas relacionadas à data e tempo levou à criação da coluna `datetime`, facilitando análises temporais e otimizando o espaço.

##### Análises

**(i) Matriz de Correlação:**

- A matriz revelou que a maioria das colunas possui correlação positiva fraca (indicado pelas cores azuis claras e vermelho claro).
- Algumas colunas não apresentaram qualquer correlação.

![Matriz de correlação inicial](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/matriz%20de%20correla%C3%A7%C3%A3o%20inicial.png)

**(ii) Box Plot:**

- Esta análise focou exclusivamente nas colunas dos sensores.
- Resultados notáveis:
  - Presença de outliers individuais e valores atípicos em diversas colunas.
  - Poucas colunas mostraram uma distribuição de box plot normal.
  - Visualmente, apenas colunas de certos grupos de sensores do "Bled" mostraram uma distribuição mais uniforme.

![Box Plot inicial](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/blox%20plot%20inicial.png)

**(iii) Análise de Tendências Temporais:**

Os dados foram analisados para o período de 01/12/2023 até 15/01/2023.

Foi-se realizado o agrupamento das seguintes colunas para uma melhor representação visual: `{ 'amscHprsovDriv': ['amscHprsovDrivF-1a', 'amscHprsovDrivF-1b', 'amscHprsovDrivF-2b'], 'amscPrsovDriv': ['amscPrsovDrivF-1a', 'amscPrsovDrivF-1b', 'amscPrsovDrivF-2b'], 'basBleedLow': ['basBleedLowPressF-1a', 'basBleedLowPressF-2b', 'basBleedLowTempF-1a', 'basBleedLowTempF-2b'], 'basBleedOver': ['basBleedOverPressF-1a', 'basBleedOverPressF-2b', 'basBleedOverTempF-1a', 'basBleedOverTempF-2b'], 'bleedFavTm': ['bleedFavTmCmd-1a', 'bleedFavTmCmd-1b', 'bleedFavTmCmd-2a', 'bleedFavTmCmd-2b', 'bleedFavTmFbk-1a', 'bleedFavTmFbk-1b', 'bleedFavTmFbk-2b'], 'bleedHprsov': ['bleedHprsovCmdStatus-1a', 'bleedHprsovCmdStatus-1b', 'bleedHprsovCmdStatus-2a', 'bleedHprsovCmdStatus-2b', 'bleedHprsovOpPosStatus-1a', 'bleedHprsovOpPosStatus-1b', 'bleedHprsovOpPosStatus-2a', 'bleedHprsovOpPosStatus-2b'], 'bleedMon': ['bleedMonPress-1a', 'bleedMonPress-1b', 'bleedMonPress-2a', 'bleedMonPress-2b'], 'bleedStatus': ['bleedOnStatus-1a', 'bleedOnStatus-1b', 'bleedOnStatus-2b'], 'bleedOverpressCas': ['bleedOverpressCas-2a', 'bleedOverpressCas-2b'], 'bleedPrecoolDiff': ['bleedPrecoolDiffPress-1a', 'bleedPrecoolDiffPress-1b', 'bleedPrecoolDiffPress-2a', 'bleedPrecoolDiffPress-2b'], 'bleedPrsov': ['bleedPrsovClPosStatus-1a', 'bleedPrsovClPosStatus-2a', 'bleedPrsovFbk-1a'] }`

Após a construção dos gráficos, foi-se observado que apenas os grupos `'bleedFavTm', 'bleedHprsov', 'bleedMon', 'bleedStatus', 'bleedOverpressCas', 'bleedPrecoolDiff', e 'bleedPrsov'` mostram variações significativas em seus valores ao longo do período em estudo.

![gráficos temporais 1](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/graficos%20temporais%201.png)

![gráficos temporais 2](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/graficos%20temporais%202.png)

##### Análises subsequentes e conclusões

Com base nas análises, algumas ações foram realizadas para criação dos modelos:

**Exclusão de colunas sem variação nos valores:** A constante nas leituras de certos grupos sugere que a variação é mínima ou inexistente. Essas colunas foram excluídas para o treinamento de modelos futuros, garantindo eficiência e foco.

**Nova Análise:** As colunas restantes foram novamente submetidas à matriz de correlação e ao box plot. Conforme a figura abaixo mostra, estas colunas tendem a ter correlações mais fortes entre si e exibem distribuições com menos outliers.

![Análise final](https://github.com/2023M7T2-Inteli/bluebird/blob/main/documentos/outros/matriz%20de%20correla%C3%A7%C3%A3o%20e%20box%20plot%20apos.png)

#### **Agreggator com pycaret**

Visando criar um modelo capaz de prever com uma semana de antecedência se ocorrerá falha ou não no avião, foram criados intervalos de falha. Esses intervalos correspondem ao dia específico em que ocorreu a falha e aos seis dias anteriores. Dessa maneira, é possível identificar janelas de falha, que são o alvo da predição do modelo.

Durante a análise desses dados, notou-se a existência de apenas um dia de falha no sistema de bleed. Portanto, foi possível criar apenas uma semana de dados de falhas. Todo esse processo pode ser encontrado em mais detalhes na pasta "aggregator_regression" com o notebook "data_processing".

Ao executar o AutoML com o PyCaret, utilizando modelos de regressão linear cujo objetivo é encontrar uma janela de falha na próxima semana, obtivemos os seguintes resultados.

<table><tbody><tr><td>&nbsp;</td><td><strong>Model</strong></td><td><strong>MAE</strong></td><td><strong>MSE</strong></td><td><strong>RMSE</strong></td><td><strong>R2</strong></td><td><strong>RMSLE</strong></td><td><strong>MAPE</strong></td></tr><tr><td><strong>lightgbm</strong></td><td>Light Gradient Boosting Machine</td><td>0.0032</td><td>0.0001</td><td>0.0096</td><td>0.9991</td><td>0.0049</td><td>0.0290</td></tr><tr><td><strong>xgboost</strong></td><td>Extreme Gradient Boosting</td><td>0.0101</td><td>0.0009</td><td>0.0303</td><td>0.9905</td><td>0.0156</td><td>0.0913</td></tr><tr><td><strong>dummy</strong></td><td>Dummy Regressor</td><td>0.1173</td><td>0.1084</td><td>0.3293</td><td>-0.1048</td><td>0.2275</td><td>0.9911</td></tr></tbody></table>

Uma análise mais detalhada revela que esses resultados não são satisfatórios. Tendo em mente a existência de apenas uma janela de falha, o modelo provavelmente sofreu com overfitting, uma vez que apresenta um R² acima de 99% tanto no LightGBM quanto no XGBoost.

Essa conclusão pode ser obtida ao examinar a importância das features nos resultados do modelo, onde o dia e o ano demonstram ter uma influência significativa. É possível verificar esses resultados no arquivo "aggregator_regression" dentro da pasta "aggregator_regression".

Para as próximas iterações, o objetivo é desenvolver um modelo que lide adequadamente com a análise de séries temporais e incluir mais janelas de falhas. Isso se baseia nos resultados satisfatórios obtidos no artigo "Predicting Compressor Valve Failures from Multi-Sensor Data," que abordou um problema semelhante ao que vem sendo tratado.

#### Exponential Smoothing Simples

O Exponential Smoothing Simples (SES) é a forma mais básica e fundamental da técnica de suavização exponencial em séries temporais. Ele é amplamente utilizado para realizar previsões com base em padrões históricos, sendo especialmente adequado para séries temporais que não exibem tendências significativas ou sazonalidades.

A principal característica do Exponential Smoothing Simples é a ênfase dada aos valores mais recentes da série temporal. Ele assume que o próximo valor na série é uma combinação ponderada do valor atual e da previsão anterior. A fórmula geral para o SES é:  
​  
$`F_{t+1} = \alpha * Y_t + (1 - \alpha) * F_t`$

Onde:

$F\_{t+1}$ é a previsão para o próximo período.  
$Y\_t$ é o valor atual na série temporal.  
$F\_t$ é a previsão anterior (para o período anterior).  
$\\alpha$ é o parâmetro de suavização exponencial, que controla o peso dado ao valor atual $(Y\_t)$ em relação à previsão anterior $(F\_t)$. O valor de $\\alpha$ está no intervalo de 0 a 1 e determina o grau de suavização.

Neste primeiro estágio, ao aplicar o método de previsão, optamos por simplificar a complexidade dos dados, já que estávamos trabalhando com a previsão de uma única característica por vez. Para isso, realizamos uma redução na dimensionalidade combinando todas as colunas que possuíam nomes semelhantes, como por exemplo, 'bleedPrsovFbk-1a' e 'bleedPrsovFbk-1b', que foram consolidadas em uma única coluna denominada 'bleedPrsovFbk', representando a diferença entre elas. Essa abordagem permitiu uma simplificação no manuseio das informações futuramente.

Durante os treinamentos da Sprint 3, conseguimos resultados aceitáveis para a previsão de algumas das características, porém são muito inferiores às outras análises que fizemos. Para exemplificar, ao prever 12 valores da coluna 'bleedPrsovFbk', que indica os valores em mA, obtivemos os seguintes resultados:

| Model                 | Feature       | MAE  | MSE  | RMSE |
| --------------------- | ------------- | ---- | ---- | ---- |
| Exponential Smoothing | bleedPrsovFbk | 3.41 | 15.4 | 3.93 |

É importante notar que as previsões obtidas apresentaram coerência com os valores anteriores e têm potencial para serem utilizadas na definição de futuros thresholds que indicariam falhas em componentes específicos.

Para análises subsequentes, nossa meta será estender o modelo para abranger um conjunto mais amplo de características e obter o maior número possível de thresholds. Essa abordagem nos permitirá criar um conjunto de critérios que identificará falhas de forma mais abrangente e precisa.

#### Modelos adotados

Após uma análise do problema, chegamos à conclusão de que seria válido criar um modelo capaz de classificar se haverá ou não uma falha na próxima semana. Com isso em mente, desenvolvemos o seguinte pipeline.

##### 1ª Etapa: Preparação dos dados

O objetivo desta etapa é criar uma janela de falha da turbina e agregar o máximo de voos em um único  dataset. Para atingir esse objetivo,  as falhas diárias foram transformadas em falhas semanais. Foram selecionados os arquivos que contêm falhas e criado uma janela de 6 dias anteriores e 2 dias posteriores a cada falha. Dessa forma, qualquer falha que ocorra no dia 6 torna todos os dias anteriores até o início do mês como falha, e os dias após a falha são marcados como não falha. Os dias sem falhas foram adicionados para equilibrar o conjunto de dados. Essa transformação foi realizada com base nos nomes dos arquivos, pois eles já contêm a data no nome. Para ver os detalhes deste processo para vários dias da semana, acesse o seguinte link:

[Agregando Dados](https://github.com/2023M7T2Inteli/bluebird/blob/main/notebooks/sprint_4/classification-pycaret/Agregando-dados.ipynb)

##### 2ª Etapa: Criação da coluna alvo

A segunda etapa consiste em criar a janela de falha temporal a partir do conjunto de dados resultante. Nesta etapa, é criada uma coluna de data e hora com as informações de cada voo. Além disso, é criada uma coluna de falha semanal. Se um voo estiver dentro do intervalo definido como falha, a coluna de falha semanal recebe o valor 1, indicando verdade. Para obter um guia passo a passo detalhado dessa etapa, visite o seguinte link:

[Preparação de Dados](https://github.com/2023M7T2-Inteli/bluebird/blob/main/notebooks/sprint_4/classification-pycaret/Prepara%C3%A7%C3%A3o-dados.ipynb)

##### 3ª Etapa: Criando o modelo

A última etapa é o treinamento do modelo em si com o PyCaret. Como o objetivo do modelo é descobrir se haverá ou não falha na próxima semana, a variável alvo é a coluna de falha semanal. Por fim, é feito todo o passo a passo do PyCaret e exportado o modelo. O notebook pode ser visto no seguinte link e os resultados do modelo foram os seguintes.

<table><tbody><tr><td>&nbsp;</td><td><strong>Accuracy</strong></td><td><strong>AUC</strong></td><td><strong>Recall</strong></td><td><strong>Precision</strong></td><td><strong>F1</strong></td><td><strong>TT (Sec)</strong></td></tr><tr><td>CatBoost Classifier</td><td>0.9700</td><td>0.9833</td><td>0.9922</td><td>0.9763</td><td>0.9842</td><td>302.2240</td></tr><tr><td>Extreme Gradient Boosting</td><td>0.9628</td><td>0.9733</td><td>0.9933</td><td>0.9679</td><td>0.9805</td><td>27.2090</td></tr><tr><td>Light Gradient Boosting Machine</td><td>0.9570</td><td>0.9617</td><td>0.9953</td><td>0.9604</td><td>0.9775</td><td>14.3880</td></tr><tr><td>Logistic Regression</td><td>0.9396</td><td>0.7129</td><td>1.0000</td><td>0.9396</td><td>0.9689</td><td>164.6790</td></tr></tbody></table>

[Modelo CatBoost](https://github.com/2023M7T2-Inteli/bluebird/blob/main/notebooks/sprint_4/classification-pycaret/Modelo-catboost.ipynb)

##### Como utilizar o modelo 
Para o modelo só é necessário realizar o input dos dados no formato de dataframe. E os detalhes desse input está disponível no notebook [Modelo CatBoost](https://github.com/2023M7T2-Inteli/bluebird/blob/main/notebooks/sprint_4/classification-pycaret/Modelo-catboost.ipynb)

##### Métricas do modelo 
Ao realizar o teste de quanto poder computacional é necessário para uma predição foram obtidos os seguintes dados 

| Peak memory  | CPU time |
| ------------- | ------------- |
|  446.99 mb  | 328 ms  |

É preciso notar que o computador no qual o teste foi realizado é um DELL-Latitude 5420 com 16 GB de RAM DDR4 e um processador i5-1145G7.

#### Custo para uso do modelo
Quando se trata de calcular o custo do uso deste modelo, é importante considerar que o custo computacional por requisição é relativamente baixo. Recomendamos a utilização de uma instância EC2 da AWS no tamanho t2.micro para hospedar o modelo, levando em consideração as seguintes considerações:

 - O projeto tem um baixo volume de requisições por semana.
- Não há uma alta demanda simultânea para processamento de dados.
- O tamanho da instância t2.micro é suficiente para a carga prevista e oferece uma opção econômica.
## Tecnologias selecionadas

Como descrito anteriormente, trabalhamos paralelamente com tecnologias mais simples para a POC e planejamos a migração para tecnologias mais robustas no médio prazo. Nesse sentido, descrevemos nessa seção as tecnologias atualmente implementadas; a serem atualizadas conforme adotamos as funcionalidades da AWS em seu lugar.

### Frontend

| Tecnologia                                                      | Utilização            | Justificativa                                                                                                   |
| --------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------- |
| ![Next.js Icon](https://skills.thijs.gg/icons?i=nextjs) Next.js | Interface gráfica     | Framework baseada em React com Tailwind e roteador de páginas integrados, diminuindo o tempo de desenvolvimento |
| Streamlit                                                       | Criação de Dashboards | Biblioteca que facilita no desenvolvimento de dashboards para consumo dos dados pelo usuário                    |

### Backend

| Tecnologia                                                                 | Utilização                                                  | Justificativa                                                             |
| -------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
| ![Node.js Icon](https://skills.thijs.gg/icons?i=nodejs)Express com Node.js | Backend para APIs                                           | Maior familiaridade do time, diminuindo o tempo de desenvolvimento da POC |
| ![FastAPI Icon](https://skills.thijs.gg/icons?i=fastapi) FastAPI           | Backend para consumo do modelo e conexão com Banco de dados | Familiaridade dos integrantes em desenvolver usando a tecnologia          |

### Armazenamento de dados

| Tecnologia                                                                | Utilização                                                              | Justificativa                                                                                 |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ![PostgreSQL Icon](https://skills.thijs.gg/icons?i=postgresql) PostgreSQL | Banco de dados relacional para dados processados                        | Facilidade de conteinerização e integração com Prism                                          |
| ![Pocketbase Icon](https://pocketbase.io/images/logo.svg) Pocketbase      | Bucket para parquets e modelos                                          | Bucket local com pouco consumo de memória, otimizado para POCs                                |
| ![MongoDB](https://skills.thijs.gg/icons?i=mongodb)                       | Banco de dados não relacional para métricas e comparações entre modelos | Acesso mais fácil e flexível para informações que não precisam ser necessariamente simétricas |
| Bucket AWS S3                                                             | Bucket em nuvem para armazenamento de arquivos                          | Estrutura de armazenamento escalável de arquivos                                              |
| AWS DynamoDB                                                              | Serviço de Tabela não-relacional                                        | Estrutura de armazenamento escalável de arquivos para treinamentos posteriores dos modelo     |
| AWS RDS                                                              | Serviço de Tabela Relacional                                            | Estrutura de armazenamento escalável de tabelas relacionais para dados pré-processados     |

No banco de dados criado a partir do PostgreSQL, realizamos a arquitetura do banco em 3 tabelas, sendo ela uma direcionada aos aviões, uma direcionada aos vôos e outra direcionada aos dados dos vôos que vamos receber a partir do processo de ETL:

![postgres - public](https://github.com/2023M7T2-Inteli/bluebird/assets/99187756/87422a21-243f-43b5-9d80-c4639a29aa49)

### Machine learning

| Tecnologia                                                    | Utilização                                                     | Justificativa                                                                                                                              |
| ------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Python Icon](https://skills.thijs.gg/icons?i=python) Python | Linguagem para manipulação dos dados e treinamento dos modelos | Linguagem com maior documentação e suporte para análise de dados e machine learning, incluindo módulos como pandas, dask, sklearn e sktime |

## Referências

AVIATION FACILITIES. **Aircraft Construction: How are airplanes made?** Disponível em: https://www.oxfordsaudia.com/en/blog/aircraft-construction-how-are-airplanes-made/. Acesso em: 09 ago. 2023.

SCIENCE & TECH. **Airplane; aircraft. Also known as: aeroplane, plane.** Disponível em: https://www.britannica.com/technology/airplane. Acesso em: 9 ago. 2023.

HAYGOOD, Joe. **Bleed Air Plane System (How It Works).** Disponível em: https://www.skytough.com/post/bleed-air-plane-system. Acesso em: 9 ago, 2023.

PINTO, Thaís Alves. **Gasolina, Gás Natural e Etanol: Comparação dos Principais Impactos Ambientais da Produção ao Consumo Final.** 2008. Trabalho de Conclusão de Curso (Graduação em Ecologia) - Instituto de Biociências, Universidade Estadual Paulista “Júlio de Mesquita Filho”, Rio Claro, 2008. Orientador: Délcio Luis Semensatto Júnior.

Patri, Om Prasad, Reyna, Nabor , Panangadan, Anand , and Viktor Prasanna. "Predicting Compressor Valve Failures from Multi-Sensor Data." Paper presented at the SPE Western Regional Meeting, Garden Grove, California, USA, April 2015. Disponível em : [https://doi.org/10.2118/174044-MS](https://doi.org/10.2118/174044-MS) Acesso em  15 ago, 2023.
