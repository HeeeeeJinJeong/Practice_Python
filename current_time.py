from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
   time_stamp = strftime('%Y-%m-%d %X\t', localtime())
   log = time_stamp + log + '\n'

   with open(logfile, 'a') as f:
       f.writelines(log)

writelog(logfile, '첫번째 로깅 문장')

"""
실행 후 test.log를 열어보면 '2019-10-16 12:31:14	첫번째 로깅 문장' 이라고 나옴
"""