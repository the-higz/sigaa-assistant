# SIGAA Assistant

Automação para coleta e organização de atividades acadêmicas do SIGAA.

## Objetivo

O projeto tem como objetivo acessar o SIGAA, coletar atividades acadêmicas e organizá-las de forma prática para acompanhamento dos prazos.

## Status

🚧 Em desenvolvimento

Atualmente, o projeto é capaz de:

* realizar login automático no SIGAA;
* coletar atividades acadêmicas;
* estruturar os dados coletados;
* identificar atividades dentro do prazo;
* filtrar atividades ativas;
* gerar um arquivo com as próximas atividades.

## Tecnologias

* Python
* Selenium
* python-dotenv

## Configuração

O projeto utiliza variáveis de ambiente para armazenar as credenciais do SIGAA.

1. Crie uma cópia do arquivo `.env_example` e renomeie para `.env`.
2. Preencha suas credenciais:

```env
SIGAA_USER=seu_usuario
SIGAA_PASSWORD=sua_senha
```

O arquivo `.env` contém informações sensíveis e não deve ser versionado no Git.

## Estrutura do projeto

```text
src/
├── main.py
├── scraper.py
├── processor.py
└── output.py
```

### `scraper.py`

Responsável pelo acesso ao SIGAA, login e coleta das atividades acadêmicas.

### `processor.py`

Responsável pelo processamento e filtragem dos dados coletados.

### `output.py`

Responsável pela geração do arquivo de saída com as atividades.

### `main.py`

Responsável por coordenar o fluxo da aplicação.

## Roadmap

* [ ] Ordenação das atividades por prazo
* [ ] Cálculo do tempo restante para cada atividade
* [ ] Testes automatizados
* [ ] Persistência dos dados
* [ ] Histórico de atividades
* [ ] Notificações de atividades próximas do prazo
* [ ] Análise dos dados acadêmicos
* [ ] Dashboard
* [ ] Entrada manual de provas e atividades
* [ ] Identificação de conteúdos e materiais relacionados
