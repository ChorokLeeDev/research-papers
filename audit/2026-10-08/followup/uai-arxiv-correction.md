# [arXiv 2601.00908v2] 통계 정정과 복구 자료 재검증을 반영한 개정본 준비

공개 arXiv v2의 원본 TeX·참고문헌이 보존된 camera-ready와 바이트 단위로 일치함을 확인했습니다. 현재 수정은 과학적 해석을 바꾸므로 arXiv 개정이 필요합니다.

변경 사항:
- APS 정의·정리 조건과 잘못된 ICC/클래스 수·다중검정 해석을 정정합니다.
- 복구한 후속 연구 24개 모델을 재학습해 528개 배열이 정확히 재현됐지만, 8개 과제의 집중도–coverage 하락 상관은 −0.238/−0.262로 기존 양의 상관을 재현하지 못했습니다.
- 복구한 고정 데이터에서 날짜로 잘린 entity join이 테스트 ID를 모두 누락시키는 문제를 입증했습니다. 이를 원래 50시드 결과의 원인이라고 단정하지 않습니다.
- 복구된 코드가 실제 재학습 대신 집계 수치를 변형하며 원래 재학습 기록도 확인되지 않아, 하이퍼파라미터 강건성 주장과 근거 없는 배포 임계값·운영 지침을 철회합니다.

검증: 원자료·모델 재생, 24회 고정 프로토콜 재학습, 별도 검토자의 528개 배열·60만 라벨·분할 시간순서 검증, 수정 원고/PDF 교차검증 완료.

수정본: https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/533814f27add9dd05bcebb74e71ea21bfeb76649/audit/2026-10-08/revision/uai-statistical-audit-revision.pdf
상세 판단: https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/533814f27add9dd05bcebb74e71ea21bfeb76649/audit/2026-10-08/recovery/arxiv-assessment.md
독립 검토: https://github.com/ChorokLeeDev/conformal-covid-uai2026/blob/533814f27add9dd05bcebb74e71ea21bfeb76649/audit/2026-10-08/recovery-independent-recheck.md

완료 조건: 원래 50시드 자료와 새 후속 재현을 명확히 구분한 개정 PDF·소스 패키지 검토, 비공개 원자료 접근 범위 공개, arXiv 변경 설명 작성, 저자 제출 후 새 버전 URL 기록. 현재 arXiv 제출은 수행하지 않았습니다.
