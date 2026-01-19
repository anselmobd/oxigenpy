# Política de Versionamento — oxigenpy

O oxigenpy segue o padrão **Semantic Versioning** com extensões de
**pre-release** conforme a PEP 440.

## Versões estáveis

- **PATCH** (`X.Y.Z`)  
  Correção de bugs sem alteração de API.

- **MINOR** (`X.Y+1.0`)  
  Novas funcionalidades compatíveis com a API existente.

- **MAJOR** (`X+1.0.0`)  
  Quebras de API pública.

## Versões pré-lançamento (pre-release)

Antes da versão `1.0.0`, o projeto utiliza versões **alfa**, **beta**
e **release candidate** para publicar progresso incremental sem assumir
estabilidade de API.

### Alpha (`a`)
Exemplo:

```
0.1.0a1
0.1.0a2
```

Usado para:
- adição de novos módulos
- evolução da estrutura interna
- expansão de testes
- mudanças frequentes de API

### Beta (`b`)
Exemplo:

```
0.1.0b1
0.1.0b2
```

Usado quando:
- os módulos principais já estão definidos
- a API pública está quase estabilizada
- mudanças passam a ser pontuais

### Release Candidate (`rc`)
Exemplo:

```
0.1.0rc1
```

Usado quando:
- não há novas funcionalidades planejadas
- apenas correções de bugs são permitidas
- o pacote está pronto para validação final

## Compromisso de estabilidade

- Até a versão **1.0.0**, a API pública pode mudar.
- A partir da versão **1.0.0**, a API pública passa a ser estável
  e segue estritamente o Semantic Versioning.
