# Programmers_Algorithm

[프로그래머스](https://school.programmers.co.kr/)에서 Python으로 푼 알고리즘 문제들을 기록하는 저장소입니다.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Programmers](https://img.shields.io/badge/Programmers-000000?style=flat&logo=programmers&logoColor=white)

---

## 소개

문제를 풀고 끝내는 게 아니라, 어떤 방식으로 접근했는지 · 어디서 막혔는지 · 왜 그 풀이가 맞는지를 함께 기록하는 것을 목표로 합니다. 각 문제는 마크다운 파일 하나에 문제 설명, 제한사항, 입출력 예, 풀이 방식, 코드를 함께 담았습니다. 막혔거나 실패한 시도도 지우지 않고 그대로 남겨서, 나중에 다시 봤을 때 그때 무엇을 몰랐는지 확인할 수 있게 했습니다.

## 폴더 구조

```
Programmers_Algorithm/
├── README.md
└── *.md          # 문제 하나당(또는 묶음당) 마크다운 파일 하나
```

각 문제 파일은 보통 아래 형식을 따릅니다.

- `## 문제 설명` / `## 제한사항` — 원문 요약
- `## 입출력 예` — 공식 예제 표
- `## 풀이` — 접근 방식과 핵심 로직 설명
- `## 시행착오` / `## 실패 이유` — 막혔던 지점이나 처음에 틀렸던 이유 (있는 경우만)
- 코드 블록 — 실제 제출/작성한 Python 코드

## 문제 목록

### 기초 (Lv.0 모음)

| 파일 | 내용 |
| --- | --- |
| [python_solutions.md](./python_solutions.md) | Lv.0 기초 문제 10개 모음 |
| [algorithm_day3.md](./algorithm_day3.md) | Lv.0 기초 문제 10개 모음 (3일차) |

### 스택 / 큐

| 문제 | 유형 | 파일 |
| --- | --- | --- |
| 올바른 괄호 | 스택 | [valid_parentheses.md](./valid_parentheses.md) |
| 괄호 변환 (Kakao 2020) | 문자열/재귀 | [correct_brackets.md](./correct_brackets.md) |
| 프로세스 우선순위 | 큐 | [process_priority.md](./process_priority.md) |
| 기능개발 | 큐/시뮬레이션 | [feature_development.md](./feature_development.md) |
| 다리를 지나는 트럭 | 큐/시뮬레이션 | [truck_bridge.md](./truck_bridge.md) |

### 정렬 / 투 포인터

| 문제 | 유형 | 파일 |
| --- | --- | --- |
| 전화번호 목록 | 정렬/문자열 | [phone_book.md](./phone_book.md), [phone_book_v2.md](./phone_book_v2.md) |
| 구명보트 | 그리디/투 포인터 | [lifeboat.md](./lifeboat.md) |
| 호텔 대실 | 투 포인터 | [hotel_room.md](./hotel_room.md) |
| 연속된 부분 수열의 합 | 투 포인터 | [subsequence_sum.md](./subsequence_sum.md) |
| 큰 수 만들기 | 그리디 | [biggest_number.md](./biggest_number.md) |

### 완전탐색 / DFS·백트래킹

| 문제 | 유형 | 파일 |
| --- | --- | --- |
| 타겟 넘버 | DFS/백트래킹 | [target_number.md](./target_number.md) |
| 소수 찾기 (종이 조각) | 순열/소수판별 | [prime_number_paper.md](./prime_number_paper.md) |
| 소수 만들기 | 조합/소수판별 | [prime_number_sum.md](./prime_number_sum.md) |
| 파괴되지 않은 건물 | 완전탐색 (효율성 실패) | [destroyed_buildings.md](./destroyed_buildings.md) |

### 그래프 / BFS / 그리디

| 문제 | 유형 | 파일 |
| --- | --- | --- |
| 전력망을 둘로 나누기 | BFS | [power_grid.md](./power_grid.md) |
| 섬 연결하기 | 그리디 (MST) | [bridge_building.md](./bridge_building.md) |

### 이분 탐색 / 수학 / 구현

| 문제 | 유형 | 파일 |
| --- | --- | --- |
| 입국심사 | 이분 탐색 | [immigration.md](./immigration.md) |
| 숫자의 표현 | 수학 | [number_expression.md](./number_expression.md) |
| 키패드 누르기 | 시뮬레이션/구현 | [keypad.md](./keypad.md) |
| 같은 숫자는 싫어 | 배열/구현 | [no_duplicates.md](./no_duplicates.md) |

### 도전 중 / 미완성 (실패 기록)

풀이 도중 막혀서 끝까지 완성하지 못했거나, 실행 중 오류가 발견된 시도도 남겨둡니다. 나중에 다시 도전할 때 참고용입니다.

| 문제 | 유형 | 파일 | 상태 |
| --- | --- | --- | --- |
| 여행경로 | DFS/백트래킹 | [travel_route.md](./travel_route.md) | 구현 중 막힘 |
| 카드 짝맞추기 (2021 Kakao) | DFS/BFS | [card_matching.md](./card_matching.md) | 구현 중 막힘 |
| 퍼즐 조각 채우기 | 구현 | [puzzle_piece.md](./puzzle_piece.md) | 구현 중 막힘 |

## 기록 방식

- 문제를 처음 풀 때 겪은 시행착오는 결과론적인 지적이 아니라, 그 순간에 어떤 접근을 시도했고 어디서 막혔는지를 그대로 남깁니다.
- 코드가 실제로 정답 예제를 통과하는지는 직접 실행해서 확인한 뒤 기록합니다.
- 같은 문제를 다른 방식으로 다시 풀었을 때는 기존 파일에 풀이를 추가하거나(`## 개선`, `## 성공` 등), 접근 자체가 다르면 `_v2` 형태로 별도 파일을 만듭니다.

## 스터디 블로그

이 저장소의 문제 풀이는 [velog 블로그](https://velog.io/@yhkim819/posts?tag=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%92%80%EC%9D%B4-Python)에도 정리하고 있습니다.
