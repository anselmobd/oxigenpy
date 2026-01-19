# Política de Versionamento — oxigenpy

O oxigenpy segue o padrão **Semantic Versioning** com suporte a
**versões pré-lançamento (pre-release)** conforme definido pela **PEP 440**.

## Versões estáveis

- **PATCH** (`X.Y.Z`)  
  Correção de bugs sem alteração da API pública.

- **MINOR** (`X.Y+1.0`)  
  Adição de novas funcionalidades compatíveis com a API existente.

- **MAJOR** (`X+1.0.0`)  
  Quebras de compatibilidade da API pública.

## Versões pré-lançamento (pre-release)

O projeto utiliza versões **alfa**, **beta** e **release candidate**
para publicar estágios intermediários de uma versão futura,
tanto **antes quanto depois da versão 1.0.0**.

Versões pré-lançamento representam **estados de maturidade** de uma
versão específica (por exemplo, `0.1.0` ou `1.1.0`), e **não** versões
menores que `PATCH`, `MINOR` ou `MAJOR`.

### Alpha (`a`)

Exemplos:

```
0.1.0a1
0.1.0a2
1.1.0a1
```

Usado para:
- adição de novos módulos
- evolução da estrutura interna
- expansão de testes
- mudanças frequentes ou experimentais de API

### Beta (`b`)

Exemplos:

```
0.1.0b1
1.1.0b1
```

Usado quando:
- os módulos principais já estão definidos
- a API pública está quase estabilizada
- mudanças passam a ser pontuais e controladas

### Release Candidate (`rc`)
Exemplos:

```
0.1.0rc1
1.1.0rc1
```

Usado quando:
- não há novas funcionalidades planejadas
- apenas correções de bugs são permitidas
- o pacote está pronto para validação final antes do release estável

## Compromisso de estabilidade

- Até a versão **1.0.0**, a API pública deve ser considerada instável e pode mudar sem aviso prévio.
- A partir da versão **1.0.0**, a API pública passa a ser considerada estável e segue estritamente o Semantic Versioning.
- Versões pré-lançamento **não** carregam compromisso de estabilidade, mesmo após a versão 1.0.0.
