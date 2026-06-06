
[ORCID: 0009-0004-1872-1153](https://orcid.org/my-orcid?orcid=0009-0004-1872-1153)  
[Zenodo DOI: 10.5281/zenodo.20571650](https://doi.org/10.5281/zenodo.20571650)

---

## Overview / Обзор

**EN.** GRA-Core-new is the production‑ready implementation of the GRA methodology (Gödel‑Reductio ad Absurdum), consolidating 103 research projects from the `qqewq` ecosystem into a single hierarchical stability core.[page:0]  
It provides a unified codebase for building self‑correcting hierarchical systems with explicit guarantees of stability under perturbations.[page:0]

**RU.** GRA-Core-new — это production‑ready реализация методологии GRA (Gödel‑Reductio ad Absurdum), объединяющая 103 исследовательских проекта экосистемы `qqewq` в единое ядро иерархической стабильности.[page:0]  
Библиотека даёт единую кодовую базу для построения самоисправляющихся иерархических систем с явными гарантиями устойчивости к возмущениям.[page:0]

Все родовые репозитории и источники идеи перечислены в `archive/README.md`.[page:0]  
All ancestor repositories and idea sources are listed in `archive/README.md`.[page:0]

---

## Key capabilities / Ключевые возможности

**EN. Core ideas**

- True contradiction metrics (“foam” Φ) for banks, drone swarms, LLMs, biology and subjective layers.[page:0]  
- Hierarchical structure with lifting operators and consistency penalties between levels.[page:0]  
- GRA‑step via criticism and revision instead of naive multiplicative decay.[page:0]  
- Full functional \(J\) with gradient descent and stability checks.[page:0]  
- Multiverse alignment, distributed swarms (military GRA, health swarm) and hybrid resonance algorithms.[page:0]  

**RU. Основные идеи**

- Настоящие метрики противоречий («пена» Φ) для банков, роёв дронов, LLM, биологии и слоёв субъективности.[page:0]  
- Иерархическая структура с операторами подъёма и штрафами согласованности между уровнями.[page:0]  
- GRA‑шаг через критику и пересмотр, а не через наивное умножение на коэффициент.[page:0]  
- Полный функционал J с градиентным спуском и проверкой устойчивости.[page:0]  
- Мультиверсное выравнивание, распределённые рои (военный GRA, рой здоровья) и гибридные резонансные алгоритмы.[page:0]  

Подробное математическое изложение см. в `gra-core-new-en.pdf` и `gra-core-new-ru.pdf`.[page:0]  
For detailed math see `gra-core-new-en.pdf` and `gra-core-new-ru.pdf`.[page:0]

---

## Repository structure / Структура репозитория

**EN**

- `gra_core/` — main Python package with core data structures, foam metrics, operators and stability checks.[page:0]  
- `demo/` — runnable examples of typical scenarios (banks, drones, LLM, bio, multiverse).[page:0]  
- `tests/` — unit tests for core modules and stability contracts.[page:0]  
- `docs/` — additional documentation and helper diagrams.[page:0]  
- `archive/` — index of the 103 original research repositories integrated into this core.[page:0]  
- `paper-en.tex`, `paper-ru.tex` — LaTeX sources of the scientific paper (EN/RU).[page:0]  
- `gra-core-new-en.pdf`, `gra-core-new-ru.pdf` — compiled PDFs of the paper (EN/RU).[page:0]  

**RU**

- `gra_core/` — основной Python‑пакет с ключевыми структурами данных, метриками пены, операторами и проверками стабильности.[page:0]  
- `demo/` — исполняемые примеры типичных сценариев (банки, дроны, LLM, био, мультиверс).[page:0]  
- `tests/` — модульные тесты для ядра и контрактов устойчивости.[page:0]  
- `docs/` — дополнительная документация и вспомогательные схемы.[page:0]  
- `archive/` — список 103 исходных исследовательских репозиториев, собранных в это ядро.[page:0]  
- `paper-en.tex`, `paper-ru.tex` — LaTeX‑исходники научной статьи (EN/RU).[page:0]  
- `gra-core-new-en.pdf`, `gra-core-new-ru.pdf` — готовые PDF‑версии статьи (EN/RU).[page:0]  

---

## Installation / Установка

**EN**

```bash
git clone https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library.git
cd GRA-Core-new-Unified-Hierarchical-Stability-Library
pip install -r requirements.txt
pip install -e .
```
[page:0]

**RU**

```bash
git clone https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library.git
cd GRA-Core-new-Unified-Hierarchical-Stability-Library
pip install -r requirements.txt
pip install -e .
```
[page:0]

---

## Quickstart / Быстрый старт

**EN. Minimal example**

```python
from gra_core import gra_system

# 1. Build a simple hierarchical system
system = gra_system.create_default_system()

# 2. Inject observations / constraints
system.observe("bank_liquidity", value=0.72)
system.observe("drone_swarm_error", value=0.18)

# 3. Run one GRA-step (critique + revision)
system.step()

# 4. Check stability
phi, dphi, d2phi = system.stability_metrics()
print("Φ =", phi, "ΔΦ =", dphi, "Δ²Φ =", d2phi)
```

More examples are available in `demo/` (multiverse, swarms, bio, cinema).[page:0]

**RU. Минимальный пример**

```python
from gra_core import gra_system

# 1. Собираем простую иерархическую систему
system = gra_system.create_default_system()

# 2. Добавляем наблюдения / ограничения
system.observe("bank_liquidity", value=0.72)
system.observe("drone_swarm_error", value=0.18)

# 3. Запускаем один GRA‑шаг (критика + пересмотр)
system.step()

# 4. Проверяем устойчивость
phi, dphi, d2phi = system.stability_metrics()
print("Φ =", phi, "ΔΦ =", dphi, "Δ²Φ =", d2phi)
```

Дополнительные примеры см. в каталоге `demo/` (мультиверс, рои, биология, кино).[page:0]

---

## Conceptual modules / Концептуальные модули

**EN**

Typical conceptual components exposed by `gra_core`:

- Foam metric Φ and its derivatives (ΔΦ, Δ²Φ) as core contradiction measures.[page:0]  
- Hierarchical levels with lift / project operators and consistency penalties between levels.[page:0]  
- GRA‑step operator implementing critique‑revision dynamics.[page:0]  
- Stability checker enforcing Φ=0, ΔΦ=0, Δ²Φ>0 for equilibria and perturbation tests.[page:0]  

**RU**

Типичные концептуальные компоненты, реализованные в `gra_core`:

- Метрика пены Φ и её производные (ΔΦ, Δ²Φ) как базовые меры противоречия.[page:0]  
- Иерархические уровни с операторами подъёма/проекции и штрафами несогласованности.[page:0]  
- Оператор GRA‑шага, реализующий динамику критики и пересмотра.[page:0]  
- Проверка устойчивости, навязывающая условия Φ=0, ΔΦ=0, Δ²Φ>0 для равновесий и тесты на возмущения.[page:0]  

---

## Papers and citation / Статьи и цитирование

**EN**

- Full English paper: `gra-core-new-en.pdf` (LaTeX: `paper-en.tex`).[page:0]  
- Full Russian paper: `gra-core-new-ru.pdf` (LaTeX: `paper-ru.tex`).[page:0]  
- Persistent record: Zenodo DOI [10.5281/zenodo.20571650](https://doi.org/10.5281/zenodo.20571650).[page:0]  

When using this library in research, please cite the Zenodo record:

> Bitsoev O. GRA-Core-new: Unified Hierarchical Stability Library. Zenodo. DOI: 10.5281/zenodo.20571650.[page:0]

**RU**

- Полная англоязычная статья: `gra-core-new-en.pdf` (LaTeX: `paper-en.tex`).[page:0]  
- Полная русскоязычная статья: `gra-core-new-ru.pdf` (LaTeX: `paper-ru.tex`).[page:0]  
- Постоянная запись: Zenodo DOI [10.5281/zenodo.20571650](https://doi.org/10.5281/zenodo.20571650).[page:0]  

При использовании библиотеки в исследованиях, пожалуйста, цитируйте запись на Zenodo:

> Bitsoev O. GRA-Core-new: Unified Hierarchical Stability Library. Zenodo. DOI: 10.5281/zenodo.20571650.[page:0]

---

## License / Лицензия

**EN.** The project is distributed under the MIT license — see `License.txt` in the repository root.[page:0]  
**RU.** Проект распространяется по лицензии MIT — см. файл `License.txt` в корне репозитория.[page:0]
