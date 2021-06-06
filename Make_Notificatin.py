# This programme is to make notification after a fix time of interval
# Here we have taken 10 Vocab words
import time

print("Here Is Your Word To Learn")


def repeat_dict():
    array = ["Intend : Have in mind as a purpose", "Concern : Something that interests you because it is important",
             "Utter : Without qualification", "Apparent : Clearly revealed to the mind or the senses or judgment",
             "Vain : Unproductive of success", "Appeal : Be attractive to",
             "League : An association of sports teams that organizes matches", "Yield : Give or supply",
             "Wander : Move or cause to move in a sinuous or circular course",
             "Harry : Annoy continually or chronically"]
    i = 0
    while i < len(array):
        print(array[i])
        i += 1
        time.sleep(5)
    repeat_dict()


repeat_dict()
