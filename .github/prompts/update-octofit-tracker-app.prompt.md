mode: 'agent'
model: GPT-4.1

# Atualizações do App Django

- Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.

1. Atualize o `settings.py` para conexão com MongoDB e CORS.
2. Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar coleções de usuários, equipes, atividades, classificação e treinos.
3. Garanta que `/` aponte para a API e que `api_root` esteja presente em `urls.py`.
