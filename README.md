# LIBNM · Ferreira Lab — site institucional

Site estático (HTML/CSS/JS puro, sem build) do LIBNM (Laboratório Integrativo de
Bioprospecção de Novas Moléculas), Instituto de Química — USP.

## Editar o site

Edite `index.html` diretamente. A seção Equipe é uma lista de grupos
(`stu-group`), um por nível (Coordenação, Pós-Doutorado, Doutorado, Mestrado,
Iniciação Científica), cada um com cards (`stu-card`) no mesmo padrão: foto
quadrada em `team/`, nome, descrição do projeto e badges de FAPESP/ORCID. Para
adicionar alguém, copie um `stu-card` existente e ajuste foto, nome, texto e
links.

## Rodar localmente

Abra `index.html` direto no navegador, ou sirva a pasta:

```
python3 -m http.server 8000
```

## Deploy

O deploy é automático via Netlify a cada push na branch `main` (conectar este
repositório em app.netlify.com → "Add new site" → "Import an existing
project"). Domínio planejado: `ferreiralab.com.br`.
