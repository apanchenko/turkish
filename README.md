<!-- markdownlint-disable MD022 MD032 MD036 MD041 -->
# turkish

1. Frontend Development:
Now, you can start building the frontend using React. I won't go into too much detail here since it could be an extensive topic on its own. Create the components you need, handle routing using React Router, and use Axios (or fetch) to make API requests to the backend.

2. Markdown Parsing:
In the backend, create a function to parse the Markdown document and store it in the PostgreSQL database using SQLAlchemy. You can use the markdown library for parsing, as previously mentioned.

3. Run the Application:
To run the backend, use Uvicorn:

```bash
uvicorn backend.main:app --reload
```

For the frontend, you can use the development server:

```bash
cd frontend
npm start
```

## Bağlantılar
- [sözlük](https://tureng.com/tr/turkce-ingilizce)
- [stemmer](https://github.com/otuncelli/turkish-stemmer-python)
- [morfoloji](https://github.com/google-research/turkish-morphology)
