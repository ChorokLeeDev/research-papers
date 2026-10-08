# [arXiv 2512.22318v3 → v4] 사전 검증 주장 정정과 재구성 실험·수정 표 반영

공개 v3는 이미 확장된 3-graph 연구이며, 소스 34개 파일이 보존된 확장 ZIP과 정확히 일치합니다. 새로운 감사본은 과거 실행·미관찰 외부 데이터 주장과 일부 수치를 수정하므로 arXiv 개정이 필요합니다.

변경 사항:
- 계정 내 과거 연구에 CoDEx 결과가 존재하므로, 완전히 미관찰된 외부 데이터 또는 검증된 사전 실행 순서라는 해석을 철회합니다.
- 복구하지 못한 원래 추가 실험과 새로 수행한 고정 프로토콜 재구성을 구분합니다. 원래 검사기의 미확인 검증 실적을 새 검사기의 결과로 대체해 소급 인증하지 않습니다.
- CoDEx 6개 모델 단계, 42개 head, 18개 relation-ID 과제, 6개 grouped reciprocal 분석을 새로 보존하고 수정 표를 반영합니다.
- 일부 FB15k-237 ensemble 수치 차이와 위험 지표 악화를 숨기지 않고 기록합니다.

검증: 별도 검토에서 77,595개 질의 기록, checkpoint·head 재생, 216개 후보 재적합, 표 462개 수치를 확인했습니다. 테스트 99개 통과; 44쪽 PDF와 34개 파일 소스 패키지 일치.

수정 PDF: https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/af000ebf0c896c4ab0a75ad0f8874077c1eece0a/output/kg-uncertainty-expanded-audit-20261008.pdf
수정 소스: https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/af000ebf0c896c4ab0a75ad0f8874077c1eece0a/output/kg-uncertainty-expanded-audit-20261008-source.zip
상세 판단: https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/af000ebf0c896c4ab0a75ad0f8874077c1eece0a/audit/2026-10-08/expanded-evidence-recovery.md
독립 검토: https://github.com/ChorokLeeDev/kg-uncertainty-revision/blob/af000ebf0c896c4ab0a75ad0f8874077c1eece0a/audit/2026-10-08/expanded-reconstruction-recheck.md

완료 조건: 재구성의 사후성·원래 자료의 한계를 유지한 v4 PDF/소스 검토, 변경 설명 작성, 저자 제출 후 새 버전 URL 기록. 현재 arXiv 제출은 수행하지 않았습니다.
