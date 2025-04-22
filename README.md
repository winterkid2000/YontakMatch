# YontakMatch
# 🚕 YontakMatch (연택 매칭 서비스)

Yonsei Move Match System for Mirae Campus
연세대학교 미래캠퍼스의 '연택' 택시 시스템을 위한 동승자 실시간 매칭 플랫폼입니다.

본 프로젝트는 FastAPI 기반 백엔드로, 프론트엔드(YMove)에서 입력된 동승 요청 데이터를 받아,  
경로와 시간 기준으로 유사한 사용자들과 자동 매칭 및 그룹 생성을 처리합니다.

---

## 주요 기능 (MVP 기준)

- ✅ 회원가입 없이 "게스트" 닉네임 기반 요청 등록
- ✅ 출발지 / 도착지 / 시간 기준 동승자 요청 생성
- ✅ 유사 경로 요청 리스트 제공
- ✅ 수락 시 RideGroup 자동 생성
- ✅ 그룹 정보 조회 가능
- ✅ API 배포 후 프론트(Vercel)에서 fetch 연동 가능

---

## 🏗 기술 스택

| 항목 | 기술 |
|------|------|
| 백엔드 프레임워크 | FastAPI (Python) |
| DB | SQLite (MVP) / PostgreSQL (생산용) |
| API 배포 | Render (무료 서버) |
| 인증 | 없음 (게스트 기반) |
| 프론트 연동 | React/Next.js 프론트(YMove)에서 fetch 사용 |
| CORS 처리 | 프론트 도메인 허용 방식으로 설정 |
