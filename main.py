import os
import time 
import schedule
import sys

def main():
	cwd = os.getcwd()
	os.system('python3 '+ cwd +'/VocabQuiz/VocabCheck.py')

main()

schedule.every(15).minutes.do(main)

while True:
	schedule.run_pending()
	time.sleep(1)
