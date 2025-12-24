# Portfolio Hackerton: AI 기반 소프트웨어 엔지니어링 및 커리어 가이드

이 리포지토리는 취업을 위한 포트폴리오 제작 해커톤의 운영 및 교육 자료를 담고 있습니다. 대학생과 주니어 개발자가 생성형 AI를 활용하여 효율적으로 학습하고, 모던 소프트웨어 엔지니어링 원칙을 이해하며, 올바른 개발 습관을 형성하는 것을 돕습니다.

## 📂 주요 목차

### 1. 학습 및 커리어 가이드 (`docs/`)
*   **[생성형 AI 활용 전략](docs/HowtoLearnFasterwithAI.md)**: 챗GPT를 활용한 프로그래밍, 영어, 전공 학습 및 학습 동기 유지 전략 (해라체 버전).
*   **모던 소프트웨어 엔지니어링**: Dave Farley의 'Modern Software Engineering' 핵심 요약
    *   **[Part 1: 엔지니어링이란 무엇인가?](docs/ModernSoftwareEngineering/Part1.md)**
    *   **[Part 2: 복잡성을 관리하는 원칙](docs/ModernSoftwareEngineering/Part2.md)**
    *   **[Part 3: 실천 및 엔지니어의 자세](docs/ModernSoftwareEngineering/Part3.md)**
*   **[프로젝트 배경 및 서사](docs/Narratave.md)**: 이 프로젝트가 시작된 배경과 목적에 대한 이야기.

### 2. 교육용 슬라이드 (`slides/`)
Marp를 활용하여 제작된 발표 자료입니다.
*   `00-Motivation.md`: 동기 부여 및 학습의 의의
*   `01-Intro.md`: 해커톤 및 과정 소개
*   `02-AIDrivenStudy.md`: AI를 활용한 학습 방법론
*   `03-Habits.md`: 실력 있는 개발자가 되기 위한 핵심 습관 설정

---

## 🛠 사용 방법

### 슬라이드 빌드 및 관리
본 리포지토리는 `Marp CLI`와 `Makefile`을 사용하여 마크다운 슬라이드를 HTML 및 PPTX 형식으로 변환합니다.

#### 사전 준비
```bash
npm install
```

#### 주요 명령어
*   **모든 슬라이드 빌드**: `make all` (HTML, PPTX 생성)
*   **특정 슬라이드 빌드**: `make slide NAME=03-Habits`
*   **실시간 미리보기**: `make preview NAME=03-Habits`
*   **변경 사항 감시 및 자동 빌드**: `make watch`
*   **생성된 파일 삭제**: `make clean`

결과물은 `slides/output/` 디렉토리에 저장됩니다.

---

## 🚀 목표
1. **AI Native 학습**: 생성형 AI를 도구가 아닌 멘토로 활용하는 능력 배양
2. **엔지니어링 사고**: 단순히 코드를 짜는 것을 넘어, 과학적 방법론에 기반한 엔지니어링 원칙 습득
3. **지속 가능한 습관**: 장기적으로 성장할 수 있는 일일 루틴 및 집중 환경 구축

---

## 👥 해커톤 참가자 및 포트폴리오

2025년 12월 22일 해커톤에 참가한 학생들의 GitHub 계정 및 포트폴리오 리포지토리 목록입니다.

| GitHub ID | 이름 | 포트폴리오 리포지토리 | GitHub Pages |
|-----------|------|----------------------|--------------|
| [Seogaeun03](https://github.com/Seogaeun03) | 서가은 | [ai_project](https://github.com/Seogaeun03/ai_project), [calculator-demo](https://github.com/Seogaeun03/calculator-demo), [The_Corporate_Shield](https://github.com/Seogaeun03/The_Corporate_Shield) | [The_Corporate_Shield](https://seogaeun03.github.io/The_Corporate_Shield/) |
| [baobabkim](https://github.com/baobabkim) | 김도현 | [apply-demo-1](https://github.com/baobabkim/apply-demo-1), [apply-demo-2](https://github.com/baobabkim/apply-demo-2) | - |
| [minjae-488](https://github.com/minjae-488) | 서민재 | [baseball](https://github.com/minjae-488/baseball), [baseball2](https://github.com/minjae-488/baseball2), [carculator_demo](https://github.com/minjae-488/carculator_demo), [hanwhalinup](https://github.com/minjae-488/hanwhalinup) | [baseball2](https://minjae-488.github.io/baseball2/), [carculator_demo](https://minjae-488.github.io/carculator_demo/), [hanwhalinup](https://minjae-488.github.io/hanwhalinup/) |
| [nohyujin](https://github.com/nohyujin) | 노유진 | [calculator](https://github.com/nohyujin/calculator), [Coop](https://github.com/nohyujin/Coop), [LnS](https://github.com/nohyujin/LnS), [local-andon](https://github.com/nohyujin/local-andon), [new](https://github.com/nohyujin/new), [second](https://github.com/nohyujin/second) | [calculator](https://nohyujin.github.io/calculator/), [LnS](https://nohyujin.github.io/LnS/), [second](https://nohyujin.github.io/second/) |
| [chp2](https://github.com/chp2) | 박창훈 | [Calculator-demo](https://github.com/chp2/Calculator-demo), [demo1](https://github.com/chp2/demo1), [Five-in-a-row](https://github.com/chp2/Five-in-a-row) | [Calculator-demo](https://chp2.github.io/Calculator-demo/), [demo1](https://chp2.github.io/demo1/) |
| [yeneua](https://github.com/yeneua) | 김예나 | [calculator](https://github.com/yeneua/calculator), [toss-apply-demo](https://github.com/yeneua/toss-apply-demo) | [calculator](https://yeneua.github.io/calculator/), [toss-apply-demo](https://yeneua.github.io/toss-apply-demo/) |
| [DongKim2](https://github.com/DongKim2) | 김동환 | [black_scholes-model](https://github.com/DongKim2/black_scholes-model), [cal1](https://github.com/DongKim2/cal1), [calculator-demo](https://github.com/DongKim2/calculator-demo), [CAMP-2025_winter](https://github.com/DongKim2/CAMP-2025_winter), [CAMP_P_R_repository](https://github.com/DongKim2/CAMP_P_R_repository), [TASKS.md](https://github.com/DongKim2/TASKS.md) | [CAMP_P_R_repository](https://dongkim2.github.io/CAMP_P_R_repository/) |
| [lsm427654-source](https://github.com/lsm427654-source) | 임선민 | [calculating](https://github.com/lsm427654-source/calculating), [ERP](https://github.com/lsm427654-source/ERP), [upstages](https://github.com/lsm427654-source/upstages), [VAT](https://github.com/lsm427654-source/VAT) | [calculating](https://lsm427654-source.github.io/calculating/), [ERP](https://lsm427654-source.github.io/ERP/), [VAT](https://lsm427654-source.github.io/VAT/) |
| [Jee-Seung](https://github.com/Jee-Seung) | 한지승 | [Demo-Calculator](https://github.com/Jee-Seung/Demo-Calculator), [project_1](https://github.com/Jee-Seung/project_1), [test](https://github.com/Jee-Seung/test) | [Demo-Calculator](https://jee-seung.github.io/Demo-Calculator/) |
| [junhachoe61-dotcom](https://github.com/junhachoe61-dotcom) | 최준하 | [calculator-demo](https://github.com/junhachoe61-dotcom/calculator-demo), [data](https://github.com/junhachoe61-dotcom/data), [Data-Enginnering](https://github.com/junhachoe61-dotcom/Data-Enginnering), [Data_pipeline](https://github.com/junhachoe61-dotcom/Data_pipeline), [subway_flow](https://github.com/junhachoe61-dotcom/subway_flow) | [calculator-demo](https://junhachoe61-dotcom.github.io/calculator-demo/), [data](https://junhachoe61-dotcom.github.io/data/) |
| [hennessynlove7552](https://github.com/hennessynlove7552) | 이현주 | [calculator](https://github.com/hennessynlove7552/calculator), [commodity-tracker](https://github.com/hennessynlove7552/commodity-tracker), [engineering-calculator](https://github.com/hennessynlove7552/engineering-calculator), [newproject](https://github.com/hennessynlove7552/newproject) | [commodity-tracker](https://hennessynlove7552.github.io/commodity-tracker/), [newproject](https://hennessynlove7552.github.io/newproject/) |
| [kwang-min13](https://github.com/kwang-min13) | 남광민 | [calculator](https://github.com/kwang-min13/calculator), [STEP1](https://github.com/kwang-min13/STEP1) | [calculator](https://kwang-min13.github.io/calculator/), [STEP1](https://kwang-min13.github.io/STEP1/) |
| [jinseungwook](https://github.com/jinseungwook) | 진승욱 | [busanbank](https://github.com/jinseungwook/busanbank), [calculate](https://github.com/jinseungwook/calculate) | [busanbank](https://jinseungwook.github.io/busanbank/), [calculate](https://jinseungwook.github.io/calculate/) |
| [ldw188918-hue](https://github.com/ldw188918-hue) | 이동욱 | [Calculator](https://github.com/ldw188918-hue/Calculator), [calculator-demo](https://github.com/ldw188918-hue/calculator-demo), [Dong-Uk](https://github.com/ldw188918-hue/Dong-Uk), [Project](https://github.com/ldw188918-hue/Project), [upstage-demo](https://github.com/ldw188918-hue/upstage-demo) | [Calculator](https://ldw188918-hue.github.io/Calculator/), [Dong-Uk](https://ldw188918-hue.github.io/Dong-Uk/), [Project](https://ldw188918-hue.github.io/Project/) |
| [ts6nqswnr8-sudo](https://github.com/ts6nqswnr8-sudo) | 김채린 | [calculator-demo](https://github.com/ts6nqswnr8-sudo/calculator-demo), [UpstageDemo](https://github.com/ts6nqswnr8-sudo/UpstageDemo) | [UpstageDemo](https://ts6nqswnr8-sudo.github.io/UpstageDemo/) |
| [CSY-333](https://github.com/CSY-333) | 진시우 | [calculator-demo](https://github.com/CSY-333/calculator-demo), [Crowling](https://github.com/CSY-333/Crowling), [Generative-Multi-Agent-Sitcom-Simulator](https://github.com/CSY-333/Generative-Multi-Agent-Sitcom-Simulator), [GPR](https://github.com/CSY-333/GPR) | [calculator-demo](https://csy-333.github.io/calculator-demo/), [Generative-Multi-Agent-Sitcom-Simulator](https://csy-333.github.io/Generative-Multi-Agent-Sitcom-Simulator/) |
| [hamjang](https://github.com/hamjang) | 함승훈 | [RAG-demo](https://github.com/hamjang/RAG-demo) | - |
| [tlstn3172](https://github.com/tlstn3172) | 이세현 | [calculator-demo](https://github.com/tlstn3172/calculator-demo), [earthworm-game-demo](https://github.com/tlstn3172/earthworm-game-demo), [national-pension-demo](https://github.com/tlstn3172/national-pension-demo), [steam-discount-demo](https://github.com/tlstn3172/steam-discount-demo), [upstage-apply-demo](https://github.com/tlstn3172/upstage-apply-demo), [weather-forecaster-demo](https://github.com/tlstn3172/weather-forecaster-demo) | [calculator-demo](https://tlstn3172.github.io/calculator-demo/), [earthworm-game-demo](https://tlstn3172.github.io/earthworm-game-demo/), [national-pension-demo](https://tlstn3172.github.io/national-pension-demo/), [steam-discount-demo](https://tlstn3172.github.io/steam-discount-demo/), [weather-forecaster-demo](https://tlstn3172.github.io/weather-forecaster-demo/) |
| [JoGiJun](https://github.com/JoGiJun) | 조기준 | [calculator-demo](https://github.com/JoGiJun/calculator-demo), [stat-stat](https://github.com/JoGiJun/stat-stat), [stat-stat_v2](https://github.com/JoGiJun/stat-stat_v2) | [calculator-demo](https://jogijun.github.io/calculator-demo/), [stat-stat](https://jogijun.github.io/stat-stat/) |
| [yonghwan-ko02](https://github.com/yonghwan-ko02) | 고용환 | [calculator-demo](https://github.com/yonghwan-ko02/calculator-demo), [Project](https://github.com/yonghwan-ko02/Project), [project01](https://github.com/yonghwan-ko02/project01) | [calculator-demo](https://yonghwan-ko02.github.io/calculator-demo/), [Project](https://yonghwan-ko02.github.io/Project/) |
| [Bsagom](https://github.com/Bsagom) | 배성환 | [Calculator-Demo](https://github.com/Bsagom/Calculator-Demo), [demo](https://github.com/Bsagom/demo), [Demo2](https://github.com/Bsagom/Demo2), [Demo3](https://github.com/Bsagom/Demo3) | [Calculator-Demo](https://bsagom.github.io/Calculator-Demo/), [Demo2](https://bsagom.github.io/Demo2/) |
| [megaTRX](https://github.com/megaTRX) | 최대영 | [calculator](https://github.com/megaTRX/calculator), [Embedded-Portfolio](https://github.com/megaTRX/Embedded-Portfolio), [upstage-apply-demo](https://github.com/megaTRX/upstage-apply-demo) | [calculator](https://megatrx.github.io/calculator/), [upstage-apply-demo](https://megatrx.github.io/upstage-apply-demo/) |
| [2216259-ctrl](https://github.com/2216259-ctrl) | 조은수 | [calculator-demo](https://github.com/2216259-ctrl/calculator-demo), [PomodoroTimer-demo](https://github.com/2216259-ctrl/PomodoroTimer-demo), [upstage-apply-demo](https://github.com/2216259-ctrl/upstage-apply-demo) | [calculator-demo](https://2216259-ctrl.github.io/calculator-demo/), [upstage-apply-demo](https://2216259-ctrl.github.io/upstage-apply-demo/) |
| [hyeonz673](https://github.com/hyeonz673) | 황현지 | [calculator-demo](https://github.com/hyeonz673/calculator-demo), [legal-chatbot](https://github.com/hyeonz673/legal-chatbot), [Local-Legal-Insight](https://github.com/hyeonz673/Local-Legal-Insight), [RAG](https://github.com/hyeonz673/RAG), [recipe](https://github.com/hyeonz673/recipe) | [legal-chatbot](https://hyeonz673.github.io/legal-chatbot/), [recipe](https://hyeonz673.github.io/recipe/) |

**참고**:
- 위 리포지토리들은 2025년 12월 22일 이후 생성된 해커톤 포트폴리오 프로젝트입니다.
- GitHub Pages 링크는 `has_pages: true`로 설정된 리포지토리를 기준으로 작성되었습니다.
- 일부 계정(chulsuun, ShinEunJi8)은 존재하지 않거나 접근할 수 없습니다.