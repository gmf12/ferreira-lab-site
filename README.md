# LIBNM · Ferreira Lab — site institucional

Site estático (HTML/CSS/JS puro, sem build) do LIBNM (Laboratório Integrativo de
Bioprospecção de Novas Moléculas), Instituto de Química — USP.

## Editar o site

Edite `index.html` diretamente. Para adicionar o ORCID de um(a) aluno(a) na
seção Equipe, procure o comentário `Para adicionar o ORCID` e troque o
`href="#"` do link com classe `stu-badge placeholder` pelo link completo do
ORCID (ex: `https://orcid.org/0000-0000-0000-0000`), removendo a classe
`placeholder`.

## Rodar localmente

Abra `index.html` direto no navegador, ou sirva a pasta:

```
python3 -m http.server 8000
```

## Deploy

O deploy é automático via Netlify a cada push na branch `main` (conectar este
repositório em app.netlify.com → "Add new site" → "Import an existing
project"). Domínio planejado: `ferreiralab.com.br`.
