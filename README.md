```markdown
# Projeto de Organização de Favoritos HTML

Este projeto contém dois scripts Python para processar arquivos HTML de favoritos (bookmarks), extraindo, organizando e limpando URLs duplicadas.

## Arquivos

### 1. `alpha.py`
Extrai URLs de um arquivo HTML de favoritos e gera um novo arquivo com as URLs organizadas em ordem alfabética.

**Funcionalidades:**
- Extrai todas as URLs encontradas dentro de tags `<a>` do HTML
- Ordena as URLs em ordem alfabética
- Gera um novo arquivo HTML com as URLs formatadas em lista

**Uso:**
```bash
python alpha.py
```

**Observação:** O script espera um arquivo de entrada chamado `bookmark.html` e gera um arquivo de saída chamado `output.html`.

### 2. `remove_duplicate_lines.py`
Remove linhas duplicadas de um arquivo de texto, útil para limpar favoritos com URLs repetidas.

**Funcionalidades:**
- Lê um arquivo e remove linhas idênticas
- Mantém a primeira ocorrência de cada linha única
- Sobrescreve o arquivo original com o conteúdo limpo

**Uso:**
```bash
python remove_duplicate_lines.py bookmarks.html
```

## Fluxo de Trabalho Sugerido

1. **Extraia seus favoritos** do navegador como um arquivo HTML (normalmente chamado `bookmarks.html`)
2. **Remova duplicatas** com:
   ```bash
   python remove_duplicate_lines.py bookmarks.html
   ```
3. **Organize em ordem alfabética** com:
   ```bash
   python alpha.py
   ```
   (Certifique-se de renomear seu arquivo para `bookmark.html` ou modificar o script)

## Requisitos

- Python 3.x
- BeautifulSoup4 (instale com `pip install beautifulsoup4`)

## Instalação das Dependências

```bash
pip install beautifulsoup4
```

## Exemplo de Uso

```bash
# 1. Copie seus favoritos para a pasta do projeto
cp ~/Downloads/bookmarks.html bookmark.html

# 2. Execute o script de organização
python alpha.py

# 3. O resultado estará em output.html
```

## Estrutura dos Arquivos de Saída

O `alpha.py` gera um arquivo HTML estruturado com:
- Cabeçalho HTML básico
- Lista de URLs em formato `<DT><A HREF='URL'>URL</A>`
- Todas as URLs em ordem alfabética

## Notas

- Ambos os scripts modificam/geram arquivos localmente
- Recomenda-se fazer backup dos favoritos originais antes de processá-los
- O `remove_duplicate_lines.py` pode ser usado em qualquer arquivo de texto, não apenas em HTML
---
