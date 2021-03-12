# Cafe Order System

객체지향의 사실과 오해 1장에서 예시로 제시된 커피 주문 시나리오를 간단하게 구현해보는 프로젝트

## 목적

협력, 역할, 책임을 고려하여 설계해보자.

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
  - Menu에서 Coffee 골라 Order 생성하기
  
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
