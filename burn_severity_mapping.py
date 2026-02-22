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
