Tudo que eu aprendi até o seguinte momento 13/05/2025 em arquitetura de rede IOT


## Infraestrutura de Redes: Ativos e Passivos

A infraestrutura de rede sustenta a comunicação corporativa e residencial. Ela é dividida estritamente em componentes que processam dados e componentes que servem de meio físico.

### Ativos de Rede

Equipamentos lógicos que gerenciam, direcionam e processam o tráfego de dados na rede.

Switch: Conecta dispositivos em uma rede local (LAN). Direciona pacotes usando endereços MAC. Reduz colisões de dados.

Roteador: Conecta redes distintas (LAN à WAN). Encaminha pacotes com base em endereços IP. Determina a melhor rota para os dados.

Access Point (AP): Converte o sinal cabeado em ondas de rádio (Wi-Fi). Permite a conexão sem fio de dispositivos móveis.

Firewall: Monitora e filtra o tráfego de entrada e saída. Aplica regras de segurança para bloquear acessos não autorizados.

### Passivos de Rede

Componentes físicos que servem de suporte para a transmissão. Não processam nem alteram as informações.

Cabo UTP (Par Trançado): Meio de cobre para redes Ethernet. Limitado a 100 metros de distância por segmento. Sensível a interferências eletromagnéticas.

Fibra Óptica: Transmite dados via pulsos de luz. Imune a interferências. Indicada para longas distâncias e altíssima velocidade.

Conector RJ-45: Interface padrão que finaliza os cabos UTP para encaixe nos ativos.

Patch Panel: Painel de conexões centrais fixas. Organiza a transição entre o cabeamento horizontal e os ativos do rack.

Rack: Gabinete metálico padrão (geralmente de 19 polegadas). Protege fisicamente e organiza os equipamentos contra poeira e calor.

---

## Internet e suas Derivações

A internet é uma infraestrutura global baseada na comutação de pacotes e no conjunto de protocolos TCP/IP. Ela possui divisões claras quanto à acessibilidade e indexação.

### Divisões Principais

Surface Web: Camada visível e pública da internet. Sites indexados por motores de busca comuns (Google, Bing). Representa menos de 5% do total.

Deep Web: Conteúdo não indexado por motores de busca. Exige credenciais ou URLs diretas para acesso. Composta por bancos de dados privados, internet banking, e-mails e prontuários médicos. É legal e segura.

Dark Web: Subconjunto oculto dentro da Deep Web. Exige softwares específicos (como o navegador Tor) e domínios `.onion`. Prioriza o anonimato total por criptografia em camadas. Abriga comunicações governamentais sigilosas, jornalismo investigativo e mercados ilegais.


##  Ecossistema IoT: Protocolo MQTT e Driver ESP32

A Internet das Coisas (IoT) conecta objetos físicos à internet para automação e coleta de dados em tempo real.

### Protocolo MQTT (Message Queuing Telemetry Transport)

Protocolo de mensagens leve baseado na arquitetura Publicador/Inscrito (Publish/Subscribe). Projetado para redes de baixa largura de banda e dispositivos com restrição de processamento.

 Broker: O servidor central que recebe as mensagens, filtra por tópicos e as distribui para os clientes inscritos.

Tópicos (Topics): Strings separadas por barras usadas para categorizar mensagens (Ex: `casa/sala/temperatura`).

QoS (Quality of Service): Níveis de garantia de entrega de mensagens (0: No máximo uma vez; 1: Pelo menos uma vez; 2: Exatamente uma vez).

### Microcontrolador e Driver ESP32
O ESP32 é um chip de baixo custo e baixo consumo com Wi-Fi e Bluetooth integrados, amplamente utilizado como nó de borda em IoT.

Driver de Comunicação USB-Serial: Para programar o ESP32 via computador, é necessário instalar drivers específicos no sistema operacional (geralmente CP210x ou CH340). Eles criam uma porta COM virtual para comunicação de dados.

Firmware e Bibliotecas: O código-fonte utiliza bibliotecas como `WiFi.h` (para conexão ao ponto de acesso) e `PubSubClient.h` (para conectar, publicar e assinar tópicos no Broker MQTT).

---

## Conclusão do Relatório

A modernização industrial e residencial exige a convergência dessas tecnologias. Os componentes passivos e ativos de rede garantem a estabilidade física e lógica do sinal. Essa estrutura viabiliza o tráfego da Internet, que por sua vez serve de estrada para o fluxo de dados de sensores baseados em ESP32. Por fim, o protocolo MQTT otimiza esse tráfego, permitindo que microcontroladores enviem leituras de campo para servidores na nuvem de forma ágil e segura.


