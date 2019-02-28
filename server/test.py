# a=[[1,2],[3,4,5]]
# a=[{'a':1,'b':2,'c':3}]
# a='AAACU|||1332552|Asia Automotive Acquisition Corp|203022522|DELAWARE|DELAWARE|f'
# x=a.split('|')
# print(x)
#
# for x in range(0, 2):
#     print(type(str(x)))
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# aa =5
# # def xx():
# #     global aa
# #     aa=6
# # xx()
# # print (aa)

# import lib.tools

# import schedule
# import time
#
# def job():
#    print("I'm working...")
#
# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

# while 1:
#    schedule.run_pending()
#    time.sleep(1)

# for x in range (0,100):
#     print (x)
#     time.sleep(2)

# a = 44
# b = 2
# h = ""
#
# h = "111" if a>b else "222"
#
# print(h)

import asyncio

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(5)
#     print('... World!')
#
# # Python 3.7+
# asyncio.run(main())

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.call_soon(functools.partial(callable, arg1, arg2))

# import time
# import random
#
# def doTimeConsumingStep(N):
#     """
#     This represents the computational part of your simulation.
#
#     For the sake of illustration, I've set it up so that it takes a random
#     amount of time which is occasionally longer than the interval you want.
#     """
#     r = random.random()
#     computationTime = N * (r + 0.2)
#     print("...computing for %f seconds..."%(computationTime,))
#     time.sleep(computationTime)
#
#
# def timerTest(N=1):
#     repsCompleted = 0
#     beginningOfTime = time.clock()
#
#     start = time.clock()
#     goAgainAt = start + N
#     while 1:
#         print("Loop #%d at time %f"%(repsCompleted, time.clock() - beginningOfTime))
#         repsCompleted += 1
#         doTimeConsumingStep(N)
#         #If we missed our interval, iterate immediately and increment the target time
#         if time.clock() > goAgainAt:
#             print("Oops, missed an iteration")
#             goAgainAt += N
#             continue
#         #Otherwise, wait for next interval
#         timeToSleep = goAgainAt - time.clock()
#         goAgainAt += N
#         time.sleep(timeToSleep)
#
# timerTest()


# import lib.tools
#
# def aa(str):
#     print (str)
#
# lib.tools.set_interval(lib.tools.partial(aa,'ss'), 2)

# import time
# def update_iterate(symbol_list, index):
#     if index<len(symbol_list):
#         print (symbol_list[index])
#         index+=1
#         time.sleep(10)
#         update_iterate(symbol_list, index)
#     else:
#         print ('done')
# update_iterate([1,2,3,4,5],0)

# from datetime import date
# print(date.fromtimestamp(int("949381200")).strftime('%Y-%m-%d %H:%M:%S'))
# import random
# print (random.randint(30,45))

# l = [5,6,7,8]
# for x in range(len(l)):
#     # print (type(l[x]))
#     print (str(x)+':'+str(l[x]))

d = {'a':4,'b':5,'c':6}
for x in d:
    print (d[x])