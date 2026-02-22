# Burn Severity Mapping

## Descrição do Projeto

Este projeto concentra-se na **avaliação pós-incêndio** através do mapeamento da severidade da queima. Utiliza o cálculo do Índice de Queimada Normalizado (NBR) e a detecção de mudanças com imagens do satélite Landsat para quantificar o impacto de incêndios florestais na vegetação e no solo. O objetivo é fornecer informações detalhadas sobre a extensão e a intensidade dos danos causados pelo fogo, auxiliando na recuperação e gestão de áreas afetadas.

## Objetivos

- Calcular o Índice de Queimada Normalizado (NBR) para imagens pré e pós-incêndio.
- Realizar a detecção de mudanças para determinar a severidade da queima (dNBR).
- Gerar mapas de severidade da queima para avaliação do impacto do incêndio.

## Metodologia

1. **Aquisição de Imagens**: Obtenção de imagens Landsat (ou Sentinel-2) de antes e depois do evento de incêndio.
2. **Pré-processamento**: Correções radiométricas e atmosféricas das imagens.
3. **Cálculo do NBR**: Aplicação da fórmula do NBR (NIR - SWIR2) / (NIR + SWIR2) para ambas as imagens.
4. **Cálculo do dNBR**: Subtração do NBR pós-incêndio do NBR pré-incêndio para obter o índice de severidade da queima.
5. **Classificação da Severidade**: Categorização dos valores de dNBR em classes de severidade (ex: baixa, moderada, alta).

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Bibliotecas Python**: `rasterio` para manipulação de dados raster, `numpy` para computação numérica, `matplotlib` para visualização.
- **Google Earth Engine (GEE) API**: (Opcional) Para acesso e processamento de dados geoespaciais em larga escala.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/tassiaparadasampaio-cmyk/Burn-Severity-Mapping.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install rasterio numpy matplotlib
   ```
3. Prepare suas imagens de satélite pré e pós-incêndio (preferencialmente em formato .tif).
4. Execute o script principal (exemplo):
   ```bash
   python burn_severity_mapping.py
   ```

## Exemplo de Código (burn_severity_mapping.py)

```python
import rasterio
import numpy as np
import matplotlib.pyplot as plt

print("Script de exemplo para mapeamento da severidade da queima.")

# Este é um placeholder. O código real exigiria imagens de satélite pré e pós-incêndio.
# Para fins de demonstração, vamos simular dados de NBR.

# Simular NBR pré-incêndio (valores entre -1 e 1)
nbr_pre = np.random.rand(100, 100) * 2 - 1

# Simular NBR pós-incêndio (valores geralmente mais baixos em áreas queimadas)
nbr_post = nbr_pre - (np.random.rand(100, 100) * 0.5 + 0.5) # Redução significativa
nbr_post = np.clip(nbr_post, -1, 1) # Garantir que os valores permaneçam entre -1 e 1

# Simular uma área queimada para demonstração
center_row, center_col = 50, 50
radius = 20
for i in range(100):
    for j in range(100):
        if (i - center_row)**2 + (j - center_col)**2 < radius**2:
            nbr_post[i, j] = nbr_pre[i, j] - (np.random.rand() * 0.8 + 0.2) # Maior redução na área queimada

nbr_post = np.clip(nbr_post, -1, 1)

# Calcular dNBR
dnbr = nbr_pre - nbr_post

# Visualização do dNBR
plt.figure(figsize=(8, 8))
plt.imshow(dnbr, cmap=\'RdYlGn_r\', vmin=-1, vmax=1) # Cores para severidade da queima
plt.colorbar(label=\'dNBR\')
plt.title(\'Mapeamento de Severidade da Queima (dNBR Simulado)\')
plt.xlabel(\'Coluna de Pixel\')
plt.ylabel(\'Linha de Pixel\')
plt.show()

print("\nPara uma aplicação real, você precisaria de:")
print("- Arquivos .tif de imagens de satélite pré e pós-incêndio (bandas NIR e SWIR2).")
print("- Funções para ler as bandas e calcular o NBR a partir delas.")
print("- Limiares para classificar o dNBR em categorias de severidade.")
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
