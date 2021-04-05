# alexandru.miclea

C:\Users\alexm>curl localhost:5000/similarity/.\input\P1__en_.bpmn/.\input\P2__en_.bpmn
{
    "Similarity ": 95.75
}



Server Side:
C:\Users\alexm\AppData\Local\Programs\Python\Python39\lib\site-packages\fuzzywuzzy\fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning
  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
 * Debugger is active!
 * Debugger PIN: 109-449-654
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Process 1 :   Get Cup Poor coffee End Event Start Event //Activities from BPMN-File Process 1

Process 2 :   End Event Get Cup Poor coffee Put lid on Start Event  //Activities from BPMN-File Process 2

127.0.0.1 - - [05/Apr/2021 14:31:24] "GET /similarity/.\input\P1__en_.bpmn/.\input\P2__en_.bpmn HTTP/1.1" 200 -
