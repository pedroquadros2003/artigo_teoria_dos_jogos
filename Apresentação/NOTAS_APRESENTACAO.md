# GED-62: Teoria dos Jogos — Notas de Apresentação e Roteiro de Fala Oral
## Trabalho P2: Leilões como Jogos Bayesianos
**Professor:** Darcton Policarpo Damião | **Instituto Tecnológico de Aeronáutica (ITA)**

### Cronograma Rigoroso da Apresentação (Total: 30 minutos)
| Bloco / Seção | Slides | Janela de Tempo | Duração |
| :--- | :---: | :---: | :---: |
| **Abertura e Roteiro** | 1 -- 3 | 00:00 -- 01:30 | 1 min 30 s |
| **Seção 1: Fundamentação Teórica I (Bayesiano)** | 4 -- 7 | 01:30 -- 06:45 | 5 min 15 s |
| **Seção 1: Fundamentação Teórica II (Formatos/RET)** | 8 -- 13 | 06:45 -- 11:30 | 4 min 45 s |
| **Seção 2: Modelo Resolvido (Enunciado)** | 14 -- 15 | 11:30 -- 13:45 | 2 min 15 s |
| **Seção 2: Modelo Resolvido (Derivação/EDO/RET)** | 16 -- 18 | 13:45 -- 21:00 | 7 min 15 s |
| **Seção 3: Caso Real (Ad Exchanges)** | 19 -- 22 | 21:00 -- 25:30 | 4 min 30 s |
| **Seção 4: Ligação com GED-62 e Conclusão** | 23 -- 25 | 25:30 -- 27:00 | 1 min 30 s |
| **Sessão de Arguição / Q&A com Prof. Darcton** | Todos | 27:00 -- 30:00 | 3 min 00 s |
| **TOTAL GERAL** | **25 Slides** | **00:00 -- 30:00** | **30 min 00 s** |

---

## Slide 1: Capa do Trabalho
**Tempo Planejado:** `[⏱ 00:00 -- 00:40]` (40 s)

### Fala Oral Sugerida:
> "Bom dia, professor Darcton, bom dia colegas de turma. Somos o Grupo 5 de Teoria dos Jogos (GED-62), e hoje apresentamos nosso trabalho final sobre **Leilões como Jogos Bayesianos: Lances, Maldição do Vencedor e Equivalência de Receita**. O objetivo desta apresentação é mostrar como a Teoria dos Jogos modela rigorosamente situações em que os agentes tomam decisões estratégicas sob informação incompleta, culminando na aplicação prática aos leilões bilionários de publicidade digital da internet."

---

## Slide 2: Roteiro da Apresentação
**Tempo Planejado:** `[⏱ 00:40 -- 01:15]` (35 s)

### Fala Oral Sugerida:
> "Para cumprir o tempo de 30 minutos com clareza e rigor metodológico, estruturamos nossa exposição em quatro etapas fundamentais: primeiro, a **Fundamentação Teórica**, onde construiremos os conceitos de tipo privado, ENB, os quatro formatos clássicos e o Teorema da Equivalência de Receita; segundo, o **Modelo Resolvido Passo a Passo**, onde demonstraremos a resolução analítica da EDO de equilíbrio e a comparação de receitas; terceiro, o **Caso Real**, analisando as transições de mercado da publicidade online em 2002 e 2019; e, finalmente, a síntese de como este tema expande a ementa de GED-62."

---

## Slide 3: Transição: Conceito e Fundamentação Teórica
**Tempo Planejado:** `[⏱ 01:15 -- 01:30]` (15 s)

### Fala Oral Sugerida:
> "Entramos agora na Seção 1: Conceito e Fundamentação Teórica. A seguir, apresentaremos a formalização matemática que nos permite transitar dos jogos de informação completa para os jogos bayesianos de informação incompleta."

---

## Slide 4: 1.1. Da Informação Completa ao Jogo Bayesiano
**Tempo Planejado:** `[⏱ 01:30 -- 02:45]` (1 min 15 s)

### Fala Oral Sugerida:
> "Na primeira metade de GED-62, estudamos jogos sob a hipótese de informação completa, como o Dilema dos Prisioneiros ou o duopólio de Cournot com custos marginais públicos. Nesses modelos, a matriz de payoffs e as funções de utilidade são de conhecimento comum. Contudo, em transações econômicas reais e em leilões, essa hipótese é insustentável. Quando uma empresa entra num leilão de frequências 5G da Anatel ou de concessão de rodovias, ela conhece com exatidão o seu próprio teto financeiro e sua estrutura de custos, mas os limites dos seus concorrentes são segredos industriais. Estamos, portanto, em um **jogo de informação incompleta**. A grande questão conceitual é: como modelar o equilíbrio quando você nem sequer tem certeza de qual função de payoff o seu adversário está maximizando?"

---

## Slide 5: 1.2. A Transformação de Harsanyi: Tipo Privado e Prior Comum
**Tempo Planejado:** `[⏱ 02:45 -- 04:05]` (1 min 20 s)

### Fala Oral Sugerida:
> "A resposta a esse dilema foi formulada por John Harsanyi em 1967, rendendo-lhe o Prêmio Nobel em 1994. Harsanyi percebeu que poderíamos converter esse jogo de informação incompleta em um jogo de informação imperfeita introduzindo um jogador fictício: a **Natureza**. A Natureza joga primeiro, no 'estágio zero', sorteando para cada jogador um vetor de características secretas, denominado **tipo** θᵢ. No nosso caso de leilões, o tipo nada mais é do que a valoração privada vᵢ do participante. O segundo pilar indispensável é a **Hipótese do Prior Comum**: embora o jogador 1 não saiba exatamente se o rival tirou 20 ou 80 reais, todos compartilham uma crença probabilística comum F(v) sobre como a Natureza sorteia esses valores. Com isso, a incerteza deixa de ser caótica e passa a ser tratada com a teoria das probabilidades e a Regra de Bayes."

---

## Slide 6: 1.3. Estratégia como Função e Equilíbrio de Nash Bayesiano (ENB)
**Tempo Planejado:** `[⏱ 04:05 -- 05:25]` (1 min 20 s)

### Fala Oral Sugerida:
> "Com os tipos definidos, mudamos o conceito de estratégia. Em um jogo tradicional, uma estratégia pura é simplesmente uma ação pontual, como 'Confessar' ou ofertar quantidade q. Em um jogo bayesiano, uma estratégia pura de um participante bᵢ(θᵢ) é uma **regra completa de conduta**: uma função que mapeia cada possível tipo que o jogador poderia ter recebido da Natureza no lance que ele submeterá. É um plano ex-ante: 'se eu tirar 10, dou lance 5; se tirar 80, dou lance 40'. E o **Equilíbrio de Nash Bayesiano (ENB)** ocorre quando essas funções de estratégia são as melhores respostas mútuas. Em relação ao seu próprio tipo, o lance bᵢ*(θᵢ) maximiza seu payoff esperado condicionado à crença bayesiana sobre o que os outros jogadores sortearão e jogarão. Ou seja, ninguém tem incentivo unilateral a desviar da sua função de lance."

---

## Slide 7: 1.4. Ambientes de Leilão: Valores Privados (IPV) vs. Valor Comum (CV)
**Tempo Planejado:** `[⏱ 05:25 -- 06:45]` (1 min 20 s)

### Fala Oral Sugerida:
> "Antes de analisar as regras de leilão, devemos definir o ambiente econômico da mercadoria disputada. A literatura divide os leilões em dois grandes polos. O primeiro é o modelo de **Valores Privados Independentes (IPV)**: nele, a minha valoração vᵢ depende puramente do meu gosto ou benefício pessoal, sem correlação com o gosto dos demais. Se leiloamos uma obra de arte para colecionador ou um doce preferido, o valor que eu atribuo a ela não muda se eu descobrir que outro colega atribui um valor menor ou maior. Já no modelo de **Valor Comum (CV)**, o objeto tem um valor objetivo subjacente V que é idêntico para todos, mas incerto no momento da disputa — como um campo de petróleo do pré-sal ou um lote de ações de uma startup. Cada participante recebe apenas um sinal ou estimativa ruidosa desse valor real. Essa distinção é crucial para entender a dinâmica de lances."

---

## Slide 8: 1.5. Os Quatro Formatos Clássicos e Equivalências Estratégicas
**Tempo Planejado:** `[⏱ 06:45 -- 07:45]` (1 min 00 s)

### Fala Oral Sugerida:
> "William Vickrey, em seu artigo seminal de 1961, catalogou os quatro formatos canônicos de leilão de um único bem: o Leilão Inglês, o Leilão Holandês, o Leilão de Primeiro Preço em envelope selado e o Leilão de Segundo Preço em envelope selado, batizado em sua homenagem como Leilão de Vickrey. Mais importante do que a taxonomia são as duas **equivalências estratégicas fundamentais**: Primeiro, o Leilão Holandês e o de 1º Preço são estrategicamente equivalentes: em ambos, o jogador precisa decidir um único número crítico sem observar lances alheios, enfrentando exatamente a mesma árvore de decisão. Segundo, sob o modelo de Valores Privados, o Leilão Inglês e o de 2º Preço são estrategicamente equivalentes: a melhor conduta no leilão inglês é permanecer ativo até o preço atingir exatamente o seu valor de reserva vᵢ e depois sair, de modo que o vencedor leva o bem pagando um incremento marginal acima do segundo colocado."

---

## Slide 9: 1.6. Como se Joga o 1º Preço? Sombreamento de Lance (Bid Shading)
**Tempo Planejado:** `[⏱ 07:45 -- 08:45]` (1 min 00 s)

### Fala Oral Sugerida:
> "Vejamos agora o comportamento estratégico no Leilão de Primeiro Preço. Aqui vale uma regra de ouro: ninguém jamais deve ofertar a sua verdadeira valoração! Se você tem valoração de 100 reais e oferta 100, no caso de vitória o seu lucro econômico é 100 - 100 = 0! Portanto, os participantes praticam o chamado **Sombreamento de Lance (Bid Shading)**: reduzem o lance deliberadamente abaixo de vᵢ. Isso cria o trade-off fundamental dos leilões de 1º preço: se eu aumento meu lance, aumento minha probabilidade de vencer a disputa; porém, diminuo minha margem unitária de lucro (vᵢ - bᵢ). Se eu diminuo o lance para abocanhar um lucro maior se vencer, corro um risco severo de ser superado por um concorrente. O equilíbrio bayesiano calcula exatamente o ponto de tangência ótimo que balanceia essas duas forças opostas."

---

## Slide 10: 1.7. Como se Joga o 2º Preço (Vickrey)? Revelação Sincera
**Tempo Planejado:** `[⏱ 08:45 -- 09:45]` (1 min 00 s)

### Fala Oral Sugerida:
> "Já no Leilão de Segundo Preço de Vickrey, a mecânica é completamente diferente e brilhante. A estratégia ótima é a **Revelação Sincera (Truthful Bidding)**: ofertar exatamente bᵢ = vᵢ é uma estratégia fracamente dominante. Por que isso acontece? Porque a regra de pagamento do leilão **desacopla** o valor do seu lance do montante que você efetivamente desembolsa! O seu lance bᵢ serve apenas para decidir se você vence ou perde; o que você paga é determinado exclusivamente pelo lance do segundo colocado. Se você tentar dar um lance menor do que seu valor, sua margem de lucro nos casos em que vence não aumenta nem um centavo, mas você corre o risco de perder negócios onde o segundo preço estaria abaixo do seu valor. E se der um lance acima de vᵢ, você só altera o resultado quando o segundo lance estiver acima do seu valor, gerando lucro negativo! Logo, a sinceridade é a melhor resposta contra absolutamente qualquer comportamento dos adversários."

---

## Slide 11: 1.8. Teorema da Equivalência de Receita (RET)
**Tempo Planejado:** `[⏱ 09:45 -- 10:30]` (45 s)

### Fala Oral Sugerida:
> "Isso nos leva a uma das descobertas mais profundas de toda a microeconomia: o **Teorema da Equivalência de Receita (RET)**, provado por Vickrey e generalizado por Roger Myerson (Nobel 2007). O teorema afirma que, sob quatro condições estritas — compradores neutros ao risco, valores privados independentes sorteados da mesma distribuição contínua e estritamente crescente, alocação eficiente ao maior valor e lance nulo para o pior tipo —, **qualquer mecanismo padrão de leilão gera exatamente a mesma receita esperada para o vendedor**! Ou seja, embora no 1º preço os lances sejam sombreados e no 2º preço os lances sejam sinceros, a média arrecadada pelo leiloeiro no final do dia é rigorosamente idêntica."

---

## Slide 12: 1.9. Validação Computacional (Monte Carlo) e Quebras do RET
**Tempo Planejado:** `[⏱ 10:30 -- 11:05]` (35 s)

### Fala Oral Sugerida:
> "Para checar esse resultado, desenvolvemos uma simulação de Monte Carlo em Python, simulando 100.000 leilões com dois compradores tirando valorações uniformes entre 0 e 100 reais. Como o gráfico demonstra, a receita média simulada no 1º preço foi de R$ 33,31 e no 2º preço foi de R$ 33,33 — convergindo com precisão de centavos para a previsão teórica exata de R$ 33,33. Porém, no mundo real, o RET quebra quando suas hipóteses são violadas: compradores avessos ao risco preferem pagar mais no 1º preço para garantir a vitória, assimetrias entre concorrentes destroem a equivalência, e a correlação entre estimativas altera as receitas arrecadadas."

---

## Slide 13: 1.10. A Maldição do Vencedor (Winner's Curse)
**Tempo Planejado:** `[⏱ 11:05 -- 11:30]` (25 s)

### Fala Oral Sugerida:
> "Para encerrar a parte conceitual, destacamos a **Maldição do Vencedor** no ambiente de Valor Comum. Se o valor do objeto é único, mas todos possuem estimativas com ruído, o participante que vence o leilão é necessariamente aquele que teve a estimativa mais otimista de todas. Se ele não antecipar essa distorção estatística e não 'sombrear' seu lance para baixo em função da quantidade de adversários, ele vencerá a disputa apenas para amargar um prejuízo financeiro certo."

---

## Slide 14: Transição: Modelo Resolvido Passo a Passo
**Tempo Planejado:** `[⏱ 11:30 -- 11:50]` (20 s)

### Fala Oral Sugerida:
> "Entramos agora na Seção 2: o **Modelo Resolvido Passo a Passo**. Aqui atenderemos diretamente ao enunciado formal solicitado para a avaliação de GED-62, deduzindo a equação diferencial ordinária de equilíbrio e provando matematicamente o Teorema da Equivalência de Receita."

---

## Slide 15: 2.1. Modelo Resolvido: Enunciado e Formulação
**Tempo Planejado:** `[⏱ 11:50 -- 13:45]` (1 min 55 s)

### Fala Oral Sugerida:
> "O problema proposto é o clássico de Vickrey (1961) e Klemperer (2004): temos dois participantes simétricos disputando um único bem indivisível. A Natureza sorteia as valorações v₁ e v₂ de forma independente a partir de uma distribuição Uniforme no intervalo [0, 1]. Portanto, a densidade é f(v) = 1 e a acumulada é F(v) = v. Os jogadores são neutros ao risco e os envelopes são selados. Buscamos um **Equilíbrio de Nash Bayesiano Simétrico** em estratégias puras e estritamente crescentes, onde ambos adotam uma mesma função de lance bᵢ = β(vᵢ), com condição de contorno natural β(0) = 0. Nosso objetivo nas próximas três lâminas é derivar analiticamente a forma funcional de β(v) para o 1º preço e demonstrar formalmente a igualdade das receitas esperadas entre 1º e 2º preço."

---

## Slide 16: 2.2. Derivação do Equilíbrio no 1º Preço — Passos 1 e 2
**Tempo Planejado:** `[⏱ 13:45 -- 16:15]` (2 min 30 s)

### Fala Oral Sugerida:
> "Vamos acompanhar a derivação matemática passo a passo. No **Passo 1**, calculamos a probabilidade de vitória do Jogador 1 quando ele submete um lance b₁ qualquer. Assumindo que o Jogador 2 joga a estratégia de equilíbrio β(v₂), o Jogador 1 vence se seu lance for maior que b₂, ou seja, se b₁ > β(v₂). Como supomos que β é estritamente crescente, ela possui uma inversa bem-definida β⁻¹. Aplicando a inversa em ambos os lados da desigualdade, a condição de vitória torna-se: v₂ < β⁻¹(b₁). Como v₂ segue uma distribuição Uniforme em [0, 1], a probabilidade de v₂ ser menor que esse limite é a própria função acumulada F, que é a própria inversa: Probabilidade de Vitória = β⁻¹(b₁). No **Passo 2**, escrevemos a função de lucro esperado do Jogador 1, denotada por Π₁(b₁). O lucro esperado é a probabilidade de vencer multiplicada pela margem econômica líquida em caso de vitória: Π₁(b₁) = (v₁ - b₁) · β⁻¹(b₁). Observem a beleza dessa equação: o termo (v₁ - b₁) é a margem de lucro, que cai quando o lance sobe; já o termo β⁻¹(b₁) é a probabilidade de vitória, que sobe quando o lance sobe. É o trade-off fundamental!"

---

## Slide 17: 2.3. Derivação do Equilíbrio no 1º Preço — Passos 3 e 4 (CPO e EDO)
**Tempo Planejado:** `[⏱ 16:15 -- 18:45]` (2 min 30 s)

### Fala Oral Sugerida:
> "Passamos agora aos Passos 3 e 4, o coração da demonstração. No **Passo 3**, o Jogador 1 escolhe b₁ para maximizar seu lucro esperado. Derivamos Π₁ em relação a b₁ pela regra do produto e igualamos a zero: A derivada de (v₁ - b₁) é -1, multiplicada por β⁻¹(b₁); somamos com (v₁ - b₁) multiplicado pela derivada da inversa (β⁻¹)'(b₁). Pelo teorema da função inversa do cálculo, a derivada de β⁻¹(b₁) é 1 / β'(v₁). Agora vem o argumento central do Equilíbrio de Nash: em equilíbrio, o Jogador 1 de tipo v₁ deve achar ótimo escolher exatamente o lance b₁ = β(v₁). Portanto, β⁻¹(b₁) é o próprio v₁! Substituindo essas relações na CPO e multiplicando ambos os lados por β'(v₁), chegamos a: (v₁ - β(v₁)) = v₁ · β'(v₁). Reorganizando os termos no **Passo 4**, obtemos a EDO linear de primeira ordem: β'(v₁) · v₁ + β(v₁) = v₁. Reconhecemos no lado esquerdo a derivada do produto: d/dv₁ [v₁ · β(v₁)] = v₁. Integrando ambos os lados de 0 a v₁ com β(0) = 0, temos: v₁ · β(v₁) = v₁² / 2. Dividindo por v₁, encontramos a solução única: β(v₁) = 1/2 v₁! E quando generalizamos essa mesma EDO para n concorrentes, encontramos β(v) = (n-1)/n · v. Com 2 jogadores, você oferta metade da sua valoração; com 10 jogadores, você oferta 90% da sua valoração."

---

## Slide 18: 2.4. Comparação da Receita Esperada: 1º Preço vs. 2º Preço
**Tempo Planejado:** `[⏱ 18:45 -- 21:00]` (2 min 15 s)

### Fala Oral Sugerida:
> "Para concluir a demonstração, comparamos a receita arrecadada pelo leiloeiro nos dois formatos. No Leilão de 1º Preço, o vencedor é aquele com maior valoração max{v₁, v₂}, e ele paga metade do seu valor: R₁º = 1/2 · max{v₁, v₂}. A função densidade do máximo de duas variáveis uniformes é dada pela primeira estatística de ordem: f_max(v) = 2v. Calculando a esperança: E[R₁º] = 1/2 · ∫₀¹ v · (2v) dv = ∫₀¹ v² dv = [v³/3]₀¹ = 1/3! No Leilão de 2º Preço, ambos revelam sinceramente bᵢ = vᵢ, e o vencedor paga o lance do perdedor, que é o mínimo min{v₁, v₂}. A densidade da segunda estatística de ordem é f_min(v) = 2(1 - v). Calculando a esperança: E[R₂º] = ∫₀¹ v · 2(1 - v) dv = 2 [v²/2 - v³/3]₀¹ = 2 (1/6) = 1/3! As duas receitas esperadas são rigorosamente iguais a 1/3 de real! E a intuição geométrica é fabulosa: n números uniformes em [0, 1] dividem o intervalo em n+1 fatias estatisticamente idênticas, cada uma de tamanho 1/(n+1). O segundo maior valor fica exatamente na posição n-1 fatias da base, ou seja, (n-1)/(n+1). Com n=2, temos 3 fatias de 1/3, e a receita é exatamente 1/3. O Teorema da Equivalência de Receita está demonstrado."

---

## Slide 19: Transição: Caso Real: Leilões de Anúncios Online
**Tempo Planejado:** `[⏱ 21:00 -- 21:15]` (15 s)

### Fala Oral Sugerida:
> "Entramos agora na Seção 3: o **Caso Real da Publicidade Digital**. Veremos como essa teoria elegante se traduziu na infraestrutura tecnológica que movimenta centenas de bilhões de dólares por ano no Google, na Meta e em todo o ecossistema de Ad Exchanges."

---

## Slide 20: 3.1. Caso Real: Anúncios Online e a Mudança de 2002 (1º → 2º Preço)
**Tempo Planejado:** `[⏱ 21:15 -- 22:45]` (1 min 30 s)

### Fala Oral Sugerida:
> "Nos primórdios dos motores de busca, entre 1997 e 2002, a empresa pioneira era a Overture (depois Yahoo!). A Overture utilizava um leilão de Primeiro Preço clássico com lances abertos para vender links patrocinados. O que aconteceu na prática foi um caos de engenharia: anunciantes concorrentes implementaram robôs de software programados para monitorar os lances a cada segundo e cobrir o rival por apenas 1 centavo. Se o rival ofertava 1 real, o outro bot dava 1,01 real. O primeiro bot via isso e dava 1,02 real. Isso continuava até um deles desistir, o preço despencava para o piso, e o ciclo recomeçava do zero. Esse comportamento gerava o chamado **padrão de dente de serra** (sawtooth pattern), que sobrecarregava os servidores com milhões de requisições inúteis por minuto. Em 2002, o Google revolucionou o mercado ao lançar o AdWords adotando o mecanismo de **Generalized Second Price (GSP)**, uma generalização do Leilão de Vickrey para múltiplos espaços publicitários. Como no 2º preço a estratégia ótima é revelar o lance sincero, a volatilidade ruiu e o mercado atingiu estabilidade."

---

## Slide 21: 3.2. A Mudança de 2019: Por que o Mercado Voltou do 2º para o 1º Preço?
**Tempo Planejado:** `[⏱ 22:45 -- 24:10]` (1 min 25 s)

### Fala Oral Sugerida:
> "Se o leilão de 2º preço era tão estável, por que em 2019 o Google Ad Manager e as grandes plataformas de ad exchange fizeram a transição histórica de volta para o leilão de Primeiro Preço? A literatura econômica e o artigo de Despotakis, Ravi e Sayedi (2021) apontam duas razões centrais. A primeira foi o surgimento do **Header Bidding**: múltiplos leilões de 2º preço rodando em paralelo no navegador do usuário antes de enviar o lance final ao servidor do Google. Em leilões paralelos encadeados, o 2º preço perde sua eficiência alocativa. A segunda razão foi a perda de confiança na integridade do leiloeiro, a chamada **trapaça dos pisos suaves (Soft Floors)**. No leilão de 2º preço, intermediários que organizavam o leilão viam o lance máximo do vencedor e secretamente criavam um piso de reserva logo abaixo dele, cobrando quase o valor total do 1º preço enquanto fingiam operar um leilão de 2º preço! A migração para o 1º preço em 2019 eliminou essa opacidade: no 1º preço, o que você oferta é exatamente o que você paga, tornando o processo transparente e auditável."

---

## Slide 22: 3.3. Modelagem Formal do Caso Real como Jogo Bayesiano
**Tempo Planejado:** `[⏱ 24:10 -- 25:30]` (1 min 20 s)

### Fala Oral Sugerida:
> "Para consolidar o caso real sob a ótica de GED-62, estruturamos a publicidade programática como um Jogo Bayesiano formal: Os **Jogadores** são os n anunciantes concorrentes; O **Tipo** θᵢ de cada anunciante é uma tupla composta por sua valoração econômica por conversão vᵢ e sua taxa prevista de cliques (CTR), sorteada da distribuição de mercado F(v); As **Ações** são os lances bᵢ submetidos via API em frações de milissegundo; E a **Função de Payoff** reflete a alocação do espaço: o vencedor com maior lance efetivo ganha a impressão e recebe payoff uᵢ = vᵢ - bᵢ no 1º preço, ou uᵢ = vᵢ - b₍₂₎ no 2º preço. Com isso, provamos que a modelagem matemática que deduzimos passo a passo nos slides governa na prática uma indústria de 600 bilhões de dólares."

---

## Slide 23: Transição: Ligação com a Disciplina GED-62 e Conclusões
**Tempo Planejado:** `[⏱ 25:30 -- 25:45]` (15 s)

### Fala Oral Sugerida:
> "Entramos agora na Seção 4: a **Síntese do Trabalho e a Ligação Direta com a Disciplina GED-62**. Vamos recapitular como os tópicos desenvolvidos fecham com chave de ouro os conceitos fundamentais do nosso curso."

---

## Slide 24: 4. Ligação com o Curso GED-62 e Conclusão
**Tempo Planejado:** `[⏱ 25:45 -- 26:45]` (1 min 00 s)

### Fala Oral Sugerida:
> "Para concluir, gostaríamos de enfatizar o que o estudo de leilões bayesianos acrescenta à nossa formação em GED-62: Primeiro, **supera a hipótese restritiva de informação completa**. A transformação de Harsanyi nos equipa com o ferramental para modelar incerteza estratégica em finanças, engenharia de defesa e licitações públicas. Segundo, **expande o conceito de estratégia** de uma ação pontual para uma função contínua de envelope bᵢ(vᵢ), conectando Teoria dos Jogos com Cálculo Variacional e Equações Diferenciais. E terceiro, estabelece a ponte direta com o **Design de Mecanismos** de Hurwicz, Maskin e Myerson: a engenharia reversa dos jogos, onde o projetista escolhe as regras para induzir equilíbrios socialmente eficientes e arrecadatórios. A teoria de leilões é a maior prova de que a Teoria dos Jogos é a base operacional da economia digital contemporânea."

---

## Slide 25: Referências Bibliográficas e Encerramento
**Tempo Planejado:** `[⏱ 26:45 -- 27:00]` (15 s)

### Fala Oral Sugerida:
> "Aqui estão as referências bibliográficas da literatura seminal e dos artigos empíricos que embasaram nossa apresentação. Agradecemos profundamente ao professor Darcton Damião pela condução exemplar da disciplina ao longo do semestre e à atenção de todos os colegas. Estamos agora integralmente à disposição do professor e da turma para a sessão de arguição e perguntas."

---
