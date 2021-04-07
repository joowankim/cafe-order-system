# Cafe Order System

객체지향의 사실과 오해 1장에서 예시로 제시된 커피 주문 시나리오를 간단하게 구현해보는 프로젝트

## 목적

협력, 역할, 책임을 고려하여 설계해보자.

## 주문 시스템 도메인 사전

### Order

주문의 id, Bucket의 내용물, 각 Product 종류마다 수량에 대한 가격, 총 가격, 주문 날짜에 대한 정보를 가지고 있는 객체

### Product

상품의 id, 이름, 가격과 같은 정보를 가지고 있는 객체

### Bucket

Customer가 선택한 Product과 그 Product의 수량 정보 리스트

### Customer

1. Menu를 참조해 Product를 선택하고 
2. Bucket을 생성
3. OrderService에게 Bucket을 보내 Order 생성을 요청
4. Order를 Casher에게 보내 Bill 생성 요청

### Casher

1. Order를 가지고 구매자와 판매자 정보가 포함된 Bill 생성

### Bill

구매자와 판매자, Order 정보, 결제 방식, 청구 날짜가 포함된 객체 

### PaymentService

1. 결제 히스토리 관리
2. 결제 정보 생성
3. 환불 

### Receipt

구매자와 판매자, Order 정보, 결제 방식, 결제 날짜가 포함된 객체


## tests

- 소비자가 메뉴에게 아메리카노 정보를 요청
- 소비자가 지갑에게 돈을 요청
- 소비자가 판매자에게 아메리카노를 요청
    - 판매자가 계산기(?)에 요금 계산을 요청

- 구매 기록 저장
- 영수증 반환

- Order 객체 추가
  - 소비자 정보(card_info, phone_number)

## 협력: 커피 주문 처리

### 역할

#### Customer

- 책임
  - Order 생성하기
    - Menu에서 Coffee 선택 
      - product 선택
      - 수량 선택
      - 가격 계산
      - Bucket에 담기
    - Order 생성
    - Bucket 등록
    - 시간 기록
  
#### Menu

- 책임
  - Coffee 이름으로 커피 검색 후 정보 반환
  
#### Seller

- 책임
  - Order를 ReceiptMachine에 입력
  - Receipt 반환
  
#### ReceiptMachine

- 책임
  - 입력 받은 Order를 Receipt으로 생성 후 반환


## 1주차 목표

대략적인 커피 주문 시스템을 구현하자

## 2주차 목표

1. 각 객체를 엔티티와 값 객체로 분류하자
  - 각 값 객체의 동등성 테스트
  - 각 엔티티의 동일성 테스트
2. 쿼리와 명령을 분리하자
  - 쿼리: 조회된 내용 검증 테스트
  - 명령: 변경된 상태 확인 테스트
3. 메인 시나리오를 구현하자
   
## 3주차 목표

1. 커피 하나만 주문하는 게 아닌 다수의 상품 주문 구현
  - Order에 커피를 리스트로 받도록 추가 후 검증
  - Receipt을 만들때 금액 총합 및 커피 리스트 나열

2. 객체들의 행동을 기반으로 분류(추상화)해보자

3. 협력에 기반해 요청을 생각하고 각 객체에 요청에 맞는 책임과 행동을 부여하자

### 제품 구매 과정

1. 제품 선택
2. 주문 생성
3. 청구서 생성
4. 결제(여기선 상태를 바꾸는 등의 한 단계로 퉁쳐보자)
  - 결제 수단 선택
  - 결제 정보 인증
  - 결제 체결
5. 영수증 생성
6. 결제 사항 확인

## 4주차 목표

1. 제품 구매라는 협력에 대한 책임을 정의
2. 책임을 수행할 행동을 정의
3. 정의된 행동을 세분화
4. 세분화한 행동을 테스트로 구현
5. 구현된 테스트를 기반으로 협력을 다시 구현
6. 도메인 모델, 유스케이스, 협력을 생각하고 코드로 구현하기

### 유스케이스

- 유스케이스 명: 커피를 구매한다.
- 일차 액터: 소비자
- 주요 성공 시나리오:  
    1. 소비자가 상품 리스트를 확인한다.
    2. 소비자가 커피를 선택해 주문리스트(장바구니)에 담는다.
    3. 장바구니를 전달받은 점원이 주문을 생성한다.
    4. 주문을 확인한 소비자는 점원으로부터 청구서를 받는다.
    5. 청구서를 받은 소비자는 결제방식을 선택해 결제를 진행한다.
    6. 소비자의 결제를 확인한 점원은 영수증을 발급한다.
- 확장:
    1. 커피말고 다른거

### 제품 구매 테스트 케이스

1. 제품 선택
    - 선택한 상품들이 제대로 선택되어 반환되는지
      - 제대로 된 값이 들어갔을 때 제대로 반환하는지
      - 잘못된 값이 들어갔을 때 에러를 발생시키는지
    - 장바구니 생성
      - 선택된 물품들 리스트로 장바구니를 생성할 수 있는지
      - 물품들이 생성된 장바구니에 제대로 들어가 있는지
      - 잘못됫 물품들을 집어넣으면 에러를 발생시키는지
2. 주문 생성
    - 장바구니가 입력되었을 때 제대로된 값이 주문에 들어가 있는지
      - 주문 시간
      - id
      - 구매자
      - 장바구니
      - 가격 총합
      - 품목별 가격
    - 잘못된 값을 넣었을 때 에러를 발생시키는지
3. 청구서 생성
    - 받은 주문으로 청구서를 제대로 생성하는지
      - id
      - 청구 시간
      - 구매자
      - 판매자
      - 결제 수단
      - 결제 금액
      - 구매 품목
    - 잘못된 값에 대한 에러

4. 결제(여기선 상태를 바꾸는 등의 한 단계로 퉁쳐보자)
    - 결제 수단 선택
    - 결제 정보 인증
    - 결제 체결
5. 영수증 생성
    - 청구서에 결제에 대한 영수증을 제대로 발급하는지
      - id
      - 결제 시간
      - 구매자
      - 판매자
      - 결제 수단
      - 결제 금액
      - 구매 품목
    - 잘못된 값에 대한 에러
      
6. 결제 사항 확인
