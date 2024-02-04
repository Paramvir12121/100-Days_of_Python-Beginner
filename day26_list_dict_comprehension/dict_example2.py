# sentence = input()
# # 🚨 Don't change code above 👆
# # Write your code below 👇

# words_list = sentence.split()

# result = {word:len(word) for word in words_list}

# print(result)

# Example 3 

weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {key:(value * 1.8) + 32 for (key,value) in weather_c.items()}


print(weather_f)