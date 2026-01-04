**Purpose**: 해커톤 참가자 포트폴리오 테이블 자동 업데이트

---

## Command Execution

해커톤 참가자들의 GitHub 리포지토리 및 GitHub Pages 정보를 조회하여 README.md의 포트폴리오 테이블을 최신 상태로 업데이트합니다.

### 실행 단계

1. **포트폴리오 테이블 생성**
   - `make portfolio` 명령 실행
   - attendee.csv에서 참가자 정보 읽기
   - GitHub API를 통해 각 참가자의 2025-12-22 이후 생성된 리포지토리 조회
   - GitHub Pages 활성화 상태 확인

2. **README.md 업데이트**
   - 생성된 테이블로 기존 포트폴리오 섹션 교체
   - `## 👥 해커톤 참가자 및 포트폴리오` 섹션의 테이블 갱신
   - `**참고**:` 섹션은 유지

3. **결과 요약**
   - 총 참가자 수
   - 새로 추가되거나 변경된 리포지토리
   - 경고 메시지 (GitHub ID 오류 등)

### 사전 요구사항
- GitHub CLI (`gh`) 설치 및 인증
- Python 3.x
- attendee.csv 파일 존재

### 참가자 추가
새 참가자를 추가하려면 attendee.csv에 다음 형식으로 추가:
```
타임스탬프,이메일,이름,GitHub_Username,리포지토리_URL
```

### 주의사항
- API 호출이 많아 실행에 1-2분 소요될 수 있음
- attendee.csv는 gitignore 대상이므로 별도 관리 필요
