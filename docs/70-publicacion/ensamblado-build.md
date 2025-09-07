# Ensamblado y Build

## Proceso de Construcción

El proceso de build transforma los Data Modules en Markdown a un sitio web estático interactivo.

### 1. Pre-build Validación

```bash
# Validar metadatos S1000D
python tools/validate_dm_metadata.py

# Verificar links internos
python tools/check_internal_links.py

# Validar DMRL consistency
python tools/validate_dmrl.py
```

### 2. Build MkDocs

```bash
# Build local para desarrollo
mkdocs serve

# Build de producción
mkdocs build

# Build estricto (falla si hay warnings)
mkdocs build --strict
```

### 3. Post-build Optimización

```bash
# Optimizar assets
python tools/optimize_assets.py

# Generar sitemap
python tools/generate_sitemap.py

# Comprimir archivos
python tools/compress_output.py
```

## Configuración de Build

### mkdocs.yml

```yaml
site_name: Teknia Tokens - S1000D Documentation
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight

plugins:
  - search
  - mermaid2

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - tables
  - toc
```

### Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `SITE_URL` | URL base del sitio | `https://localhost:8000` |
| `BUILD_ENV` | Entorno de build | `development` |
| `ENABLE_ANALYTICS` | Habilitar analytics | `false` |

## Pipeline CI/CD

### GitHub Actions

```yaml
name: Build and Deploy IETP
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Validate Data Modules
        run: python tools/validate_dm_metadata.py
        
      - name: Build site
        run: mkdocs build --strict
        
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

## Optimizaciones de Performance

### Assets
- Compresión automática de imágenes
- Minificación de CSS/JS
- Lazy loading para multimedia
- CDN para assets estáticos

### Contenido
- Índice de búsqueda optimizado
- Paginación para secciones grandes
- Caché de navegador configurado
- Preload de recursos críticos

## Monitoreo y Analytics

### Métricas de Uso
- Páginas más visitadas
- Términos de búsqueda frecuentes
- Tiempo de permanencia
- Dispositivos y navegadores

### Calidad del Contenido
- Enlaces rotos
- Páginas sin referencias
- Módulos obsoletos
- Cobertura DMRL

## Troubleshooting

### Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Build falla con warnings | Referencias rotas | Revisar enlaces internos |
| Mermaid no renderiza | Plugin no configurado | Verificar instalación |
| Búsqueda no funciona | Índice corrupto | Rebuild completo |
| Assets no cargan | Rutas incorrectas | Verificar paths relativos |

### Logs de Build

```bash
# Logs detallados
mkdocs build --verbose

# Debug de plugins
mkdocs build --config-file mkdocs-debug.yml
```