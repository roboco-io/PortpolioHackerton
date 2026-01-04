# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

취업을 위한 포트폴리오 제작 해커톤의 운영 및 교육 자료 리포지토리. 대학생/주니어 개발자 대상 AI 활용 학습, 모던 소프트웨어 엔지니어링, 개발 습관 형성 교육을 목적으로 함.

## Commands

### Slide Management (Marp CLI)
```bash
npm install                      # Install dependencies
make all                         # Build all slides (HTML + PPTX)
make slide NAME=03-Habits        # Build specific slide
make preview NAME=03-Habits      # Preview in browser
make watch                       # Watch mode for development
make clean                       # Clean generated files
```

Output location: `slides/output/`

### Portfolio Table Generation
```bash
make portfolio                   # Generate from attendee.csv (requires gh CLI)
make portfolio START_DATE=2025-12-20 PORTFOLIO_OUTPUT=output.md
```

### Claude Skill
```
/update-portfolio                # 포트폴리오 테이블 자동 업데이트
```

## Repository Structure

- `docs/` - 학습 및 커리어 가이드 문서
- `slides/` - Marp 마크다운 슬라이드 소스
- `scripts/generate_portfolio_table.py` - 포트폴리오 테이블 생성 스크립트
- `attendee.csv` - 해커톤 참가자 정보 (gitignored)
- `.claude/commands/` - Claude Code 스킬

## Attendee Management

참가자 추가 시 attendee.csv에 다음 형식으로 추가:
```
타임스탬프,이메일,이름,GitHub_Username,리포지토리_URL
```

**주의**: GitHub Username 컬럼에 공백이 포함된 값(예: `Geonyul Shin`)은 무시됨. 정확한 GitHub username 사용 필요.

## Tech Stack

- **Slides**: Marp CLI
- **Portfolio Script**: Python 3 + GitHub CLI (`gh`)
- **Build**: GNU Make
