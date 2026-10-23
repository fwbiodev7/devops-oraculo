# Oráculo DevOps

[![Oráculo](https://github.com/fwbiodev7/devops-oraculo/actions/workflows/oraculo.yml/badge.svg)](https://github.com/fwbiodev7/devops-oraculo/actions/workflows/oraculo.yml)

Repositório: [fwbiodev7/devops-oraculo](https://github.com/fwbiodev7/devops-oraculo).

Programa em Python que sorteia uma previsão para programadores. O GitHub Actions testa e executa o código na nuvem, sem precisar executar Python no computador.

## Pipeline

O workflow é acionado a cada push, manualmente pelo botão **Run workflow** ou pelo agendamento. Os passos são: baixar o código, instalar o Python 3.12, rodar os testes e publicar a previsão no Summary. Os testes conferem se há pelo menos cinco previsões e se o resultado sorteado pertence à lista.

## Respostas da questão 4

**a) No Passo 6, o passo “Consultar o oráculo” chegou a ser executado? Por que isso é uma vantagem do CI?**

Não. Com apenas três previsões, o primeiro assert falha com `AssertionError: Poucas previsões!`. O passo “Rodar os testes” termina com erro e o próximo passo é pulado. A vantagem da integração contínua (CI) é detectar automaticamente quando uma mudança quebra uma regra do projeto e impedir que as etapas seguintes usem o código com erro. Em um pipeline com CD, os testes também podem ser uma condição antes do deploy.

**b) Cite uma situação real em que você usaria o GitHub Actions para automatizar algo.**

Eu usaria em um projeto de site feito em grupo na escola. A cada push, um workflow executaria os testes e verificaria se o site consegue ser gerado. Depois da aprovação dos testes na branch principal, outro passo poderia fazer o deploy. Assim, o grupo perceberia os erros cedo e automatizaria tarefas repetitivas, aplicando práticas de DevOps.

## Desafio bônus

O agendamento `0 11 * * 1-5` usa cinco campos:

| Campo | Valor | Significado |
| --- | --- | --- |
| Minuto | `0` | No minuto zero |
| Hora | `11` | Às 11h UTC, equivalentes a 8h de Brasília (UTC-3) |
| Dia do mês | `*` | Qualquer dia do mês |
| Mês | `*` | Qualquer mês |
| Dia da semana | `1-5` | De segunda a sexta |

O workflow agendado usa a branch padrão do repositório. O horário é o agendamento solicitado; o GitHub pode atrasar o início em períodos de maior carga.

## Fontes

- [GitHub Docs — sintaxe de workflows e cron](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onschedule)
- [GitHub Docs — condições de status dos passos](https://docs.github.com/en/actions/learn-github-actions/expressions#status-check-functions)
- [GitHub Docs — eventos que acionam workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
