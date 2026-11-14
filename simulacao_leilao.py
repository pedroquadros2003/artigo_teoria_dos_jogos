#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulador de Leilão de Anúncios Online (1º Preço vs. 2º Preço / Vickrey)
GED-62 — Teoria dos Jogos (ITA) — Grupo 5

Simula N_LEILOES = 10.000 leilões com n anunciantes simétricos cujas valorações
privadas v_i ~ U[0, 1] são independentes e identicamente distribuídas (IPV),
comparando:
  1. As retas de lance ótimo em equilíbrio:
     - 2º Preço (Vickrey): b(v) = v (Revelação Sincera)
     - 1º Preço:           b(v) = ((n - 1) / n) * v (Com Bid Shading)
  2. A convergência da receita média acumulada da plataforma nos dois formatos
     para o valor teórico exato E[R] = (n - 1) / (n + 1), demonstrando
     visualmente o Teorema da Equivalência de Receita (RET).
"""

import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def executar_simulacao(n_jogadores: int = 2, n_leiloes: int = 10_000, semente: int = 42):
    t0 = time.perf_counter()
    rng = np.random.default_rng(semente)

    # Sorteio das valorações privadas v_i ~ U[0, 1] para todos os leilões
    # Matriz de dimensão (n_leiloes, n_jogadores)
    valoracoes = rng.uniform(0.0, 1.0, size=(n_leiloes, n_jogadores))

    # Estratégias de equilíbrio de Nash Bayesiano:
    # - 2º Preço (Vickrey): lance sincero b^(2)(v) = v
    lances_2p = valoracoes

    # - 1º Preço: lance com bid shading b^(1)(v) = ((n - 1) / n) * v
    fator_shading = (n_jogadores - 1.0) / n_jogadores
    lances_1p = fator_shading * valoracoes

    # Receita do leiloeiro (plataforma de anúncios) em cada leilão:
    # - No 1º Preço, o vencedor paga o seu próprio lance (o maior lance submetido)
    receita_1p = np.max(lances_1p, axis=1)

    # - No 2º Preço (Vickrey), o vencedor paga o 2º maior lance submetido
    lances_2p_ordenados = np.sort(lances_2p, axis=1)
    receita_2p = lances_2p_ordenados[:, -2]

    # Receita média acumulada ao longo dos 10.000 leilões
    indices = np.arange(1, n_leiloes + 1)
    media_acum_1p = np.cumsum(receita_1p) / indices
    media_acum_2p = np.cumsum(receita_2p) / indices

    # Valor teórico exato pelo Teorema da Equivalência de Receita: E[R] = (n - 1) / (n + 1)
    receita_teorica = (n_jogadores - 1.0) / (n_jogadores + 1.0)

    dt = time.perf_counter() - t0
    print(f"Simulação concluída em {dt:.4f} segundos ({n_leiloes} leilões, n = {n_jogadores} anunciantes).")
    print(f"  Receita Teórica Esperada E[R] = (n-1)/(n+1) : {receita_teorica:.4f}")
    print(f"  Receita Média Simulada (1º Preço)           : {media_acum_1p[-1]:.4f}")
    print(f"  Receita Média Simulada (2º Preço / Vickrey) : {media_acum_2p[-1]:.4f}")

    # Configuração visual para publicação (ABNT / Relatório)
    plt.rcParams.update({
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 9.5,
        "figure.titlesize": 13,
    })

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), dpi=300)

    # -------------------------------------------------------------------------
    # Painel (a): Retas de Lance de Equilíbrio b(v)
    # -------------------------------------------------------------------------
    v_grid = np.linspace(0.0, 1.0, 200)
    b_grid_2p = v_grid
    b_grid_1p = fator_shading * v_grid

    ax1.plot(
        v_grid,
        b_grid_2p,
        color="#1f77b4",
        linewidth=2.5,
        label=r"2º Preço (Vickrey): $b(v) = v$ (Lance Sincero)",
    )
    ax1.plot(
        v_grid,
        b_grid_1p,
        color="#d62728",
        linewidth=2.5,
        linestyle="--",
        label=rf"1º Preço: $b(v) = \frac{{n-1}}{{n}}v = \frac{{{n_jogadores-1}}}{{{n_jogadores}}}v$ (Com Bid Shading)",
    )
    ax1.fill_between(
        v_grid,
        b_grid_1p,
        b_grid_2p,
        color="#ff9896",
        alpha=0.25,
        label=r"Desconto Estratégico ($\it{Bid\ Shading}$)",
    )

    # Seta ilustrativa do Bid Shading em v = 0.80
    v_ref = 0.80
    ax1.annotate(
        "",
        xy=(v_ref, fator_shading * v_ref),
        xytext=(v_ref, v_ref),
        arrowprops=dict(arrowstyle="->", color="#b22222", lw=1.8),
    )
    ax1.text(
        v_ref + 0.02,
        0.5 * (v_ref + fator_shading * v_ref) - 0.02,
        "Bid Shading\n" + rf"($-{int((1 - fator_shading)*100)}\%$)",
        color="#8b0000",
        fontsize=9.5,
        fontweight="bold",
    )

    ax1.set_title("(a) Funções de Lance no Equilíbrio de Nash Bayesiano", fontweight="bold", pad=10)
    ax1.set_xlabel(r"Valoração Privada do Anunciante ($v_i \sim U[0,1]$)")
    ax1.set_ylabel(r"Lance Submetido ($b_i$)")
    ax1.set_xlim(0.0, 1.0)
    ax1.set_ylim(0.0, 1.05)
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left", frameon=True, facecolor="white", framealpha=0.9)

    # -------------------------------------------------------------------------
    # Painel (b): Convergência da Receita Média Acumulada (10.000 Leilões)
    # -------------------------------------------------------------------------
    ax2.plot(
        indices,
        media_acum_2p,
        color="#1f77b4",
        linewidth=1.8,
        alpha=0.9,
        label=f"Receita Média Acumulada — 2º Preço (final: {media_acum_2p[-1]:.4f})",
    )
    ax2.plot(
        indices,
        media_acum_1p,
        color="#d62728",
        linewidth=1.8,
        alpha=0.9,
        label=f"Receita Média Acumulada — 1º Preço (final: {media_acum_1p[-1]:.4f})",
    )
    ax2.axhline(
        receita_teorica,
        color="#2ca02c",
        linestyle="--",
        linewidth=2.2,
        label=rf"Valor Teórico Exato: $\mathbb{{E}}[R] = \frac{{n-1}}{{n+1}} = \frac{{{n_jogadores-1}}}{{{n_jogadores+1}}} \approx {receita_teorica:.4f}$",
    )

    ax2.set_title(
        f"(b) Equivalência de Receita em {n_leiloes:,} Leilões Simulados ($n={n_jogadores}$)".replace(",", "."),
        fontweight="bold",
        pad=10,
    )
    ax2.set_xlabel("Número de Leilões Simulados (Escala Linear)")
    ax2.set_ylabel("Receita Média Acumulada da Plataforma")
    ax2.set_xlim(1, n_leiloes)
    ax2.set_ylim(receita_teorica - 0.12, receita_teorica + 0.12)
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right", frameon=True, facecolor="white", framealpha=0.9)

    fig.suptitle(
        "Simulação de Monte Carlo: Leilão de 1º Preço vs. 2º Preço (Vickrey) e Teorema da Equivalência de Receita",
        fontweight="bold",
        y=0.99,
    )
    fig.tight_layout()

    caminho_img = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Artigo",
        "Imagens",
        "equivalencia_receita_simulacao.png",
    )
    os.makedirs(os.path.dirname(caminho_img), exist_ok=True)
    fig.savefig(caminho_img, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfico salvo com sucesso em: {caminho_img}")


if __name__ == "__main__":
    executar_simulacao(n_jogadores=2, n_leiloes=10_000, semente=42)
