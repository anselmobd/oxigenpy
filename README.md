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

## Status

O oxigenpy encontra-se em desenvolvimento ativo.
Até a versão 1.0.0, a API pública deve ser considerada instável.

Versões alfa e beta são publicadas para teste e feedback.
