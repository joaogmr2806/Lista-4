# listaexercicio4.py
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ip

# 1) Configure título, header e descrição (texto igual ao original)
st.set_page_config(page_title="Lista de Exercícios 4")
st.title("Projeto Final – Análise Contábil com Ajuste Econômico")
st.write("Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.")

# 2) Importe os dados do arquivo empresas_dados.csv e apresente todas as linhas da df (peso: 1,0)
df = pd.read_csv("empresas_dados.csv", sep=";")
st.subheader("2) Dados do arquivo empresas_dados.csv")
st.dataframe(df.head(len(df)))

# 3) Calcule os indicadores Margem Líquida e ROA e salve como novas colunas da df. Depois apresente os dois indicadores no mesmo gráfico de linhas, agrupado por Ano (peso: 1,0)
st.subheader("3) Indicadores Margem Líquida e ROA por Ano")
df['Margem Líquida (%)'] = (df['Lucro Líquido'] / df['Receita Líquida']) * 100
df['ROA (%)'] = (df['Lucro Líquido'] / df['Ativo Total']) * 100
df_ano = df.groupby('Ano')[['Margem Líquida (%)', 'ROA (%)']].mean().reset_index()

fig1, ax1 = plt.subplots()
ax1.plot(df_ano['Ano'], df_ano['Margem Líquida (%)'], marker='o', label='Margem Líquida (%)')
ax1.plot(df_ano['Ano'], df_ano['ROA (%)'], marker='o', label='ROA (%)')
ax1.set_title('Indicadores Margem Líquida e ROA por Ano')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Percentual (%)')
ax1.legend()
st.pyplot(fig1)

# 4) Utilize o pacote ipeadatapy e faça busca para encontrar o indicador que traga o IPCA, taxa de variação, em % e anual (peso: 2,0)
st.subheader("4) Dados IPCA (2010 a 2024) via ipeadatapy")
df_ipca = ip.timeseries("PRECOS_IPCAG")
df_ipca = df_ipca.loc["2010":"2024"]
df_ipca = df_ipca.rename(columns={"YEAR": "Ano", "VALUE ((% a.a.))": "IPCA"})
st.dataframe(df_ipca)

# 5) Combine as duas df (Excel e IPEA) em uma nova df e calcule nova coluna chamada Receita Real (peso: 2,0)
st.subheader("5) Combinação das df e cálculo da Receita Real")
df_combinado = pd.merge(df, df_ipca, on='Ano')
df_combinado["Receita Real"] = df_combinado["Receita Líquida"] - (df_combinado["Receita Líquida"] * (df_combinado["IPCA"] / 100))
st.dataframe(df_combinado)

# 6) Crie gráfico de linha que apresente as variáveis Receita Líquida e Receita Real ao longo dos anos (peso: 1,0)
st.subheader("6) Gráfico Receita Líquida e Receita Real ao longo dos anos")
df_receita_liquida = df_combinado.groupby("Ano")["Receita Líquida"].mean()
df_receita_real = df_combinado.groupby("Ano")["Receita Real"].mean()

fig2, ax2 = plt.subplots()
ax2.plot(df_receita_liquida.index, df_receita_liquida.values, label="Receita Líquida", marker='o')
ax2.plot(df_receita_real.index, df_receita_real.values, label="Receita Real", marker='o')
ax2.set_xlabel("Ano")
ax2.set_ylabel("Valor (médio)")
ax2.set_title("Receita Líquida e Receita Real ao longo dos anos")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# 7) Faça os ajustes necessários e leve este projeto para a web usando GitHub e Streamlit (peso: 2,0)
st.write("""
7) Faça os ajustes necessários e leve este projeto para a web usando GitHub e Streamlit (peso: 2,0)

- Caça os ajustes necessários no projeto para ser publicado no Streamlit  
- Crie novo repositório público no GitHub e leve os arquivos .py e .csv pra lá. Aproveite e crie o arquivo requirements.txt com os pacotes utilizados no projeto  
- Crie novo projeto no Streamlit e associe ao repositório da lista
""")
