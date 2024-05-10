# import nltk  

# nltk.download('punkt')
# nltk.download('stopwords') 

# from nltk.tokenize import word_tokenize , sent_tokenize 

# text = "hey shreyank nice to meet u, i am a robot ,i am ml engineer" 

# words = word_tokenize(text) 

# sentence =sent_tokenize(text) 

# print("words",words) 
# print("sentence",sentence)  

# from nltk.corpus import stopwords   

# stop_words = set(stopwords.words("english"))  

# filterword = [word for word  in words if word.lower() not in stop_words] 

# print("Filtered Words ", filterword) 


# Part of speech                   

# from nltk import pos_tag

# pos_tags = pos_tag(words)
# print("Part-of-Speech Tags:", pos_tags) 


# def respond (user_input): 
#     if "greet" in user_input.lower(): 
#         return "heelo sir i am good what about you " 
#     elif 'informastion' in user_input.lower(): 
#         return "ni batana aur puucho" 
    
#     else : 
#         return "kya kh rhe samajh ni ara"  

# while True : 
#     user_input = input("You:") 
#     if user_input.lower() == "exit": 
#         print("ohk , bhaaf jaao") 
#         break   
#     response =respond(user_input) 
#     print("chatbot :" , response) 

