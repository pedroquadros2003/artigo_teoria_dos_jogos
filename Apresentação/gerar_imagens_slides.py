#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera todas as figuras vetoriais (.pdf) da apresentação em Apresentação/Imagens/
usando pdflatex + TikZ standalone, garantindo fontes idênticas aos slides.
"""

import os
import subprocess

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Imagens")
os.makedirs(IMG_DIR, exist_ok=True)

PREAMBLE = r"""\documentclass[tikz,border=4pt]{standalone}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,patterns,decorations.pathreplacing}
\definecolor{itaNavy}{RGB}{15, 38, 74}
\definecolor{itaBlue}{RGB}{29, 78, 216}
\definecolor{itaLightBlue}{RGB}{219, 234, 254}
\definecolor{itaRed}{RGB}{185, 28, 28}
\definecolor{itaLightRed}{RGB}{254, 226, 226}
\definecolor{itaGreen}{RGB}{5, 120, 87}
\definecolor{itaLightGreen}{RGB}{209, 250, 229}
\definecolor{itaAmber}{RGB}{180, 83, 9}
\definecolor{itaLightAmber}{RGB}{254, 243, 199}
\definecolor{itaGray}{RGB}{71, 85, 105}
\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""

FIGURES = {
    "harsanyi_tipos_prior": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=0.95]
  % Painel (a): Simétrico
  \begin{scope}[shift={(0,0)}]
    \node[font=\sffamily\bfseries\footnotesize, text=itaNavy, align=center] at (2.1, 2.75) {(a) Simétrico ($F_1 = F_2$)\\{\scriptsize Ex.: João e Lucas ($U[0,100]$)}};
    \draw[->, thick, itaGray] (0,0) -- (4.1,0) node[right, font=\scriptsize] {$v_i$};
    \draw[->, thick, itaGray] (0,0) -- (0,2.0) node[left, font=\scriptsize] {$f(v_i)$};
    \fill[itaLightBlue] (0.25,0) rectangle (3.55, 1.35);
    \draw[itaBlue, ultra thick] (0.25,0) -- (0.25,1.35) -- (3.55,1.35) -- (3.55,0);
    \node[below, font=\scriptsize] at (0.25,0) {$0$};
    \node[below, font=\scriptsize] at (3.55,0) {$100$ (R\$)};
    \node[text=itaBlue, font=\scriptsize\bfseries] at (1.9, 0.68) {$F_1 = F_2 \sim U[0,100]$};
  \end{scope}

  % Painel (b): Assimétrico
  \begin{scope}[shift={(5.3,0)}]
    \node[font=\sffamily\bfseries\footnotesize, text=itaNavy, align=center] at (2.2, 2.75) {(b) Assimétrico ($F_1 \neq F_2$)\\{\scriptsize Ex.: Leilão 5G (Mapas públicos)}};
    \draw[->, thick, itaGray] (0,0) -- (4.3,0) node[right, font=\scriptsize] {$v_i$};
    \draw[->, thick, itaGray] (0,0) -- (0,2.0) node[left, font=\scriptsize] {$f_i(v_i)$};
    % Pequena [100, 400]
    \fill[itaLightAmber] (0.3,0) rectangle (1.65, 1.55);
    \draw[itaAmber, ultra thick] (0.3,0) -- (0.3,1.55) -- (1.65,1.55) -- (1.65,0);
    \node[text=itaAmber, font=\tiny\bfseries, align=center] at (0.97, 0.78) {Pequena\\$[100,400]$};
    % Vivo [500, 1000]
    \fill[itaLightGreen] (2.05,0) rectangle (3.95, 1.05);
    \draw[itaGreen, ultra thick] (2.05,0) -- (2.05,1.05) -- (3.95,1.05) -- (3.95,0);
    \node[text=itaGreen, font=\tiny\bfseries, align=center] at (3.0, 0.52) {Vivo (Gigante)\\$[500,1000]$};
    \node[below, font=\tiny] at (2.1, -0.02) {(R\$ milhões)};
  \end{scope}

  % Painel (c): Correlacionado
  \begin{scope}[shift={(10.8,0)}]
    \node[font=\sffamily\bfseries\footnotesize, text=itaNavy, align=center] at (2.15, 2.75) {(c) Tipos Correlacionados\\{\scriptsize Ex.: Pôquer ($F(\theta_{-i}\mid\theta_i)$ muda!)}};
    \draw[->, thick, itaGray] (0,0) -- (4.3,0);
    \draw[->, thick, itaGray] (0,0) -- (0,2.0) node[left, font=\scriptsize] {$P(\text{Ás})$};
    % Barras
    \fill[itaGray!30, draw=itaGray, thick] (0.35,0) rectangle (1.2, 1.40);
    \node[above, font=\scriptsize\bfseries] at (0.77, 1.40) {$4/52$};
    \node[below, font=\tiny, align=center] at (0.77, 0) {Prior\\Inicial};

    \fill[itaLightRed, draw=itaRed, thick] (1.75,0) rectangle (2.6, 0.72);
    \node[above, font=\scriptsize\bfseries, text=itaRed] at (2.17, 0.72) {$2/50$};
    \node[below, font=\tiny, align=center] at (2.17, 0) {Jog.\ 1\\(Viu 2 Ases)};

    \fill[itaLightBlue, draw=itaBlue, thick] (3.15,0) rectangle (4.0, 1.48);
    \node[above, font=\scriptsize\bfseries, text=itaBlue] at (3.57, 1.48) {$4/50$};
    \node[below, font=\tiny, align=center] at (3.57, 0) {Jog.\ 2\\(Viu 2 e 7)};
  \end{scope}
\end{tikzpicture}
""",

    "bid_shading_tradeoff": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=1.02]
  \draw[->, thick, itaGray] (0,0) -- (5.1,0) node[right, font=\scriptsize] {Lance $b_1$};
  \draw[->, thick, itaGray] (0,0) -- (0,3.35) node[above right, font=\scriptsize] {Payoff Esperado $\Pi_1(b_1)$};

  % Parabola Pi_1(b_1) = (v1 - b1)*2*b1 para v1 = 0.8 (escalada: x in [0, 4.4], max em x=2.2, y=2.45)
  \fill[itaLightBlue!60] plot[domain=0:4.4, samples=60] (\x, {2.45 * (1 - ((\x - 2.2)/2.2)^2)}) -- (4.4,0) -- (0,0) -- cycle;
  \draw[itaBlue, ultra thick] plot[domain=0:4.4, samples=60] (\x, {2.45 * (1 - ((\x - 2.2)/2.2)^2)});

  % Ponto ótimo em b* = v1/2
  \draw[dashed, itaRed, thick] (2.2, 0) node[below, font=\scriptsize\bfseries, text=itaRed] {$b_1^\ast(v_1) = \dfrac{v_1}{2}$} -- (2.2, 2.45);
  \fill[itaRed] (2.2, 2.45) circle (2.8pt);
  \node[above, fill=itaLightRed, draw=itaRed, text=itaRed, rounded corners=2pt, font=\scriptsize\bfseries, align=center, inner sep=2.5pt] at (2.2, 2.58) {Ótimo em ENB ($b_1^\ast = v_1/2$)\\[-1pt]{\tiny Equilibra Margem $\times$ Probabilidade}};

  % Ponto sincero b1 = v1
  \fill[itaGray] (4.4, 0) circle (2.8pt);
  \node[below, font=\scriptsize\bfseries] at (4.4, 0) {$b_1 = v_1$};
  \node[fill=white, draw=itaGray, text=black, rounded corners=2pt, font=\tiny, align=center, inner sep=2pt] (zero_lbl) at (4.05, 1.25) {Se $b_1 = v_1$: margem\\$(v_1 - v_1) = 0 \Rightarrow \Pi_1 = 0$!};
  \draw[->, thick, itaGray] (zero_lbl) -- (4.38, 0.12);

  % Seta de Bid Shading
  \draw[<->, ultra thick, itaGreen] (2.25, 0.45) -- (4.35, 0.45) node[midway, fill=itaLightGreen, draw=itaGreen, text=itaGreen, rounded corners=2pt, font=\tiny\bfseries, inner sep=1.8pt] {Bid Shading ($-50\%$)};
\end{tikzpicture}
""",

    "vickrey_dominancia_payoff": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=0.90]
  % Painel (a): Mentir para baixo (b1 = 70 vs b1 = 100)
  \begin{scope}[shift={(0,0)}]
    \node[font=\sffamily\bfseries\scriptsize, text=itaNavy] at (2.3, 3.25) {(a) Sublance ($b_1 = 70 < v_1 = 100$)};
    \draw[->, thick, itaGray] (0,0) -- (4.5,0) node[right, font=\tiny] {$M$};
    \draw[->, thick, itaGray] (0,-0.6) -- (0,2.75) node[left, font=\tiny] {$u_1$};

    % Zona de lucro perdido entre M=70 (x=2.1) e M=100 (x=3.0)
    \fill[itaLightAmber] (2.1,0) -- (2.1, 0.72) -- (3.0, 0) -- cycle;
    \draw[itaBlue, ultra thick] (0, 2.4) -- (3.0, 0) -- (4.2, 0);
    \draw[itaAmber, ultra thick, dashed] (0, 2.4) -- (2.1, 0.72) -- (2.1, 0) -- (4.2, 0);

    \node[below, font=\tiny] at (2.1, 0) {$70$};
    \node[below, font=\tiny\bfseries, text=itaBlue] at (3.0, 0) {$100$};
    \node[left, font=\tiny] at (0, 2.35) {$100$};

    \node[fill=itaLightAmber, draw=itaAmber, text=itaAmber, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2pt] (lbl1) at (3.05, 1.65) {Caso 2 ($M=85$):\\Perde R\$\,15 de lucro!};
    \draw[->, thick, itaAmber] (lbl1) -- (2.45, 0.32);
  \end{scope}

  % Painel (b): Mentir para cima (b1 = 120 vs b1 = 100)
  \begin{scope}[shift={(5.5,0)}]
    \node[font=\sffamily\bfseries\scriptsize, text=itaNavy] at (2.3, 3.25) {(b) Sobrelance ($b_1 = 120 > v_1 = 100$)};
    \draw[->, thick, itaGray] (0,0) -- (4.5,0) node[right, font=\tiny] {$M$};
    \draw[->, thick, itaGray] (0,-0.8) -- (0,2.75) node[left, font=\tiny] {$u_1$};

    % Zona de prejuizo entre M=100 (x=3.0) e M=120 (x=3.6)
    \fill[itaLightRed] (3.0,0) -- (3.6, -0.55) -- (3.6, 0) -- cycle;
    \draw[itaBlue, ultra thick] (0, 2.4) -- (3.0, 0) -- (4.2, 0);
    \draw[itaRed, ultra thick, dashed] (0, 2.4) -- (3.6, -0.55) -- (3.6, 0) -- (4.2, 0);

    \node[below, font=\tiny\bfseries, text=itaBlue] at (2.9, 0) {$100$};
    \node[above, font=\tiny\bfseries, text=itaRed] at (3.65, 0) {$120$};
    \node[left, font=\tiny] at (0, 2.35) {$100$};

    \node[fill=itaLightRed, draw=itaRed, text=itaRed, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2pt] (lbl2) at (2.95, 1.55) {Caso 3 ($M=110$):\\Vence pagando R\$\,110\\e tem prejuízo ($-$R\$\,10)!};
    \draw[->, thick, itaRed] (lbl2) -- (3.35, -0.25);
  \end{scope}
\end{tikzpicture}
""",

    "ipv_vs_cv_maldicao": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=0.98]
  \draw[->, thick, itaGray] (0,0) -- (8.6,0) node[right, font=\scriptsize] {R\$};
  \draw[->, thick, itaGray] (0,0) -- (0,3.2) node[above right, font=\scriptsize] {Densidade dos Sinais $s_i = V + \varepsilon_i$};

  % Metade esquerda (conservadores s_i < V) e metade direita (otimistas s_i > V)
  \fill[itaLightBlue!80] plot[domain=0.6:4.2, samples=50] (\x, {2.5*exp(-0.5*((\x-4.2)/1.25)^2)}) -- (4.2,0) -- (0.6,0) -- cycle;
  \fill[itaLightRed!85] plot[domain=4.2:7.8, samples=50] (\x, {2.5*exp(-0.5*((\x-4.2)/1.25)^2)}) -- (7.8,0) -- (4.2,0) -- cycle;
  \draw[itaNavy, ultra thick] plot[domain=0.6:7.8, samples=80] (\x, {2.5*exp(-0.5*((\x-4.2)/1.25)^2)});

  % Valor verdadeiro V = 100 (x = 4.2)
  \draw[itaGreen, ultra thick] (4.2, 0) node[below, font=\scriptsize\bfseries, text=itaGreen] {$V = 100$} -- (4.2, 2.7) node[above, font=\scriptsize\bfseries, text=itaGreen] {Valor Comum Real ($V = \text{R\$\,100}$)};

  % Maior chute max s_i = 150 (x = 7.2)
  \draw[itaRed, thick, dashed] (7.2, 0) node[below, font=\scriptsize\bfseries, text=itaRed] {$\max s_i = 150$} -- (7.2, 1.75);
  \fill[itaRed] (7.2, 0.18) circle (2.5pt);

  % Lance ingenuo vencedor b = 130 (x = 5.75)
  \draw[itaRed, very thick, dotted] (5.75, 0) node[below, font=\scriptsize\bfseries, text=itaRed] {$p = 130$} -- (5.75, 1.5);
  \node[fill=itaLightRed, draw=itaRed, text=itaRed, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2.5pt] (curse) at (6.7, 2.25) {Maldição do Vencedor:\\Ganha o mais otimista ($150$),\\paga R\$\,130 e perde R\$\,30!};
  \draw[->, thick, itaRed] (curse) -- (5.8, 1.15);

  % Lance Bayesiano Racional (x = 2.95)
  \draw[itaBlue, very thick, dashdotted] (2.95, 0) node[below, font=\scriptsize\bfseries, text=itaBlue] {$b_{\text{ENB}}^\ast$} -- (2.95, 1.75);
  \node[fill=itaLightBlue, draw=itaBlue, text=itaBlue, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2.5pt] (rational) at (1.7, 2.25) {Lance Bayesiano Racional:\\Condiciona em vencer\\($\max_{j\neq i} s_j < s_i$)};
  \draw[->, thick, itaBlue] (rational) -- (2.9, 1.35);
\end{tikzpicture}
""",

    "modelo_resolvido_fatias": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=1.0]
  \node[font=\sffamily\bfseries\footnotesize, text=itaNavy] at (3.6, 3.35) {Divisão Média de $[0,1]$ por $n=2$ Sorteios Uniformes};

  % Barra 1: Segmento [0,1] em 3 terços
  \draw[itaNavy, line width=2.5pt] (0.4, 2.45) -- (6.8, 2.45);
  \foreach \x/\lbl in {0.4/$0$, 2.53/$\mathbb{E}[\min]=\frac{1}{3}$, 4.67/$\mathbb{E}[\max]=\frac{2}{3}$, 6.8/$1$} {
    \draw[itaNavy, line width=1.8pt] (\x, 2.3) -- (\x, 2.6);
    \node[above, font=\scriptsize\bfseries, text=itaNavy] at (\x, 2.6) {\lbl};
  }
  \draw[decorate, decoration={brace, mirror, amplitude=4pt}, itaGray, thick] (0.4, 2.22) -- (2.51, 2.22) node[midway, below=3pt, font=\tiny] {$1/3$};
  \draw[decorate, decoration={brace, mirror, amplitude=4pt}, itaGray, thick] (2.55, 2.22) -- (4.65, 2.22) node[midway, below=3pt, font=\tiny] {$1/3$};
  \draw[decorate, decoration={brace, mirror, amplitude=4pt}, itaGray, thick] (4.69, 2.22) -- (6.8, 2.22) node[midway, below=3pt, font=\tiny] {$1/3$};

  % Barra 2: 2º Preço (Vickrey)
  \node[left, font=\scriptsize\bfseries, text=itaBlue] at (0.3, 1.35) {2º Preço:};
  \fill[itaBlue!85, draw=itaNavy, thick] (0.4, 1.12) rectangle (2.53, 1.58);
  \fill[itaGray!15, draw=itaGray, dashed] (2.53, 1.12) rectangle (6.8, 1.58);
  \node[text=white, font=\scriptsize\bfseries] at (1.46, 1.35) {Receita $= 1/3$};
  \node[text=itaNavy, font=\tiny\bfseries] at (4.70, 1.35) {$100\%$ do 2º colocado ($\mathbb{E}[\min] = 1/3$)};

  % Barra 3: 1º Preço
  \node[left, font=\scriptsize\bfseries, text=itaRed] at (0.3, 0.45) {1º Preço:};
  \fill[itaRed!85, draw=itaRed!90!black, thick] (0.4, 0.22) rectangle (2.53, 0.68);
  \fill[itaLightRed, draw=itaRed, dashed] (2.53, 0.22) rectangle (4.67, 0.68);
  \fill[itaGray!15, draw=itaGray, dashed] (4.67, 0.22) rectangle (6.8, 0.68);
  \node[text=white, font=\scriptsize\bfseries] at (1.46, 0.45) {Receita $= 1/3$};
  \node[text=itaRed, font=\tiny\bfseries] at (3.60, 0.45) {Shading ($-50\%$)};
  \node[text=itaNavy, font=\tiny\bfseries] at (5.75, 0.45) {$\frac{1}{2} \times \frac{2}{3} = \frac{1}{3}$};
\end{tikzpicture}
""",

    "caso_real_dente_serra": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=0.96]
  \node[font=\sffamily\bfseries\footnotesize, text=itaNavy] at (3.4, 3.55) {1997--2001 (Dente de Serra) vs.\ 2002 (2º Preço Google)};
  \draw[->, thick, itaGray] (0,0) -- (6.6,0) node[right, font=\scriptsize] {Tempo ($t$)};
  \draw[->, thick, itaGray] (0,0) -- (0,3.05) node[left, font=\scriptsize] {R\$};

  % Valor da Nike R$ 10 (y = 2.75)
  \draw[itaGreen, thick, dotted] (0, 2.75) -- (6.3, 2.75) node[right, font=\tiny\bfseries, text=itaGreen] {$v_{\text{Nike}} = 10$};
  \node[left, font=\tiny, text=itaGreen] at (0, 2.75) {$10{,}00$};

  % Limite da Adidas R$ 5,01 (y = 1.50)
  \draw[itaBlue, ultra thick, dashed] (0, 1.50) -- (6.3, 1.50);
  \node[left, font=\tiny\bfseries, text=itaBlue] at (0, 1.50) {$5{,}01$};
  \node[left, font=\tiny] at (0, 0.35) {$1{,}00$};

  % Ciclos Dente de Serra em vermelho
  \draw[itaRed, very thick]
    (0.1, 0.35) -- (1.9, 1.50) -- (1.95, 0.35)
    -- (3.8, 1.50) -- (3.85, 0.35)
    -- (5.7, 1.50) -- (5.75, 0.35);

  \node[fill=itaLightRed, draw=itaRed, text=itaRed, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2pt] (saw) at (1.6, 2.22) {Overture (1º Preço Visível):\\Adidas cai p/ R\$\,1,00 e reinicia!};
  \draw[->, thick, itaRed] (saw) -- (1.9, 1.56);

  \node[fill=itaLightBlue, draw=itaBlue, text=itaBlue, rounded corners=2pt, font=\tiny\bfseries, align=center, inner sep=2pt] (gsp) at (5.15, 2.22) {Google 2002 (2º Preço):\\Estável em R\$\,5,01!};
  \draw[->, thick, itaBlue] (gsp) -- (5.15, 1.56);
\end{tikzpicture}
""",

    "caso_real_header_bidding": r"""
\begin{tikzpicture}[font=\sffamily\footnotesize, scale=0.92]
  \node[font=\sffamily\bfseries\footnotesize, text=itaNavy] at (3.6, 3.65) {Torneio de 2 Etapas (\textit{Header Bidding} --- 2019)};

  % Semifinal A
  \node[draw=itaBlue, fill=itaLightBlue, text=black, rounded corners=3pt, minimum width=3.1cm, minimum height=1.15cm, align=center, font=\tiny] (semiA) at (1.6, 2.35) {\textbf{Semifinal Corretora A}\\Nike: \textbf{R\$\,10,00} vs.\ Adidas: \textbf{R\$\,2,00}\\{\color{itaRed}\textbf{No 2º Preço: cai p/ R\$\,2,00!}}};

  % Semifinal B
  \node[draw=itaAmber, fill=itaLightAmber, text=black, rounded corners=3pt, minimum width=3.1cm, minimum height=1.15cm, align=center, font=\tiny] (semiB) at (5.6, 2.35) {\textbf{Semifinal Corretora B}\\Puma: \textbf{R\$\,6,00}\\{\color{itaAmber}\textbf{No 1º Preço: envia R\$\,6,00}}};

  % Grande Final (Desastre no 2º Preço)
  \node[draw=itaRed, fill=itaLightRed, text=itaRed, rounded corners=3pt, minimum width=6.6cm, minimum height=0.82cm, align=center, font=\tiny\bfseries] (final1) at (3.6, 0.95) {Grande Final (Site de Notícias): R\$\,2,00 (A) vs.\ R\$\,6,00 (B)\\$\Rightarrow$ Puma (R\$\,6) derrota a Nike (que pagaria R\$\,10)! Ineficiente!};

  % Solução 2019 (1º Preço + Bid Shading)
  \node[draw=itaGreen, fill=itaLightGreen, text=itaGreen, rounded corners=3pt, minimum width=6.6cm, minimum height=0.78cm, align=center, font=\tiny\bfseries] (final2) at (3.6, -0.05) {Solução (2019 --- Migração p/ 1º Preço + Shading):\\Nike oferta R\$\,7,00 $\to$ vai R\$\,7,00 inteiro p/ a Final e vence a Puma (R\$\,6)!};

  \draw[-{Stealth[length=2mm]}, thick, itaBlue] (semiA.south) -- (1.6, 1.36);
  \draw[-{Stealth[length=2mm]}, thick, itaAmber] (semiB.south) -- (5.6, 1.36);
\end{tikzpicture}
""",
}


def main():
    for name, body in FIGURES.items():
        tex_path = os.path.join(IMG_DIR, f"{name}.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(PREAMBLE + body + POSTAMBLE)
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"],
            cwd=IMG_DIR,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for ext in (".aux", ".log", ".tex"):
            p = os.path.join(IMG_DIR, f"{name}{ext}")
            if os.path.exists(p):
                os.remove(p)
        print(f"Gerada figura vetorial: {name}.pdf")


if __name__ == "__main__":
    main()
