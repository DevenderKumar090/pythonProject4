##string concatenation(aka how to put strings together)
#Suppose we want to crate a string that says :Subscribe to ------"

youtuber = " Kylies ying" #some string variable


# a few ways to do this
print("subscribe" + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
#
# famous_person = input("Famous person:")
#
# madlib = f"Computer programming is so {adj}! It makes  me so excited all the time because\
# ilove to{verb1}.Stay hydrated and {verb2} like you are {famous_person}!"
#
# print(madlib)

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person")

madlib = f" You looks so great and {adj}! i like you so much when you always share the things like {verb1}.Sometimes its better to have \
much {verb2}.And  work {famous_person}!"

print(madlib)