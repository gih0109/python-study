# Chapter06-04
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API 를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임 아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures ProcessPoolExecutor, ThreadPoolExcutor

# GIL : 두 개 이상의 쓰레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우
#  -> 문제가 생기는 것을 방지하기 위해 GIL 실행, 리소스 전체에 락이 걸린다
#  -> Context Swith(문맥 교환)

# GIL 우회 : 멀티프로세싱 사용, CPython

import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 메인 함수
# 누적 합계 함수(제네레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Wortker Count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor, ThreadPoolExcutor 두 종류
    with futures.ProcessPoolExecutor() as excutor:
        # map -> 작업순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST) # map 은 모든 작업이 끝날 때까지 기다린다


    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 싷행
if __name__ == "__main__":
    main()