# Health

# Server

## 라이브러리 설치

```
pip install flask
pip install pandas
pip install psycopg2
pip install flask_restx
```

## 실행방법입니다.
`최상위 폴더에서 python start_server 로 서버실행 `

## API 설명입니다

### person
API | Method | Address
:-----|:------:|:------|
전체 환자수 조회 API | GET | http://0.0.0.0:5000/person |
성별 환자수 조회 API | GET | http://0.0.0.0:5000/person/gender |
인종별 환자수 조회 API | GET | http://0.0.0.0:5000/person/race |
민족별 환자수 조회 API | GET | http://0.0.0.0:5000/person/ethnicity |
사망 환자수 조회 API | GET | http://0.0.0.0:5000/person/death |


### serch
API | Method | Address
:-----|:------:|:------|
concept_id 정보 조회 API | GET | http://0.0.0.0:5000/concept/:id |

### visit
API | Method | Address
:-----|:------:|:------|
방문유형별 방문수 조회 API | GET | http://0.0.0.0:5000/visit |
성별 방문수 조회 API | GET | http://0.0.0.0:5000/visit/gender |

---------

순위 설정
테이블간의 관계가 적고 기능이 없는 단순 조회부터 해결한 뒤, 기능이 있는 조회 구현순서로 순위를 설정하였습니다.  
따라서 1번 환자테이블 -> 2번 검색기능 -> 1번 방문테이블 -> 3번 순서로 순위를 생각하였습니다. 

기능별로 라우터 분리가 필요합니다.

방문유형별 방문수 조회 기능은 visit_concept_id 이름을 알기위해 concept테이블과의 관계가 필요할것같습니다.  
1번 방문테이블별 조회기능은 성별 방문수 조회기능 쿼리에서 성별을 각 필드별 이름만 바꿔서 구현하면 될것같다고 생각하였습니다.  
3번의 row조회 쿼리는 2번 검색기능과 1번 조회기능을 적절히 섞어서 구현하면 될것같다고 생각하였습니다.






