# SIGAA Assistant

Automação para coleta e organização de atividades acadêmicas do SIGAA.

## Objetivo

O projeto tem como objetivo acessar o SIGAA, coletar atividades acadêmicas e organizá-las de forma prática para acompanhamento dos prazos.

## Status

🚧 Em desenvolvimento

Atualmente, o projeto é capaz de:

* acessar o portal do SIGAA;
* coletar atividades acadêmicas;
* estruturar os dados coletados;
* identificar atividades dentro do prazo;
* filtrar atividades ativas;
* organizar as atividades em um arquivo de saída.

## Tecnologias

* Python
* Selenium

## Estrutura

```text
src/
├── main.py
├── scraper.py
├── processor.py
└── output.py
```

### `scraper.py`

Responsável pela comunicação com o SIGAA e pela coleta das atividades.

### `processor.py`

Responsável pelo processamento e filtragem dos dados coletados.

### `output.py`

Responsável pela geração do arquivo com as atividades.

### `main.py`

Responsável por coordenar o fluxo da aplicação.

## Roadmap

* [ ] Login automático
* [ ] Configuração por `.env`
* [ ] Ordenação por prazo
* [ ] Persistência dos dados
* [ ] Notificações de atividades próximas do prazo
* [ ] Análise dos dados acadêmicos
* [ ] Dashboard
