from bs4 import BeautifulSoup

# Função para extrair URLs de um arquivo HTML
def extract_urls_from_html(html_content):
    urls = []
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for link in soup.find_all('a'):
        url = link.get('href')
        if url:
            urls.append(url)
    
    return urls

# Função para organizar URLs em ordem alfabética e criar um novo HTML
def organize_and_save(sorted_urls, output_file):
    with open(output_file, 'w') as f:
        f.write("<html>\n<head>\n<title>URLs Organizadas</title>\n</head>\n<body>\n")
        f.write("<ul>\n")
        
        for url in sorted_urls:
            f.write(f"<DT><A HREF='{url}'>{url}</A>\n")
        
        f.write(f"<DT><A HREF='{url}'>{url}</A>\n")

# Ler o conteúdo do arquivo HTML
input_file_path = 'bookmark.html'
output_file_path = 'output.html'

with open(input_file_path, 'r') as f:
    html_content = f.read()

# Extrair URLs do arquivo HTML
urls = extract_urls_from_html(html_content)

# Organizar as URLs em ordem alfabética
sorted_urls = sorted(urls)

# Salvar as URLs organizadas em um novo arquivo HTML
organize_and_save(sorted_urls, output_file_path)

print(f"URLs organizadas foram salvas em '{output_file_path}'.")
