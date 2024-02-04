# Desafio Google Sheets

Dado a planilha no [Google Sheets](https://docs.google.com/spreadsheets/d/13K1VCIX41I8HVpdllr_9Si6jhUVhL7awRkBRrVhcYnY/edit#gid=0) ou com a mesma estrutura é necessário calcular a situação de cada aluno baseado na média das 3 provas (P1, P2, P3):

- Se média < 5, então <span style= "color: #eb5252"> Reprovado por Nota</span>
- Se 5 <= média < 7, então <span style= "color: #eded0c"> Exame Final</span>
- Se média >= 7, então <span style= "color: #19cf20"> Aprovado</span>
- Se o número de faltas ultrapasse 25% do número total de aulas o aluno terá a situação <span style= "color: #eb5252"> Reprovado por Falta</span>, independente da média

Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final" (naf) de  cada aluno de acordo com seguinte fórmula: 

$$ 5 <= {média +  naf \over 2} $$

Caso a situação do aluno seja diferente de "Exame Final", o campo "Nota para  Aprovação Final" será 0.

## Instruções para utilizar

1- Entre no [Console Google Developer](https://console.developers.google.com/)

2- Clique em "Selecione um projeto"

<img alt="image" src="https://gist.github.com/assets/92896528/c479fecd-8510-4299-8363-3ad0f17f7068">

3- Clique em "Novo projeto" e crie um novo

4- Você será redirecionado para a mesma tela do 1° passo, em seguida clique em "Tela de permissão OAuth"

<img alt="image" src="https://gist.github.com/assets/92896528/77076448-bb4a-40b1-bde1-bccc72478fae">

5- Preencha todos os campos obrigatórios e em "Usuários de teste" coloque todos os emails que você poderá usar. OBS: Na parte "Nome do app" coloque o mesmo nome que foi colocado na criação do projeto no 3° passo para evitar erros

6- Depois de configurado vá para a aba "Credenciais" que fica acima da "Tela de permissão OAuth" como visto na imagem do 4° passo e clique em "Criar credenciais > ID do client OAuth". Em "Tipo de aplicativo" selecione App para computador e em "Nome" coloque um de sua preferência

7- Após o 6° passo irá aparece um popup e depois só clicar em "Fazer download do JSON" e será baixado um arquivo JSON que será necessário para a realização do desafio, além disso renomeie o nome do arquivo baixado para "credentials.json" e coloque esse arquivo na mesma pasta onde está o arquivo python presente no repositório

<img alt="image" src="https://gist.github.com/assets/92896528/91f0fd57-aee8-481d-a27a-e858876665e6">

8- Se ao executar o challenge.py não consiga conectar na [planilha exemplo no Google Sheets](https://docs.google.com/spreadsheets/d/13K1VCIX41I8HVpdllr_9Si6jhUVhL7awRkBRrVhcYnY/edit#gid=0), faça uma cópia da planilha e mude o SAMPLE_SPREADSHEET_ID para o ID da planilha copiada. Além disso, caso queira adicionar mais linhas sempre lembre de atualizar no SAMPLE_RANGE_NAME, que no caso dessa planilha é A2:H27

<img alt="image" src="https://gist.github.com/assets/92896528/0e1a377b-c525-472e-b868-91cf2878dfeb">

<img alt="image" src="https://gist.github.com/assets/92896528/663625a4-8495-4e50-8b0c-5368c0bfcf3a">

OBS: Ao executar o challenge.py você terá 3 arquivos na pasta que você selecionou: challenge.py, credentials.json e token.json.