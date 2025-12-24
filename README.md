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