from memory_stream_constructor import *

memory_stream = MemoryStream()

memory_object1 = MemoryObject()

memory_object1.set_recency("early today")
memory_object1.add_non_chats("0600","Just woke up!")

memory_object1.add_non_chats("0700","Packed the bag, had a lunch. Heading out for college.")
memory_object1.add_chats("0702", "Juan", "You coming for class today?")
memory_object1.add_chats("0703", "Rodriguez", "Nah man, got fever.")
memory_object1.add_chats("0703", "Juan", "Umm okay. Today's day is gonna be not so cool then. Sad emoji")
memory_object1.add_chats("0703", "Rodriguez", "Haha. Don't worry man. You better ask Jenny out tonight. haha")
memory_object1.add_chats("0703", "Juan", "Wish me luck!")
memory_object1.add_non_chats("0800","Attending the classes. They have begun now. Juan is busy.")
memory_object1.add_non_chats("1200","First batch of classse are over. Getting ready to go to canteen for the lunch")
memory_object1.add_non_chats("1600","Asked Jenny out on a date at 1800. She agreed.")
memory_object1.add_chats("1605", "Juan", "Rodriguez!! \n Man!! ")
memory_object1.add_chats("1606", "Rodriguez", "What happened dude?!")
memory_object1.add_chats("1609", "Juan", "She said yes!! \n I am soo excited and nervous as well...!!")
memory_object1.add_chats("1609", "Rodriguez", "WOW broo \n ask her out \n Ask her out!!!")
memory_object1.add_chats("1610", "Juan", "Definitely! Will try.")


memory_stream.append_memory(memory_object1)