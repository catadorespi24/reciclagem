# Aplicação de Catadores de Coleta de Reciclagem

## Descrição
Essa aplicação visa conectar catadores de materiais recicláveis com pessoas e empresas que desejam descartar resíduos recicláveis de forma responsável. A ideia é facilitar a coleta, garantindo que os materiais cheguem ao destino correto e incentivando práticas sustentáveis.

## Funcionalidades
- **Cadastro de Catadores:** Permite que catadores de reciclagem se cadastrem na plataforma, informando seus dados de contato, regiões de atuação e tipos de materiais que coletam.
- **Solicitação de Coleta:** Usuários podem solicitar a coleta de materiais recicláveis, especificando o tipo de resíduo e a quantidade disponível.
- **Geolocalização:** Utiliza geolocalização para mostrar catadores disponíveis nas proximidades e possibilitar a combinação de coletas eficientes.
- **Notificações:** Envio de notificações para catadores sobre novas solicitações de coleta e para usuários sobre a chegada do catador.
- **Histórico de Coletas:** Registro de todas as coletas realizadas, permitindo um acompanhamento do impacto ambiental gerado.

## Tecnologias Utilizadas
- **Front-end:** flutter
- **Back-end:** Node
- **Banco de Dados:** MongoDB
- **Geolocalização:** Google Maps API
- **Notificações:** Firebase Cloud Messaging

## Arquitetura

```cleancode
         Usuário         Catador
           |                |
           |   client   |
           |<--------------->|
           |                |
           |                |
           |   repository   |
           |<--------------->|
           |                |
           |                |
           | controller|
           |<--------------->|
           |                |
         Plataforma (Back-end)
