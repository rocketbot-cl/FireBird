



# FireBird
  
Conecte-se a um banco de dados Firebird; criar tabelas; inserir ou atualizar dados; faça consultas personalizadas.  

  
*Read this in other languages: [English](Manual_FireBird.md), [Português](Manual_FireBird.pr.md), [Español](Manual_FireBird.es.md)*  

  
![banner](imgs/Banner_FireBird.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar
  
Conecte-se a um banco de dados Firebird.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|DSN (Data Source Name)||[host[/port]]:database|
|Nome de usuário||ISC_USER|
|Senha||Valor Predeterminado ISC_PASSWORD|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Consulta
  
Execute uma consulta personalizada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Query||SELECT <column>, <column> FROM <table> WHERE <column> = <value> ...|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Atualizar
  
Fazer alterações em uma tabela de banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da tabela||Tablea|
|Novo valor por cabeçalho/coluna||{header_1: value_1, header_2: value_2}|
|Condicionais||{header_3: condition}|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Inserir
  
Insira um registro em uma tabela de banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da tabela||Tablea|
|Cabeçalhos de tabela||Nombre,Dirección|
|Valores a inserir||1, 'Will'|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Criar Tabela
  
Criar uma tabela dentro do banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da tabela||Tablea|
|Coluna e tipo de dados||Nome varchar(20),NúmeroEmpregado int|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Excluir Tabela
  
Exclua uma tabela existente no banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da tabela||Tablea|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Selecione Tabela
  
Recuperar dados de uma tabela inteira do banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da tabela||Tablea|
|Sessão||Conn1|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Fechar conexão
  
Feche a conexão com o banco de dados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão||Conn1|
