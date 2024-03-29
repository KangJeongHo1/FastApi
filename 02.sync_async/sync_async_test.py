from fastapi import APIRouter
import time

router = APIRouter()

@router.get('/slow-sync-ping')
def slow_sync_ping():
    time.sleep(10)

    return {'msg':'pong'}

import asyncio
@router.get('/slow-async-ping')
async def slow_async_ping():
    await asyncio.sleep(10) # 10초를 기다린다. 하지만 다른 작업들은 계속 실행이 됌

    return {'msg':'pong'}

# 피보나치 수열 -> 무거운 연산 작업
# CPU에 부하가 걸리는 작업 (복잡한 연산): 동기
# I/O 비동기
def cpu_intensive_task():
    def fiboancci(n):
        if n <= 1:
            return n
        else: 
            return fiboancci(n-1) + fiboancci(n-2)

    result = fiboancci(35)
    return result

# Worst case
# CPU 부하 -> Evnet Loop에 부하가 걸림.
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {'msg': result}

# good case
# CPU에 부하가 많이 걸리는 작업은 이벤트 루프에서 분리 후
# 별도에 프로세스에서 실행

from concurrent.futures import ProcessPoolExecutor
def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task
        ) # CONTEXT SWITCHING

    return {'result': result}