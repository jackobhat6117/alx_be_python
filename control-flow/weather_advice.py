weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()


if weather == "sunny":
        advice = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
        advice = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
        advice = "Make sure to wear a warm coat and a scarf."
else:
        advice = "Sorry, I don't have recommendations for this weather."

   
print(advice)