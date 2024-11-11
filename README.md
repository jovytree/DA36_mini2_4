# Mini Project2 - K3J1
# 🐻 Olive Young 🐻

## 데이터 보고서

### 🫧 데이터셋 설명
- 출처 : kaggle의 데이터(https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews) 
- 데이터 크기 : Sephora 온라인 매장에서 판매되는 모든 뷰티 제품에 대한 정보(2023) 
  - 8,000개 이상의 제품: 제품 이름, 브랜드 이름, 가격, 성분, 평점, 기타 특징
  - 사용자 리뷰 (약 1백만 개의 리뷰, 2,000개 이상의 제품에 대한 리뷰)
  - 
### 👨‍👩‍👧‍👦 팀원소개
- 3명의 김씨(K3)와 1명의 조씨(J1)로 구성된 K3J1
- 김정아, 김진수, 김희애, 조은비

### 🎈데이터 선정 이유
- 화장품 유목민들을 위한 '개인 맞춤 추천'으로 주제 선정
  - 사용자 추천 시스템 구현이라는 주제에 걸맞게 'review' 요소가 많은 프랑스 화장품 유통사 sephora 데이터셋을 선정
  - Index: 1,094,480, columns: 45개의 방대한 데이터로 이뤄졌고, 'primary category', 'secondary category' 등으로 상세 분류가 가능
  - 사용자 평점 예측치, 성분 유사 제품 등으로 화장품 유목민들이 기존 화장품 중 '나에게 제일 잘 맞았던' 제품들을 추천받을 수 있는 시스템을 구현하기로 함
  - 국내 Olive Young에도 적용할 수 있는 추천 시스템을 만들어보고 싶었음

### 🏎️ 총 42개의 데이터 중 선정된 최종 데이터
  **Product Data (제품 데이터)**
1. product_name: 제품의 전체 이름
2. brand_name: 제품 브랜드의 전체 이름
3. loves_count: 이 제품을 좋아요로 표시한 사람들의 수
4. rating: 사용자 리뷰를 바탕으로 한 제품의 평균 평점
5. reviews: 해당 제품에 대한 사용자 리뷰 수
6. variation_desc: 변형 유형에 대한 설명 (예: 피부 톤을 고려한 색상 등)
7. ingredients: 제품에 포함된 성분 목록. 변형이 있는 경우 각 변형에 대한 성분 리스트가 따로 있을 수 있음
8. price_usd: 제품의 정가 (미국 달러 기준)
9. highlights: 제품의 특징이나 주요 속성에 대한 태그 목록 (예: "비건", "매트 피니시")
10. primary_category: 제품이 속한 첫 번째 카테고리
11. secondary_category: 제품이 속한 두 번째 카테고리

  **Reviews Data (리뷰 데이터)**
1. author_id: 리뷰 작성자의 고유 식별자
2. rating: 리뷰 작성자가 부여한 제품의 평점 (1~5)
3. is_recommended: 리뷰 작성자가 이 제품을 추천하는지 여부 (1: 추천, 0: 추천하지 않음)
4. helpfulness: 리뷰의 유용성 지표, 긍정적인 피드백 수 / 전체 피드백 수
5. total_feedback_count: 해당 리뷰에 대한 총 피드백 수 (긍정적 및 부정적 피드백을 모두 포함)
6. total_neg_feedback_count: 해당 리뷰에 대해 부정적인 피드백을 남긴 사용자 수
7. total_pos_feedback_count: 해당 리뷰에 대해 긍정적인 피드백을 남긴 사용자 수
8. submission_time: 리뷰가 작성된 날짜 (yyyy-mm-dd 형식)
9. review_text: 리뷰의 본문 텍스트
10. review_title: 리뷰의 제목
11. skin_tone: 리뷰 작성자의 피부 톤 (예: fair, tan 등)
12. eye_color: 리뷰 작성자의 눈 색깔 (예: brown, green 등)
13. skin_type: 리뷰 작성자의 피부 타입 (예: combination, oily 등)
14. hair_color: 리뷰 작성자의 머리 색깔 (예: brown, auburn 등)
15. product_id: 리뷰가 작성된 제품의 고유 ID

### 🔦 데이터 전처리 과정
- 8,000개의 제품 데이터와 1,000,000개의 리뷰 데이터를 가지고 진행
  - 제품/리뷰 데이터 병합 
  - 결측치 제거
  - 필요한 데이터 구분 45 → 25 features
  - Random 추출
- 최종 10만개의 데이터셋으로 진행

### 🤖 프로그램 구조

#### 1. 좋아요♥️ TOP3 
- 카테고리를 선택하면 해당 카테고리의 '좋아요' 상위 3개의 제품을 알려주는 메뉴
  - 해당 제품의 제품명, 카테고리, 좋아요수, 하이라이터 출력
#### 2. 브랜드별 TOP3
- 브랜드를 선택하면 해당 브랜드의 '평점' 상위 3개의 제품을 알려주는 메뉴
  - 해당 제품의 제품명, 브랜드명, 평점, 하이라이트 출력
#### 3. 리뷰 & 평점
- 제품명을 선택하면 해당 제품의 리뷰와 평점을 알려주는 메뉴
  - 해당 제품의 리뷰, 평점, 하이라이트 출력
#### 4. 화장품 추천 1
- 추천받고 싶은 화장품을 추천하는 메뉴
  - 피부타입, 카테고리, 원하는 브랜드를 선택하면 추천 제품들 출력
#### 5. 화장품 추천 2
- 기존 화장품 기반으로 비슷한 성분의 화장품을 추천해주는 메뉴
  - 제품명을 선택하면 주요기능 및 주요성분을 안내해주며, CV와 TF-IDF로 비슷한 제품을 출력

### 🎞️ 유튜브 시연영상
[<img alt="OliveYoung의 시연영상" src="&quot;C://Users//playdata2//Pictures//Screenshots//youtude.png&quot;"/>](https://youtu.be/fcDj0I0Eeeg)




