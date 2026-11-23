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

## Publicações (sincronizadas com o ORCID)

A lista da aba Publicações é gerada de `pub.orcid.org` (ORCID 0000-0002-1952-9428)
por `scripts/update_pubs.py`, entre os marcadores `ORCID-PUBS:START/END` do
`index.html`. O workflow `.github/workflows/sync-orcid.yml` roda todo dia e
faz commit se houver paper novo (o Netlify publica em seguida). Para forçar:
aba Actions → "Sincronizar publicações (ORCID)" → Run workflow, ou
`python3 scripts/update_pubs.py` localmente. Não edite a lista à mão.

## SnorMol

O app QSAR é um único HTML autocontido em `snormol/index.html`, com guia em PDF
e dados de exemplo em `snormol/`.

## Rodar localmente

Abra `index.html` direto no navegador, ou sirva a pasta:

```
python3 -m http.server 8000
```

## Deploy

O deploy é automático via Netlify a cada push na branch `main` (conectar este
repositório em app.netlify.com → "Add new site" → "Import an existing
project"). Domínio planejado: `ferreiralab.com.br`.

## Jogo

"SnorMol X Hipercolesterolemia" é um HTML autocontido (Phaser embutido) em `jogo/index.html`. Aparece nas abas Software e Em destaque.
