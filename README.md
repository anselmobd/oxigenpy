# oxigenpy

Utilitários Python mantidos pela **Oxigenai**.

O objetivo do `oxigenpy` é concentrar funções reutilizáveis de uso geral
(strings, datas, etc.), com uma API estável e organizada por domínio.

## Instalação

### Em desenvolvimento (local)

```bash
pip install -e .
```

### Via pip (futuro)

```bash
pip install oxigenpy
```

### Uso

```bash
import oxigenpy as oxy

oxy.strings.slugify("Olá Mundo")
oxy.strings.normalizar("  texto  ")
oxy.datas.hoje()
```
