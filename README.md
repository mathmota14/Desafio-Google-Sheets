# Desafio Google Sheets

Dado a planilha no [Google Sheets](https://docs.google.com/spreadsheets/d/13K1VCIX41I8HVpdllr_9Si6jhUVhL7awRkBRrVhcYnY/edit#gid=0) ou com a mesma estrutura é necessário calcular a situação de cada aluno baseado na média das 3 provas (P1, P2, P3):

- Se média < 50, então $\color{#eb5252}{\textsf{Reprovado por Nota}}$
- Se 50 <= média < 70, então $\color{#eded0c}{\textsf{Exame Final}}$
- Se média >= 70, então $\color{#19cf20}{\textsf{Aprovado}}$
- Se o número de faltas ultrapasse 25% do número total de aulas o aluno terá a situação $\color{#eb5252}{\textsf{Reprovado por Falta}}$, independente da média

Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final" (naf) de  cada aluno de acordo com seguinte fórmula: 

$$ 50 <= {média +  naf \over 2} $$

Caso a situação do aluno seja diferente de "Exame Final", o campo "Nota para  Aprovação Final" será 0.

## Instruções para utilizar

1- Entre no [Console Google Developer](https://console.developers.google.com/)

2- Clique em "Selecione um projeto"

![image](https://github.com/mathmota14/Desafio-Google-Sheets/assets/92896528/39ed0f94-5c6e-459d-b812-7cd4827c028e)

3- Clique em "Novo projeto" e crie um novo

4- Você será redirecionado para a mesma tela do 1° passo, em seguida clique em "Tela de permissão OAuth"

![image](https://github.com/mathmota14/Desafio-Google-Sheets/assets/92896528/037e7ee4-d9e4-4dc0-ac97-8a01ecb656b0)

5- Preencha todos os campos obrigatórios e em "Usuários de teste" coloque todos os emails que você poderá usar. OBS: Na parte "Nome do app" coloque o mesmo nome que foi colocado na criação do projeto no 3° passo para evitar erros

6- Depois de configurado vá para a aba "Credenciais" que fica acima da "Tela de permissão OAuth" como visto na imagem do 4° passo e clique em "Criar credenciais > ID do client OAuth". Em "Tipo de aplicativo" selecione App para computador e em "Nome" coloque um de sua preferência

7- Após o 6° passo irá aparece um popup e depois só clicar em "Fazer download do JSON" e será baixado um arquivo JSON que será necessário para a realização do desafio, além disso renomeie o nome do arquivo baixado para "credentials.json" e coloque esse arquivo na mesma pasta onde está o arquivo python presente no repositório

![image](https://github.com/mathmota14/Desafio-Google-Sheets/assets/92896528/53f29cdd-b253-449e-bd4f-eb004332ae64)

8- Se ao executar o challenge.py não consiga conectar na [planilha exemplo no Google Sheets](https://docs.google.com/spreadsheets/d/13K1VCIX41I8HVpdllr_9Si6jhUVhL7awRkBRrVhcYnY/edit#gid=0), faça uma cópia da planilha e mude o SAMPLE_SPREADSHEET_ID para o ID da planilha copiada. Além disso, caso queira adicionar mais linhas sempre lembre de atualizar no SAMPLE_RANGE_NAME, que no caso dessa planilha é A2:H27

![image](https://github.com/mathmota14/Desafio-Google-Sheets/assets/92896528/b7779f45-be42-4949-a4b9-c0c6a7b20b02)

![image](https://github.com/mathmota14/Desafio-Google-Sheets/assets/92896528/8c3a9e3f-ad95-4632-907d-e791001f68b6)

OBS: Ao executar o challenge.py você terá 3 arquivos na pasta que você selecionou: challenge.py, credentials.json e token.json.
